# Dùng để validate dữ liệu

from rest_framework import serializers
from .models import User

# class UserSerialize(serializers.Serializer):
class UserSerialize(serializers.ModelSerializer):
  # name = serializers.CharField(max_length=20)
  # # Trong Serialize chỉ có IntegerField
  # # required=Falsed: cho phép Optional
  # age = serializers.IntegerField(required=False)
  # salary = serializers.IntegerField()
  # hometown = serializers.CharField(max_length=20)
  foo = serializers.SerializerMethodField()
  custom_field = serializers.ReadOnlyField()
  rank_name = serializers.ReadOnlyField()

  class Meta:
    model = User
    fields = '__all__'
    # read_only_fields = (
    #   'custom_field',
    # )
    # fields = ['salary', 'hometown']
    # exclude = ['name']

  # def validate_name(self, value): #tên hàm phải có dạng validate+tên_field
  #   # Handle validate age of user
  #   user = User.objects.filter(name=value)
  #   if user:
  #     raise serializers.ValidationError("User already exists!")

  #   return value

  def get_foo(self, obj):
    return "Foo id: " + obj.pk

  def validate_age(self, value): #tên hàm phải có dạng validate+tên_field
    # Handle validate age of user
    if value < 18 or value > 60:
      raise serializers.ValidationError("Age must be between 18 and 60!")

    return value
  
  def validate(self, data): #validate cho tất cả field trong class
    # Validate salary => data['salary']

    print("data", data)

    # if data['salary'] < data['age']:
    #   raise serializers.ValidationError("salary: You have to try harder!")

    return data
  
  def create(self, validated_data):
    return User.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    instance.age = validated_data.get('age', instance.age)
    instance.salary = validated_data.get('salary', instance.salary)
    instance.hometown = validated_data.get('hometown', instance.hometown)
    instance.save()
    return instance

