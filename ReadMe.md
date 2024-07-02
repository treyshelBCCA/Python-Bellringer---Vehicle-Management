# Vehicle Management Console Application

This is a simple console application written in Python that allows users to manage a collection of vehicles. The application provides functionalities to add, view, update, and delete vehicles. Each vehicle is represented by a data class, and one of the fields is a dictionary to store additional details about the vehicle.

### Features

- [ ] Add a new vehicle
- [ ] View all vehicles
- [ ] Update a vehicle's details
- [ ] Delete a vehicle by its ID
- [ ] Exit the application

_Notes_:
I have already created the dataclass and main() function for you. You will need to fill in the functions `add_vehicle(vehicles, id, make, model, year, details)`, `view_vehicles(vehicles)`, `update_vehicle(vehicles, id, make=None, model=None, year=None, details=None):`, `delete_vehicle(vehicles, id)`. You will remove anywhere it says `pass` and fill in the appropriate code to make the function work according to the example output below. You will not need to change anything in the `main.py` function.

```
Vehicle Management System
1. Add a new vehicle
2. View all vehicles
3. Update a vehicle's details
4. Delete a vehicle
5. Exit
Enter your choice: 1
Enter vehicle ID: 101
Enter vehicle make: Toyota
Enter vehicle model: Camry
Enter vehicle year: 2020
Enter detail key (or 'done' to finish): color
Enter value for color: Red
Enter detail key (or 'done' to finish): mileage
Enter value for mileage: 15000
Enter detail key (or 'done' to finish): done
Vehicle added successfully!

Vehicle Management System
1. Add a new vehicle
2. View all vehicles
3. Update a vehicle's details
4. Delete a vehicle
5. Exit
Enter your choice: 2
Vehicle(id=101, make='Toyota', model='Camry', year=2020, details={'color': 'Red', 'mileage': '15000'})

Vehicle Management System
1. Add a new vehicle
2. View all vehicles
3. Update a vehicle's details
4. Delete a vehicle
5. Exit
Enter your choice: 3
Enter vehicle ID to update: 101
Updating vehicle: Vehicle(id=101, make='Toyota', model='Camry', year=2020, details={'color': 'Red', 'mileage': '15000'})
Enter new vehicle make (or press enter to keep current):
Enter new vehicle model (or press enter to keep current):
Enter new vehicle year (or press enter to keep current):
Enter detail key to update (or 'done' to finish): mileage
Enter new value for mileage: 16000
Enter detail key to update (or 'done' to finish): owner
Enter value for owner: John Doe
Enter detail key to update (or 'done' to finish): done
Vehicle updated successfully!

Vehicle Management System
1. Add a new vehicle
2. View all vehicles
3. Update a vehicle's details
4. Delete a vehicle
5. Exit
Enter your choice: 2
Vehicle(id=101, make='Toyota', model='Camry', year=2020, details={'color': 'Red', 'mileage': '16000', 'owner': 'John Doe'})

Vehicle Management System
1. Add a new vehicle
2. View all vehicles
3. Update a vehicle's details
4. Delete a vehicle
5. Exit
Enter your choice: 4
Enter vehicle ID to delete: 101
Vehicle deleted successfully!

Vehicle Management System
1. Add a new vehicle
2. View all vehicles
3. Update a vehicle's details
4. Delete a vehicle
5. Exit
Enter your choice: 5
Exiting the application...


```
