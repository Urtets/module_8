class Context:
    values = ()

    def __enter__(self):
        self.values = list(self.values)
        return self.values

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.values = tuple(self.values)
    # def append(self, value):
    #     some_list = list(self.values)
    #     some_list.append(value)
    #     self.values = tuple(some_list)
    # def __str__(self):
    #     return list(self.values)


if __name__ == '__main__':
    cm = Context()

    print(cm.values)  # Result: ()

    with cm as list_:
        list_.append(4)

    print(cm.values)  # Result: (4,)