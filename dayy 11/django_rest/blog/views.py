from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *

@api_view(["GET"])
def home(request):
    students_obj = Students.objects.all()
    serializer = StudentsSerializer(students_obj,many = True)
    return Response({'status':200,'paylaod':serializer.data})

@api_view(["POST"])
def post_students(request):
    data = request.data
    print(data)
    serializer = StudentsSerializer(data = request.data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({"status" : 403 ,"errors": serializer.error, "message" : "Something went wrong"})
    serializer.save()
    return Response({'status' : 200, 'payload' : serializer.data , "message" : "your data is saved"})





