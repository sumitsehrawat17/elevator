from .models import Elevator, Request
from django.db.models import F

# this function is deciding which elevator to call 
def decide_elevator(floor):
    elevator = Elevator.objects.all().order_by(abs(F('current_floor')-floor))
    return elevator[0].id

def move_elevator(elevator_id,next_floor):
    elevator = Elevator.objects.get(id=elevator_id)
    # requests = Request.objects.filter(elevator=elevator,is_complete=False)
    if requests:
        if next_floor > elevator.current_floor:
            elevator.direction = 'up'
            elevator.is_busy = True
        elif next_floor < elevator.current_floor:
            elevator.direction = 'down'
            elevator.is_busy = True
        else:
            elevator.direction = 'stopped'
            elevator.is_busy = False
            
        elevator.save()


def open_door(elevator_id):
    elevator = Elevator.objects.get(id=elevator_id)
    requests = Request.objects.filter(elevator=elevator,is_complete=False)
    next_floor = requests[0].floor
    elevator.current_floor = next_floor
    elevator.is_open = True
    elevator.is_busy = False
    elevator.save()
    print("Doors are Open")
    

    


def close_door(elevator_id):
    elevator = Elevator.objects.get(id=elevator_id)
    requests = Request.objects.filter(elevator=elevator,is_complete=False)
    destination = requests[0].destination_floor
    elevator.current_floor = destination
    elevator.is_open = False
    elevator.is_busy = True
    elevator.save()
    print("Doors are Closed")