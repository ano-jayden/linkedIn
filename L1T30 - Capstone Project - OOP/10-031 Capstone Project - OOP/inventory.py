from tabulate import tabulate

class Shoe:
    """
    A class to represent a shoe.
    Attributes:
        country (str): The country of origin.
        code (str): The product code.
        product (str): The product name.
        cost (float): The cost of the shoe.
        quantity (int): The quantity available in inventory.
    """

    def __init__(self, country, code, product, cost, quantity):
        """
        Initializes the Shoe object with the provided attributes.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)  # Ensure cost is stored as a float
        self.quantity = int(quantity)  # Ensure quantity is stored as an integer

    def get_cost(self):
        """
        Returns the cost of the shoe.
        """
        return self.cost

    def get_quantity(self):
        """
        Returns the quantity of the shoe.
        """
        return self.quantity

    def __str__(self):
        """
        Returns a string representation of the shoe object.
        This is useful for printing the object details.
        """
        return (
            f"Product: {self.product}, Code: {self.code}, Country: {self.country}, "
            f"Cost: {self.cost}, Quantity: {self.quantity}"
        )


# List to store all Shoe objects
shoe_list = []


def read_shoes_data():
    """
    Reads shoe data from 'inventory.txt' and populates the shoe_list.
    If the file is not found, it prints an error message.
    """
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the header line
            for line in file:
                # Split each line by comma and unpack the values
                country, code, product, cost, quantity = line.strip().split(",")
                # Create a Shoe object with the unpacked values
                shoe = Shoe(country, code, product, cost, quantity)
                # Add the shoe to the shoe_list
                shoe_list.append(shoe)
        print("Shoes data read successfully!")  # Confirmation message
    except FileNotFoundError:
        print("The file inventory.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def capture_shoes():
    """
    Captures shoe details from the user via input and adds a new Shoe object to the shoe_list.
    """
    # Prompt the user for shoe details
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product name: ")
    cost = input("Enter the cost: ")
    quantity = input("Enter the quantity: ")

    # Create a new Shoe object with the provided details
    shoe = Shoe(country, code, product, cost, quantity)
    # Add the shoe to the shoe_list
    shoe_list.append(shoe)
    print("Shoe added successfully!")  # Confirmation message


def view_all():
    """
    Displays all shoes in the inventory in a tabulated format.
    If the inventory is empty, it notifies the user.
    """
    if not shoe_list:
        print("No shoes in inventory.")  # Notify if the list is empty
    else:
        # Create a table for display using the tabulate module
        table = [[shoe.product, shoe.code, shoe.country, shoe.cost, shoe.quantity] for shoe in shoe_list]
        print(tabulate(table, headers=["Product", "Code", "Country", "Cost", "Quantity"], tablefmt="grid"))


def re_stock():
    """
    Identifies the shoe with the lowest quantity in the inventory.
    Allows the user to increase the quantity if desired.
    """
    if not shoe_list:
        print("No shoes in inventory.")  # Notify if the list is empty
    else:
        # Find the shoe with the lowest quantity using the min function
        min_shoe = min(shoe_list, key=lambda x: x.get_quantity())
        print(f"The shoe with the lowest quantity is: {min_shoe}")
        
        # Ask the user if they want to add more quantity
        add_quantity = input("Do you want to add more to the quantity? (yes/no): ")
        if add_quantity.lower() == "yes":
            # Prompt for additional quantity and update the shoe's quantity
            additional_qty = int(input("Enter the quantity to add: "))
            min_shoe.quantity += additional_qty
            print(f"Updated quantity for {min_shoe.product} is now {min_shoe.quantity}")
            update_inventory_file()  # Update the inventory file with new quantity


def search_shoe():
    """
    Searches for a shoe in the inventory by its code and displays its details.
    """
    code = input("Enter the shoe code: ")  # Prompt for shoe code
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)  # Print shoe details if found
            return
    print("Shoe not found.")  # Notify if the shoe is not in the list


def value_per_item():
    """
    Calculates and displays the total value of each shoe type based on its cost and quantity.
    """
    for shoe in shoe_list:
        # Calculate value as cost multiplied by quantity
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product}: Value = {value}")  # Display the value


def highest_qty():
    """
    Identifies the shoe with the highest quantity in inventory and displays it.
    """
    if not shoe_list:
        print("No shoes in inventory.")  # Notify if the list is empty
    else:
        # Find the shoe with the highest quantity using the max function
        max_shoe = max(shoe_list, key=lambda x: x.get_quantity())
        print(f"The shoe with the highest quantity is: {max_shoe}, and it's on sale!")  # Notify the user


def update_inventory_file():
    """
    Updates the inventory file ('inventory.txt') with the current data in shoe_list.
    """
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")  # Write header
        for shoe in shoe_list:
            # Write each shoe's data to the file
            file.write(
                f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
            )
    print("Inventory file updated successfully!")  # Confirmation message


def main_menu():
    """
    Displays the main menu and handles user input to navigate through the program options.
    """
    while True:
        # Display menu options
        print("\nShoe Inventory Menu")
        print("1. Read Shoes Data")
        print("2. Capture Shoes")
        print("3. View All Shoes")
        print("4. Re-stock Shoes")
        print("5. Search Shoe")
        print("6. Calculate Value per Item")
        print("7. Highest Quantity Shoe")
        print("8. Exit")
        choice = input("Enter your choice: ")

        # Execute the corresponding function based on the user's choice
        if choice == "1":
            read_shoes_data()
        if choice == "2":
            capture_shoes()
        if choice == "3":
            view_all()
        if choice == "4":
            re_stock()
        if choice == "5":
            search_shoe()
        if choice == "6":
            value_per_item()
        if choice == "7":
            highest_qty()
        if choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")  # Notify the user of invalid input


# Start the program by displaying the main menu
main_menu()