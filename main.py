class Vending_machine_product():
  
  def __init__(self, name, price, quantity):
    self.type = name
    self.price = price
    self.quantity = quantity
    self.revenue = 0

  def stock_update(self, amount):
    self.quantity += amount

  def price_update(self, newprice):
    self.price = newprice

  def buy(self):
    q_bought = int(input(f'How much of {self.type} would you like to buy?:'))

    if self.quantity > q_bought:
      self.quantity -= q_bought
      self.revenue += q_bought * self.price
    
    else:
      print(f'The requested amount of {self.type} is not available.The maximum amount we can provide is {self.quantity}.Please request again')

  def inventory_check(self):
    print(f'\nName: {self.type} \nPrice: {self.price} \nQuantity: {self.quantity} \nRevenue: {self.revenue}')
      
    

#Initializing the products and vending machine
milk = Vending_machine_product('whole milk', 1, 0)
pepsi = Vending_machine_product('pepsi', 2, 20)

#Updating the stock of whole milk
milk.stock_update(10)

#Updating the price of pepsi
pepsi.price_update(2.5)

#Customer transaction
pepsi.buy()
milk.buy()

#Checking what's happening with the vending machine after
pepsi.inventory_check()
milk.inventory_check()

  
    






