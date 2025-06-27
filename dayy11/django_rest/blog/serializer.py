from rest_framework import serializers
from .models import *
class StudentsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Students
        fields = ['name','age']
        # exclude = ['father_name']
        # fields = "__all__"