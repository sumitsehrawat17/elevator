
# Elevator System Project

This Django project implements an Elevator System with various capabilities such as moving up and down, opening and closing doors, starting and stopping running, displaying the current status, and deciding which elevator to associate with each floor. The project provides a set of APIs for managing the elevator system and its operations.

## Requirements

The following are the requirements for the Elevator System project:

A. Each elevator has the following capabilities:
- Move Up and Down
- Open and Close Door
- Start and Stop Running
- Display Current Status
- Decide whether to move up or down, based on a list of requests from users.

B. Elevator System takes care of:
- Deciding which lift to associate with each floor
- Marking elevators as available or busy
- Marking elevators as operational or under maintenance

C. Assumptions:
- Number of elevators in the system is defined during initialization.
- Elevator System has only one button per floor.
- Once the elevator reaches its called point, it moves either up or down based on the requested floor.
- Assume the API calls for elevator movement reflect immediately.

D. APIs provided:
- Initialize the elevator system to create 'n' elevators in the system.
- Fetch all requests for a given elevator.
- Fetch the next destination floor for a given elevator.
- Fetch whether the elevator is currently moving up or down.
- Save a user request to the list of requests for an elevator.
- Mark an elevator as not working or in maintenance.
- Open/close the door.

## Technologies Used

- Django: A high-level Python web framework for building web applications.
- Django REST Framework (DRF): A powerful and flexible toolkit for building Web APIs.

## API Endpoints

- `POST /elevator-systems/elevatorsystem/`: Initialize the elevator system with 'n' elevators and with the name of elevator system.
- `GET /elevators/{elevator_id}/ElevatorRequests/`: Fetch all requests for a given elevator.
- `GET /elevators/{elevator_id}/`: Fetch the next destination floor for a given elevator and Fetch whether the elevator is currently moving up or down..
- `POST /elevators/{elevator_id}/move/`: Move the elevator to a specified destination floor.
- `POST /elevators/{elevator_id}/Operational/`: Mark an elevator as operational or under maintenance.
- `GET /elevators/{elevator_id}/OpenDoor/`: Open the door of the elevator.
- `GET /elevators/{elevator_id}/CloseDoor/`: Close the door of the elevator.
- `POST /requests/decide/`: Make a request to the elevator system to decide which elevator to use based on the floor and elevator system name.

## Getting Started

To run the Elevator System project locally, follow these steps:

1. Clone the repository:

   ```
   git clone <repository-url>
   cd elevatorsystem
   ```

2. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database and Redis cache according to your configuration. Update the database and cache settings in the `settings.py` file.

4. Apply database migrations:

   ```
   python manage.py migrate
   ```

5. Run the development server:

   ```
   python manage.py runserver
   ```

6. Access the API endpoints through the browser or a tool like Post
