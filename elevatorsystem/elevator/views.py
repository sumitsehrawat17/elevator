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
        if not elevator.is_operational:
            return Response({"message": "This elevator is under maintenance!!"},status=status.HTTP_200_OK)
        destination = request.data["destination"]
        req = request.data["request"]
        request = Request.objects.get(id = req)
        request.destination_floor = destination
        request.is_complete = True
        request.save()
        direction = move_elevator(pk,destination)
        return Response({'message': 'Elevator movement is in {} direction'.format(direction)})
    @action(detail = True, methods=['post'])
    def Operational(self,request,pk=None):
        op = request.data["operational"]
        elevator = Elevator.objects.get(id = pk)
        elevator.is_operational = op
        elevator.save()
        return Response({"message" : "This elevator is not operational"},status=status.HTTP_200_OK)
    
    @action(detail = True ,methods=["get"])
    def ElevatorRequests(self,request,pk=None):
        elevator = Elevator.objects.get(id = pk)
        requests = Request.objects.filter(elevator = elevator)
        serializer = RequestSerializer(requests,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)


    @action(detail=True, methods=['get'])
    def OpenDoor(self, request, pk=None):
        elevator = self.get_object()
        open_door(elevator.id)
        return Response({'message': 'Elevator door opened'})

    @action(detail=True, methods=['get'])
    def CloseDoor(self, request, pk=None):
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
            elevator.current_floor = floor
            elevator.save()
            new_request = Request(floor = floor,elevator = elevator)
            new_request.save()
        except:
            return Response({"message":"Wrong Inputs..."},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Elevator {} is coming...".format(elevator),"elevator":elevator.id,"request" : new_request.id},status=status.HTTP_202_ACCEPTED)
