class Employee:
    def __init__(self, id, first_name, last_name, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return (
            f"Employee(id={self.id}, "
            f"first_name='{self.first_name}', "
            f"last_name='{self.last_name}', "
            f"age={self.age})"
        )