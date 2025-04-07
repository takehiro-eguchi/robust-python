class SampleContextManager:
    def __init__(self, value: str):
        print(f"__init__, value = {value}")
        self.value = value

    def __enter__(self):
        print(f"__enter__, value = {self.value}")
        return self
    
    def disp(self):
        print(f"display")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"__exit__")

with SampleContextManager("Hello") as manager:
    print(f"{manager.__str__()}")
