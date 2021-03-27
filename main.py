class Budget:
    def __init__(self, allowance):
        self.allowance = allowance

    def transfer(self):
        # FIXME: Create transfer method for transferring funds from one category to another.

    def withdrawl(self):
        # FIXME: Create withdrawl method for withdrawing a given amount from a category

    def deposit(self):
        # FIXME: Create deposit method for depositing spe

food = Budget(100.00)
clothing = Budget(40.00)

print('Food budget: ${:.2f}'.format(food.allowance))
print('Clothing budget: ${:.2f}'.format(clothing.allowance))