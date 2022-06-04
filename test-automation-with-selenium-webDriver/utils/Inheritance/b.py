from a import A


class B(A):
    def __init__(self, value1):
        super().__init__(value1, 45354454)
        print(f"from B value1 {value1}")
