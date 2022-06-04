import b


class C(b.B):
    def __init__(self):
        super().__init__("nu ma")
        print("Class C is running")


C()
