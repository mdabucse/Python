# Custom ORM (Object-Relational Mapper)

A lightweight ORM built from scratch using Python metaclasses and descriptors. Supports model definition, field validation, query building, relationships, and lazy loading — all backed by SQLite.

## Project Structure

```
Task-3/
├── database.py   # SQLite connection and query execution
├── fields.py     # Field types: CharField, IntegerField, ForeignKey
├── model.py      # Base Model class with metaclass
├── queryset.py   # QuerySet for chained filtering and ordering
└── test.py       # Full demo
```

## How It Works

### Define Models

```python
from model import Model
from fields import CharField, IntegerField, ForeignKey

class User(Model):
    name  = CharField(max_length=100)
    email = CharField(max_length=255, unique=True)
    age   = IntegerField(nullable=True)

class Post(Model):
    title  = CharField(max_length=200)
    author = ForeignKey(User, related_name="posts")
```

### Create Tables

```python
User.create_table()
Post.create_table()
```

```
SQL: CREATE TABLE IF NOT EXISTS user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  age INTEGER
);
Table 'user' created.
```

### Save Records

```python
alice = User(name="Alice", email="alice@example.com", age=30)
alice.save()

post = Post(title="Hello World", author=alice)
post.save()
```

```
SQL: INSERT INTO user (name, email, age) VALUES (?, ?, ?)
Record saved: User(id=1)

SQL: INSERT INTO post (title, author_id) VALUES (?, ?)
Record saved: Post(id=1)
```

### Filter and Order

```python
users = User.filter(age__gte=25).order_by("-name").all()
```

```
SQL: SELECT * FROM user WHERE age >= ? ORDER BY name DESC
[User(id=1, name='Alice', email='alice@example.com', age=30)]
```

Supported lookups: `eq`, `gte`, `lte`, `gt`, `lt`

### Lazy-Loaded Relationships

```python
alice.posts   # triggers SQL only when accessed
```

```
SQL: SELECT * FROM post WHERE author_id = ?
[Post(id=1, title='Hello World', author_id=1)]
```

### Delete

```python
alice.delete()
```

```
SQL: DELETE FROM user WHERE id = ?
Record deleted: User(id=1)
```

## Run

```
python test.py
```

No external dependencies. Uses Python's built-in `sqlite3`.

## Key Concepts Used

| Concept | Where Used |
|---|---|
| Metaclass (`ModelMeta`) | Auto-collects fields, sets `_meta` on class |
| Descriptor protocol | `Field.__get__`, `__set__`, `__set_name__` |
| `__set_name__` | Registers FK as `author_id`, sets reverse relation |
| Method chaining | `QuerySet.filter().order_by().all()` |
| Lazy loading | `ReverseRelation.__get__` runs SQL on access |
