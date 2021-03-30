class Budget:
    def __init__(self, name):
        self.amount = 0.00
        self.name = ''

    def transfer(self, receiving_category, amount):
        # FIXME: Create transfer method for transferring funds from one category to another.
        return -1

    def withdrawl(self, amount):
        # FIXME: Create withdrawl method for withdrawing a given amount from a category
        return -1

    def deposit(self, amount):
        # FIXME: Create deposit method for depositing spe
        return -1

def main():
    categories_list = []
    user_input = int(input('1: Check Total Balance\n2: Deposit\n3: Withdrawl\n4: Transfer\n5: Add New Category\n6: Balance Breakdown\n0: Quit\n'))
    while user_input != 0:

        user_input = int(input('1: Check Total Balance\n2: Deposit\n3: Withdrawl\n4: Transfer\n5: Add New Category\n6: Balance Breakdown\n0: Quit\n'))
    print('Thank you!')

if __name__ == '__main__':
    main()