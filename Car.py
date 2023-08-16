class Car:
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        if self.make != rhs.make:
            return self.make > rhs.make
        elif self.model != rhs.model:
            return self.model > rhs.model
        elif self.year != rhs.year:
            return self.year > rhs.year
        else:
            return self.price > rhs.price

    def __lt__(self, rhs):
        if self.make != rhs.make:
            return self.make < rhs.make
        elif self.model != rhs.model:
            return self.model < rhs.model
        elif self.year != rhs.year:
            return self.year < rhs.year
        else:
            return self.price < rhs.price

    def __eq__(self, rhs):
        if self and rhs:
            if (self.make == rhs.make) and (self.model == rhs.model) and (self.year == rhs.year) and (self.price == rhs.price):
                return True
            else:
                return False
        return False

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}"
