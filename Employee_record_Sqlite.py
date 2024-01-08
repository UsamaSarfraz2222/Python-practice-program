import sqlite3
class employee:
  def __init__(self,dbname="MyEmployeeSQLite.db"):
    self.conn=sqlite3.connect(dbname)
    self.curr=self.conn.cursor()
    self.curr.execute('''CREATE TABLE IF NOT EXISTS Bio_data(emp_code INTEGER PRIMARY KEY,
                            name TEXT,address TEXT,blood_group TEXT)''')

  def add_employee_data(self,emp_code,name,address,blood_group):
    self.curr.execute("INSERT OR IGNORE INTO Bio_data(emp_code,name,address,blood_group) VALUES(?,?,?,?)",(emp_code,name,address,blood_group))
    self.conn.commit()

  def search_employee(self,emp_code):
    self.curr.execute("SELECT * FROM Bio_data WHERE emp_code=?",(emp_code,))
    result=self.curr.fetchone()
    if result:
      print(
          f"\nEmployee Code: {result[0]}\nName: {result[1]}\nAddress: {result[2]}\nBlood Group: {result[3]}"
      )
    else:
      print(f"Employee with code {emp_code} not found.")

  def summary_employees(self):
    self.curr.execute("SELECT * FROM Bio_data")
    result=self.curr.fetchall()
    for i in result:
      print(f"\nEmployee Code: {i[0]}\nName: {i[1]}\nAddress: {i[2]}\nBlood Group: {i[3]}")

obj=employee()

try:
  while True:
    print("\n1. for Data Entry\n2. for Employee Code Search\n3. for Summary Employees\n4. to Exit record: ")
    choice = int(input("\nEnter 1 / 2 / 3: "))

    if choice == 1:
      emp_code = int(input("\nEnter Employee Code: "))
      name = input("Enter Name: ")
      address = input("Enter Address: ")
      blood_group = input("Enter your Blood Group: ")
      obj.add_employee_data(emp_code, name, address, blood_group)

    elif choice == 2:
      emp_code = int(input("Enter Employee Code to search: "))
      obj.search_employee(emp_code)

    elif choice==3:
      obj.summary_employees()

    elif choice ==4:
      break
      
    else:
      print("Invalid Input!")
finally:
  obj.conn.close()
