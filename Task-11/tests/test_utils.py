from minitest import fixture
import os

@fixture
def temp_file():
    filename = "temp_test.txt"
    with open(filename, "w") as f:
        f.write("hello")

    return filename

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()

def test_read_file(temp_file):
    content = read_file(temp_file)
    assert content == "hello"

def test_uppercase():
    assert "hello".upper() == "HELLO"

def test_divide_error():
    x = 1 / 0  # This will trigger ERROR