from registry import task

@task
def add(a, b):
    return a + b

@task
def multiply(a, b):
    return a * b