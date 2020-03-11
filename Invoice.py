

class Invoice:
    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        totalImpure = 0
        for k, v in products.items():
            totalImpure += float(v['unit_price']) * int(v['qnt'])
        totalImpure = round(totalImpure, 2)
        return totalImpure

    def totalDiscount(self, products):
        totalDiscount = 0
        for k, v in products.items():
            totalDiscount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
        totalDiscount = round(totalDiscount, 2)
        return totalDiscount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput

