from rest_framework import serializers
from .models import User

class UserSerialize(serializers.Serializer):
  name = serializers.CharField(max_length=20, required=False)
  age = serializers.IntegerField(required=False)
  salary = serializers.IntegerField()
  hometown = serializers.CharField(max_length=20)

  def validate_age(self, value):
    # Handle validate age of user
    if value < 18 or value > 60:
      raise serializers.ValidationError("Age must be between 18 and 60!")

    return value

  def validate(self, data):
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

