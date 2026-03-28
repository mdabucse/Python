class Field:
    def __init__(self, nullable=False, unique=False):
        self.name = None
        self.nullable = nullable
        self.unique = unique

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value):
        if not self.nullable and value is None:
            raise ValueError(f"{self.name} cannot be NULL")

    def get_sql(self):
        raise NotImplementedError


class CharField(Field):
    def __init__(self, max_length, **kwargs):
        super().__init__(**kwargs)
        self.max_length = max_length

    def validate(self, value):
        super().validate(value)

        if value is not None:
            if not isinstance(value, str):
                raise TypeError(f"{self.name} must be a string")

            if len(value) > self.max_length:
                raise ValueError(f"{self.name} exceeds max length {self.max_length}")

    def get_sql(self):
        sql = f"{self.name} VARCHAR({self.max_length})"

        if not self.nullable:
            sql += " NOT NULL"

        if self.unique:
            sql += " UNIQUE"

        return sql


class IntegerField(Field):
    def validate(self, value):
        super().validate(value)

        if value is not None and not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")

    def get_sql(self):
        sql = f"{self.name} INTEGER"

        if not self.nullable:
            sql += " NOT NULL"

        if self.unique:
            sql += " UNIQUE"

        return sql


class ForeignKey(Field):
    def __init__(self, to, related_name=None, **kwargs):
        super().__init__(**kwargs)
        self.to = to
        self.related_name = related_name

    def __set_name__(self, owner, name):
        self.name = f"{name}_id"

        if self.related_name:
            setattr(self.to, self.related_name, ReverseRelation(owner, name))

    def __get__(self, instance, owner):
        if instance is None:
            return self

        fk_id = instance.__dict__.get(self.name)

        if fk_id is None:
            return None

        return self.to.get(id=fk_id)

    def __set__(self, instance, value):
        if hasattr(value, "id"):
            instance.__dict__[self.name] = value.id
        else:
            instance.__dict__[self.name] = value

    def get_sql(self):
        return f"{self.name} INTEGER"


class ReverseRelation:
    def __init__(self, model, field_name):
        self.model = model
        self.field_name = field_name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return self.model.filter(**{f"{self.field_name}_id": instance.id}).all()