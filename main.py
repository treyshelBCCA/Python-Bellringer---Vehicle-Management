from dataclasses import dataclass

@dataclass
class Vehicle:
    id: int
    make: str
    model: str
    year: int
    details: dict 

def add_vehicle(vehicles, id, make, model, year, details):
    pass
    return "Vehicle added successfully!"

def view_vehicles(vehicles):
    if not vehicles:
        return "No vehicles available."
    else:
        pass

def update_vehicle(vehicles, id, make=None, model=None, year=None, details=None):
    for vehicle in vehicles:
        if vehicle.id == id:
            pass
            return "Vehicle updated successfully!"
    return "Vehicle not found."

def delete_vehicle(vehicles, id):
    pass
    return "Vehicle deleted successfully!"

def main():
    vehicles = []

    while True:
        print("\nVehicle Management System")
        print("1. Add a new vehicle")
        print("2. View all vehicles")
        print("3. Update a vehicle's details")
        print("4. Delete a vehicle")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            id = int(input("Enter vehicle ID: "))
            make = input("Enter vehicle make: ")
            model = input("Enter vehicle model: ")
            year = int(input("Enter vehicle year: "))
            details = {}
            while True:
                key = input("Enter detail key (or 'done' to finish): ")
                if key == 'done':
                    break
                value = input(f"Enter value for {key}: ")
                details[key] = value
            print(add_vehicle(vehicles, id, make, model, year, details))

        elif choice == '2':
            print(view_vehicles(vehicles))

        elif choice == '3':
            id = int(input("Enter vehicle ID to update: "))
            make = input("Enter new vehicle make (or press enter to keep current): ")
            model = input("Enter new vehicle model (or press enter to keep current): ")
            year = input("Enter new vehicle year (or press enter to keep current): ")
            year = int(year) if year else None
            details = {}
            while True:
                key = input("Enter detail key to update (or 'done' to finish): ")
                if key == 'done':
                    break
                value = input(f"Enter new value for {key}: ")
                details[key] = value
            print(update_vehicle(vehicles, id, make, model, year, details))

        elif choice == '4':
            id = int(input("Enter vehicle ID to delete: "))
            print(delete_vehicle(vehicles, id))

        elif choice == '5':
            print("Exiting the application...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
