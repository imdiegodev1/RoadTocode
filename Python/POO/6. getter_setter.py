##Getters and Setters allows you to read and hange properties isight a
##class. It also can modify private attributes

class Bill:

    def __init__(self, owner, balance, coin):
        
        self.__owner = owner
        self.__balance = balance
        self.__coin = coin

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    def get_coin(self):
        return self.__coin

    def set_coin(self, coin):
        self.__coin == coin

def main():
    bill_1 = Bill('Diego', 500, 'usd')

    print(bill_1.get_owner())
    print(bill_1.get_balance())
    print(bill_1.get_coin())

    bill_1.set_coin('cop')
    print(bill_1.get_coin())

if __name__ == '__main__':
    main()