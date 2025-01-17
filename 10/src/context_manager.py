class SampleContextManager:

    def __enter__(self):
        print(f"__enter__")
        return self
    
    def disp(self):
        print(f"display")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"__exit__")

with SampleContextManager() as manager:
    manager.disp()
