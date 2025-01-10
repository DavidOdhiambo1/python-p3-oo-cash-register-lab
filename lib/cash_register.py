#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for i in range(quantity):
            self.items.append(title)
        self.previous_transactions.append(price * quantity) 
        
    def apply_discount(self):
        if self.discount > 0: 
            self.total = int(self.total * (1 - self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if len(self.previous_transactions) > 0:
            self.total -= self.previous_transactions.pop()
        else:
            print("No previous transactions to void.")
        


