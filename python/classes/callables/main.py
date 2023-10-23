class multiply:
    def __init__(self):
        print("instance created of mlutiply")

    def __call__(self, a: int, b: int):
        print(f"{a} * {b} = {a*b}")

instance = multiply()

instance(2, 3)
