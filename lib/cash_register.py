#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity =1):
    self.total += price * quantity
    
  
  def apply_discount(self):
    discounted_price = self.total * (1 - self.discount)
    self.total = discounted_price
    return self.total
  
cash_register = CashRegister(0.20)

cash_register.add_item("macbook", 1000)

cash_register.apply_discount()

print(cash_register.total)


