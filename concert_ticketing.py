class Concert:
    def __init__(self):
        self.total_tickets = 100
        self.buyer_data = {}

    def sell(self, name, amount):
        if amount <= 0:
            print("Please enter a valid positive ticket amount!")
        elif amount > self.total_tickets:
            print(f"Insufficient tickets available! Tickets left: {self.total_tickets}")
        else:
            if name in self.buyer_data:
                self.total_tickets += self.buyer_data[name]  # Return the previous ticket count
            self.buyer_data[name] = amount  # Update ticket count for the person
            self.total_tickets -= amount

    def summary_purchase(self):
        print()
        for name, amount in self.buyer_data.items():
            print(f"{name} has purchased {amount} ticket(s).")
        print(f"Remaining number of tickets: {self.total_tickets}")

ticket1 = Concert()
while True:
    try:
        choose = int(
            input(
                "\nEnter 1 to purchase Ticket\n2 for printing summary purchases\n3 for exiting store: "
            ))
        if choose == 1:
            name = input("\nEnter your name: ")
            try:
                tickets = int(input("\nEnter Tickets you want: "))
                ticket1.sell(name, tickets)
            except ValueError:
                print("Invalid input for the number of tickets. Please enter a valid integer.")

        elif choose == 2:
            ticket1.summary_purchase()

        elif choose == 3:
            break

        else:
            print("Invalid Choice, Enter a valid number: ")

    except ValueError:
        print("Invalid Input, Enter a valid Number!")
