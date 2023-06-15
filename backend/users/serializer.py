from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate, get_user_model
from django.http.response import Http404

# serialize model admin
class AdminSerialiser(serializers.ModelSerializer):
    class Meta:   
        model = Admin
        fields = '__all__'
# serialize model Student
class StudentSerialiser(serializers.ModelSerializer):
    user = AdminSerialiser()
    class Meta:   
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = Admin.objects.create(**user_data)
        Student = Student.objects.create(user=user, **validated_data)

        return Student


    
# serialize model lecturer
class LecturerSerialiser(serializers.ModelSerializer):
    user = AdminSerialiser()
    class Meta:   
        model = Lecturer
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = Admin.objects.create(**user_data)
        lecturer = Lecturer.objects.create(user=user, **validated_data)

        return lecturer
    

# user login serializer
class UserLoginSerialiser(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):

        user = authenticate(username=clean_data['email'], password=clean_data['password'])

        if not user:
            raise Http404

        return user