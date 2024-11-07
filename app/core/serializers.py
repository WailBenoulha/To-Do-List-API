from rest_framework import serializers
from .models import CustomUser,Task
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)    
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title','description','status')  

class UpdateStatus(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields = ('id','title','description','status')   
        extra_kwargs = {
            'title':{'read_only':True},
            'description':{'read_only':True},
        }       