from .models import Elevator, Request
from django.db.models import F

# this function is deciding which elevator to call 
def decide_elevator(floor,elevator_system):
    elevator = Elevator.objects.filter(elevator_system = elevator_system,is_operational = True).order_by(F('current_floor')-floor)
    # print(elevator[0].elevator_system.name)
    return elevator[0]

def move_elevator(elevator_id,next_floor):
    elevator = Elevator.objects.get(id=elevator_id)
    # requests = Request.objects.filter(elevator=elevator,is_complete=False)
  
    if next_floor > elevator.current_floor:
        elevator.direction = 'up'
        elevator.is_busy = True
    elif next_floor < elevator.current_floor:
        elevator.direction = 'down'
        elevator.is_busy = True
    else:
        elevator.direction = 'stopped'
        elevator.is_busy = False

    elevator.current_floor = next_floor
    elevator.save()
    return elevator.direction


def open_door(elevator_id):
    elevator = Elevator.objects.get(id=elevator_id)
    requests = Request.objects.filter(elevator=elevator,is_complete=False)
    # next_floor = requests[0].floor
    # elevator.current_floor = next_floor
    elevator.is_open = True
    elevator.is_busy = False
    elevator.save()

def close_door(elevator_id):
    elevator = Elevator.objects.get(id=elevator_id)
    requests = Request.objects.filter(elevator=elevator,is_complete=False)
    # destination = requests[0].destination_floor
    # elevator.current_floor = destination
    elevator.is_open = False
    elevator.is_busy = True
    elevator.save()
