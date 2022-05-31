class flat_Rate:

    def __init__(self, fixed_amount):
        self.fixed_amount = fixed_amount

    def calculate(self, amount):
        return amount - self.fixed_amount


class variable_rate:

    def __init__(self, percentage):
        self.percentage = percentage

    def calculate(self, amount):
        return amount - (amount * self.percentage)


class Client:

    def __init__(self, billing_strategy):
        self.billing_strategy = billing_strategy

    def generate_bill(self, total):
        return self.billing_strategy.calculate(total)


if __name__ == '__main__':
    flat = flat_Rate(10)
    var = variable_rate(0.2)

    client1 = Client(flat)
    client2 = Client(var)

    print(client1.generate_bill(100))
    print(client2.generate_bill(200))

    
