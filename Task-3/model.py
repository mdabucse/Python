from fields import Field
from database import Database
from queryset import QuerySet


class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return super().__new__(cls, name, bases, attrs)

        fields = {}

        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                fields[key] = value

        new_class = super().__new__(cls, name, bases, attrs)

        new_class._meta = {
            "table_name": name.lower(),
            "fields": fields
        }

        return new_class


class Model(metaclass=ModelMeta):

    id = None

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")

        for field_name, field in self._meta["fields"].items():
            # Check for field.name first (e.g. "author_id" from DB row),
            # then fall back to the attribute name (e.g. "author" from user code).
            value = kwargs.get(field.name)
            if value is None:
                value = kwargs.get(field_name)
            # If someone passed a Model instance (e.g. author=alice), store its id
            if hasattr(value, "id") and hasattr(value, "_meta"):
                value = value.id
            self.__dict__[field.name] = value

    def __repr__(self):
        field_values = ", ".join(
            f"{field.name}={self.__dict__.get(field.name)!r}"
            for field in self._meta["fields"].values()
        )
        return f"{self.__class__.__name__}(id={self.id}, {field_values})"

    @classmethod
    def create_table(cls):
        table_name = cls._meta["table_name"]
        fields = cls._meta["fields"]

        columns = ["id INTEGER PRIMARY KEY AUTOINCREMENT"]

        for field in fields.values():
            columns.append(field.get_sql())

        cols_sql = ",\n  ".join(columns)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} (\n  {cols_sql}\n);"

        Database.execute(query)
        print(f"Table '{table_name}' created.")

    def save(self):
        table_name = self._meta["table_name"]
        fields = self._meta["fields"]

        field_names = []
        placeholders = []
        values = []

        for name, field in fields.items():
            # Read directly from __dict__ so FK fields return the _id integer
            value = self.__dict__.get(field.name)

            if value is not None:
                field_names.append(field.name)
                placeholders.append("?")
                values.append(value)

        if self.id:
            set_clause = ", ".join([f"{col}=?" for col in field_names])
            query = f"UPDATE {table_name} SET {set_clause} WHERE id=?"
            values.append(self.id)
        else:
            cols = ", ".join(field_names)
            ph = ", ".join(placeholders)
            query = f"INSERT INTO {table_name} ({cols}) VALUES ({ph})"

        cursor = Database.execute(query, values)

        if not self.id:
            self.id = cursor.lastrowid

        print(f"Record saved: {self.__class__.__name__}(id={self.id})")

    def delete(self):
        if not self.id:
            raise ValueError("Cannot delete unsaved object")

        table_name = self._meta["table_name"]
        deleted_id = self.id

        query = f"DELETE FROM {table_name} WHERE id = ?"
        Database.execute(query, [self.id])

        print(f"Record deleted: {self.__class__.__name__}(id={deleted_id})")
        self.id = None

    @classmethod
    def filter(cls, **kwargs):
        return QuerySet(cls).filter(**kwargs)

    @classmethod
    def all(cls):
        return QuerySet(cls).all()

    @classmethod
    def get(cls, **kwargs):
        results = cls.filter(**kwargs).all()

        if not results:
            raise ValueError(f"{cls.__name__} not found")

        if len(results) > 1:
            raise ValueError(f"Multiple {cls.__name__} found")

        return results[0]