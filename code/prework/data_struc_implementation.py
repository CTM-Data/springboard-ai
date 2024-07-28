class DynamArray:
    def __init__(self, capacity):
        if capacity < 0:
            raise Exception(f'Illegal capacity: {capacity}')
        else:
            self.capacity = capacity

    def size(self):
        return 