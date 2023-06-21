from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status 
from .models import Elevator, Request,ElevatorSystem
from .serializers import ElevatorSerializer, RequestSerializer,ElevatorSystemSerializer
from .elevator_logic import move_elevator, open_door, close_door,decide_elevator

class ElevatorSystemIn(viewsets.ModelViewSet):
    queryset = ElevatorSystem.objects.all()
    serializer_class = ElevatorSystemSerializer
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            el_sys = serializer.save()
            for el in range(1,el_sys.no_of_elevators+1):
                direction = "stopped"
                elevator = Elevator(elevator_system=el_sys,direction=direction,elevator_id=el)
                print(elevator)
                elevator.save()
            return Response({"message":"Elevator System Set up Successfully!!"},status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=True, methods=['post'])
    def move(self, request, pk=None):
        elevator = self.get_object()
        move_elevator(elevator.id)
        return Response({'message': 'Elevator movement triggered.'})

    @action(detail=True, methods=['post'])
    def open(self, request, pk=None):
        elevator = self.get_object()
        open_door(elevator.id)
        return Response({'message': 'Elevator door opened'})

    @action(detail=True, methods=['post'])
    def close(self, request, pk=None):
        elevator = self.get_object()
        close_door(elevator.id)
        return Response({'message': 'Elevator door closed'})


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    @action(detail = False, methods = ['post'])
    def decide(self,request):
        floor = request.data["floor"]
        name = request.data["name"]
        try:
            elevator_system = ElevatorSystem.objects.get(name = name)
            elevator = decide_elevator(floor,elevator_system)
            new_request = Request(floor = floor,elevator = elevator)
            new_request.save()
        except:
            return Response({"message":"Wrong Inputs..."},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Elevator {} is coming...".format(elevator),"elevator":elevator.id},status=status.HTTP_202_ACCEPTED)
