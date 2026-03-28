from database import Database


class QuerySet:
    def __init__(self, model):
        self.model = model
        self.table = model._meta["table_name"]

        self._where = []
        self._params = []
        self._order_by = None

    def filter(self, **kwargs):
        for key, value in kwargs.items():
            field, op = self._parse_lookup(key)
            sql_op = self._get_operator(op)

            self._where.append(f"{field} {sql_op} ?")
            self._params.append(value)

        return self

    def order_by(self, field):
        if field.startswith("-"):
            self._order_by = f"{field[1:]} DESC"
        else:
            self._order_by = f"{field} ASC"

        return self

    def all(self):
        query = f"SELECT * FROM {self.table}"

        if self._where:
            query += " WHERE " + " AND ".join(self._where)

        if self._order_by:
            query += f" ORDER BY {self._order_by}"

        rows = Database.fetch_all(query, self._params)

        return [self.model(**row) for row in rows]

    def _parse_lookup(self, key):
        if "__" in key:
            return key.split("__", 1)
        return key, "eq"

    def _get_operator(self, op):
        return {
            "eq": "=",
            "gte": ">=",
            "lte": "<=",
            "gt": ">",
            "lt": "<"
        }.get(op, "=")