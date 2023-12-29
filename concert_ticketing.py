class concert:
  def __init__(self):
    self.total_tickets=100
    self.buyer_data={}

  def sell(self,name,amount):
    if amount > self.total_tickets:
      print(f"Insufficient Tickets availible! Tickets only left {self.total_tickets}")
    elif amount <= 0:
      print("Please enter a valid ticket amount!")
    else:
      if name in self.buyer_data:
        self.buyer_data[name] +=amount
      else:
        self.buyer_data[name]=amount
        self.total_tickets -= amount

  def summary_purchase(self):
    print()
    for name,amount in self.buyer_data.items():
      print(f"{name} has purchased {amount} Tickets.")
  
    print(f"\nRemaining number of Tickets are: {self.total_tickets}")

ticket1=concert()
while True:
  try:
    choose=int(input("\nEnter 1 to purchase Ticket\n2 for printing summary purchases\n3 for exiting store: "))
    if choose == 1:
      name=input("\nEnter your name: ")
      tickets=float(input("\nEnter Tickets you want: "))
      ticket1.sell(name,tickets)
  
    elif choose == 2:
      ticket1.summary_purchase()
  
    elif choose == 3:
      break

    else:
      print("Invalid Choice, Enter a valid number: ")

  except ValueError:
    print("Invalid Input, Enter a valid Number!")
