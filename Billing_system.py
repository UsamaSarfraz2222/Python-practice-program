class electric_bill:

  def __init__(self):
    self.current_units = []

  def below_300(self, units):
    self.current_units.append(units)
    current_units = self.calculation()
    if current_units <= 300:
      result_bel300 = current_units * 22
      print(f"\nYour current bill is {result_bel300}")
    else:
      result_over300 = current_units * 35
      print(f"\nYour current bill is {result_over300}")


  def calculation(self):
    previous_units = 0
    for units in self.current_units:
      current_units = units - previous_units
      previous_units = units
    return current_units

  def summary_bills(self):
    months = ["Jan", "Feb", "March", "April", "May"]
    print("Your Units Consumed Summary is: ")
    previous = 0
    for month, i in zip(months, self.current_units):
      x = i - previous
      if x <=300:
        y=x*22
        z=22
      elif x > 300:
        y=x*35
        z=35
      print(f"Units consumed in month {month} are {i} = Calculated units are {x} x {z} and bill is {y}")
      previous = i


billing1 = electric_bill()
while True:
  choose = int(input("1. For Units check 2. For Printing Summary: "))
  if choose == 1:
    user_units = float(input("\nEnter your units consumed: "))
    billing1.below_300(user_units)

  elif choose == 2:
    billing1.summary_bills()
