# Dùng để validate dữ liệu

from rest_framework import serializers
from .models import User, Traveller, Member
from datetime import datetime
from django.http import HttpResponse

class UserSerialize(serializers.Serializer):
  name = serializers.CharField(max_length=20)
  # Trong Serialize chỉ có IntegerField
  # required=Falsed: cho phép Optional
  age = serializers.IntegerField(required=False)
  salary = serializers.IntegerField()
  hometown = serializers.CharField(max_length=20)

  def validate_age(self, value): #tên hàm phải có dạng validate+tên_field
    # Handle validate age of user
    if value < 18 or value > 60:
      raise serializers.ValidationError("Age must be between 18 and 60!")

    return value
  
  def validate(self, data): #validate cho tất cả field trong class
    # Validate salary => data['salary']
    if data['salary'] < data['age']:
      raise serializers.ValidationError("salary: You have to try harder!")

    return data
  
  def create(self, validated_data):
    return User.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    instance.age = validated_data.get('age', instance.age)
    instance.salary = validated_data.get('salary', instance.salary)
    instance.hometown = validated_data.get('hometown', instance.hometown)
    instance.save()
    return instance
class TravellerSerialize(serializers.ModelSerializer):
#   mem_no = serializers.IntegerField()
#   apl_no = serializers.IntegerField()
  class Meta: 
    model = Traveller
    exclude = ['traveller_no']

# def validate(self, data):
#     #validate data type
#     if data['mem_no'] > 5:
#       raise serializers.ValidationError("number is too low")

#     return data
# def validate_traveller_no(self, value): #tên hàm phải có dạng validate+tên_field
#     # Handle validate traveller_no

#     return value
# def validate_mem_no(self, value):
#         # Check if the mem_no already exists in the database
#         if not Member.objects.filter(mem_no=value).exist():
#             raise serializers.ValidationError("This member number does not exist")
#         return value 
  
def create(self, validated_data):
    return Traveller.objects.create(**validated_data)
