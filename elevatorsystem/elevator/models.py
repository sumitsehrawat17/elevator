from django.db import models

# Create your models here.
# This model is for storing the elevator-system info
class ElevatorSystem(models.Model):
    name = models.CharField(max_length=50,unique=True)
    no_of_elevators = models.BigIntegerField()

class Elevator(models.Model):
    elevator_system = models.ForeignKey(ElevatorSystem,on_delete=models.CASCADE)
    is_operational = models.BooleanField(default=True) # True means it can be utilised and False means it is under maintaince
    is_busy = models.BooleanField(default=False) # True means elevator is in moving and False means it is available 
    current_floor = models.IntegerField(default=1)
    is_open = models.BooleanField(default=False)# True means elevator doors are open and False means they are closed 
    direction = models.CharField(max_length=10, choices=[('up', 'Up'), ('down', 'Down'), ('stopped', 'Stopped')])

class Request(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor = models.IntegerField()  # it is the floor no.(point) from which request is made 
    created_at = models.DateTimeField(auto_now=True)
    destination_floor = models.IntegerField() # it is the destination on which user wants to go
    is_complete = models.BooleanField(default=False)# False means the request is not completed and True means request is done 





