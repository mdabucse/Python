## Call Back Function
* a function that is passed into another function 
 ```python 
    def greet(name):
    print(f"Hello {name}")

    def process_user(callback):
        print("Processing...")
        callback("Abu")   # calling the callback

    process_user(greet)
 ```
