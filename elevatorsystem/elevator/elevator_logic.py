from .models import Elevator, Request
from django.db.models import F, Value, IntegerField, Case, When
from django.db.models.functions import Abs

# this function is deciding which elevator to call 
def decide_elevator(floor,elevator_system):
    print("hii")
    elevator = Elevator.objects.filter(elevator_system=elevator_system, is_operational=True).annotate(near=Abs(F('current_floor') - floor)).order_by('near')

    # elevator = Elevator.objects.filter(elevator_system=elevator_system,is_operational=True).annotate(near=Case(When(current_floor__gte=F('floor'), then=F('current_floor') - F('floor')),When(current_floor__lt=F('floor'), then=F('floor') - F('current_floor')),output_field=IntegerField())).order_by('-near')

    print(elevator[0].current_floor)
    for i in elevator:
        print(i.elevator_id," ",i.current_floor," ",i.near)
    # print("hear")
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
