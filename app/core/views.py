from django.shortcuts import render
from rest_framework.views import APIView,status,Response
from .models import CustomUser,Task
from .serializers import UserSerializer,TaskSerializer,UpdateStatus
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

class RegisterView(APIView):
    queryset = CustomUser
    serializer_class = UserSerializer

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
class TaskView(APIView):
    authentication_classes = [JWTAuthentication]    
    permission_classes = [IsAuthenticated]
    queryset = Task
    serializer_class = TaskSerializer

    def get(self,request):
        model = Task.objects.filter(owner=request.user)
        serializer = TaskSerializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        try:
            instance = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    
        serializer = UpdateStatus(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            instance=Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)   
        instance.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
    

from rest_framework.decorators import api_view

@api_view(['GET'])
def get_true_status(request):
    instance=Task.objects.filter(status=True)
    serializer=TaskSerializer(instance,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_false_status(request):
    instance=Task.objects.filter(status=False)
    serializer=TaskSerializer(instance,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)