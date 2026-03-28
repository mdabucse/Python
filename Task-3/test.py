from model import Model
from fields import CharField, IntegerField, ForeignKey


class User(Model):
    name = CharField(max_length=100)
    email = CharField(max_length=255, unique=True)
    age = IntegerField(nullable=True)


class Post(Model):
    title = CharField(max_length=200)
    author = ForeignKey(User, related_name="posts")


# Create tables
print("--- Create Tables ---")
User.create_table()
Post.create_table()

# Insert a user
print("\n--- Save User ---")
alice = User(name="Alice", email="alice@example.com", age=30)
alice.save()

# Insert a post linked to alice
print("\n--- Save Post ---")
post = Post(title="Hello World", author=alice)
post.save()

# Filter + order query
print("\n--- Filter Query ---")
users = User.filter(age__gte=25).order_by("-name").all()
print(users)

# Lazy-loaded reverse relation
print("\n--- Lazy Load alice.posts ---")
print(alice.posts)

# Delete
print("\n--- Delete User ---")
alice.delete()