class Employee:

  def __init__(self):
    self.emp_data = {}

  def add_employee_data(self, emp_code, name, address, blood_group):
    self.emp_data[emp_code] = [name, address, blood_group]

  def emp_code_search(self, emp_code):

    if emp_code in self.emp_data:
      values = self.emp_data[emp_code]
      print(
          f"\nEmployee Code: {emp_code}\nName: {values[0]}\nAddress: {values[1]}\nBlood Group: {values[2]}"
      )
    else:
      print(f"Employee with code {emp_code} not found.")


emp01 = Employee()

while True:
  print("\n1. for Data Entry\n2. for Employee Code Search\n3. for Exiting")
  choice = int(input("\nEnter 1 / 2 / 3: "))

  if choice == 1:
    emp_code = int(input("\nEnter Employee Code: "))
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    blood_group = input("Enter your Blood Group: ")
    emp01.add_employee_data(emp_code, name, address, blood_group)

  elif choice == 2:
    search_code = int(input("Enter Employee Code to search: "))
    emp01.emp_code_search(search_code)

  else:
    break
