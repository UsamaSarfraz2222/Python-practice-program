# class GroceryCalculator:

#   def __init__(self):
#     self.items = {}

#   def add_item(self, item, price):
#     self.items[item] = price
#     print(f"{item} added to the list. Price: ${price}")

#   def calculate_totals(self):
#     subtotal = sum(self.items.values())
#     tax_rate = 0.08  # You can adjust the tax rate as needed
#     tax = subtotal * tax_rate
#     total = subtotal + tax
#     return subtotal, tax, total

#   def print_receipt(self):
#     print("\n--- Grocery List ---")
#     for item, price in self.items.items():
#       print(f"{item}: ${price}")
#     subtotal, tax, total = self.calculate_totals()
#     print(f"\nSubtotal: ${subtotal:.2f}")
#     print(f"Tax (8%): ${tax:.2f}")
#     print(f"Total: ${total:.2f}")


# def main():
#   grocery_calculator = GroceryCalculator()

#   while True:
#     print("\n1. Add Item\n2. Print Receipt\n3. Quit")
#     choice = input("Enter your choice (1/2/3): ")

#     if choice == '1':
#       item = input("Enter item name: ")
#       price = float(input("Enter item price: "))
#       grocery_calculator.add_item(item, price)
#     elif choice == '2':
#       grocery_calculator.print_receipt()
#     elif choice == '3':
#       print("Exiting the grocery calculator. Goodbye!")
#       break
#     else:
#       print("Invalid choice. Please enter a valid option.")


# if __name__ == "__main__":
#   main()

class GroceryCalculator:
  def __init__(self):
      self.items = {}
      self.subtotal = 0
      self.tax_rate = 0.08
      self.tax = 0
      self.total = 0

  def add_items(self,item,price):
      self.items[item]=price
      self.subtotal = sum(self.items.values())
      self.tax = self.subtotal * self.tax_rate
      self.total = self.subtotal + self.tax
      print(f"Item {item} with price ${price} added to cart.\n")

  def print_receipt(self):
      print(f"Sub total= {self.subtotal}")
      print(f"Tax= {self.tax}")
      print(f"Gross Total={self.total}")

grocery_calculator = GroceryCalculator()

while True:
  print("\n1. Add Item\n2. Print Receipt\n3. Quit")
  choice = input("Enter your choice (1/2/3): ")

  if choice == '1':
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    grocery_calculator.add_items(item, price)
  elif choice == '2':
    grocery_calculator.print_receipt()
  elif choice == '3':
    print("Exiting the grocery calculator. Goodbye!")
    break
  else:
    print("Invalid choice. Please enter a valid option.")
