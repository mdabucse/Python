TASK_REGISTRY = {}

def task(func):
    """
    Decorator to register a function as a task
    """
    TASK_REGISTRY[func.__name__] = func
    return func