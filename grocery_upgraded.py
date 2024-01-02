class mart:
  products = {
      "milk": {
          "quantity": 10,
          "price": 50
      },
      "bread": {
          "quantity": 10,
          "price": 30
      },
      "eggs": {
          "quantity": 24,
          "price": 30
      },
      "choclate": {
          "quantity": 10,
          "price": 25
      }
  }

  def __init__(self):
    self.cart={}


  def calculation(self, name, amount):
    if name in mart.products and mart.products[name]["quantity"] >= amount:
      if name in self.cart:
        self.cart[name]["Quantity"] += amount

      else:
        self.cart[name] = {
            "Quantity": amount,
            "Price$": mart.products[name]["price"]
        }

      mart.products[name]["quantity"] -= amount

      self.print_receipt()

    else:
      print(f"Sorry we dont have {name} in our inventroy!")


  def print_receipt(self):
    print("*-------------------------*")
    gross_total = 0
    for item, details in self.cart.items():
      total_item = details["Quantity"] * details["Price$"]
      print(
          f"Item: {item} Quantity: {details['Quantity']} X Price: {details['Price$']} = {total_item}"
      )
      gross_total += total_item
    print("*----------------*")


list_customer = {}
current_account = None

while True:
  print("^^^^^^^^^^^^^^^^^^^^^")
  print(
      "1.to create customer account\n2.for switching customer account\n3. for purchasing a product\n4. for Quitting\n5. for printing todays inventory sale: "
  )
  choose = int(input("\nEnter 1 / 2 / 3 / 4 / 5: "))

  if choose == 1:
    account_name = input("Enter Account name to create: ")
    current_account=mart()
    list_customer[account_name] = current_account
    print(f"\nAccount created with name {account_name}")

  elif choose == 2:
    account_name = input("\nEnter Account name to switch: ")
    if account_name in list_customer:
      current_account = list_customer[account_name]
      print(f"Account Switched to {account_name}")

    else:
      list_customer[account_name] = mart()
      current_account = list_customer[account_name]
      print(
          f"No Account record found, created a new account named {account_name}"
      )

  elif choose == 3:
    if current_account is None:
      print("Please Create or Switch account first!")

    else:
      name_product = input("\nEnter Product name to purchase: ")
      quantity_product = int(input("Enter quantity of product: "))
      current_account.calculation(name_product, quantity_product)

  elif choose == 4:
    break

  elif choose ==5:
    if not list_customer:
      print("Sorry no sale done today!")

    else:
      print("*-----Todays Inventory Sale-----*")
      for account_name,mart in list_customer.items():
        print(f"\nAccount {account_name}")
        mart.print_receipt()

  else:
    print("Please enter a valid choice: ")
