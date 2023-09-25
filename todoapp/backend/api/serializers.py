from rest_framework import serializers
from todo.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
  created = serializers.ReadOnlyField()
  completed = serializers.ReadOnlyField()

  class Meta:
    model = ToDo
    fields = ['id', 'title', 'memo', 'created', 'completed']

class ToDoToggleCompleteSerializer(serializers.ModelSerializer):
  completed = serializers.BooleanField()

  class Meta:
    model = ToDo
    fields = ['completed']

  def update(self, instance, validated_data):
    instance.completed = validated_data['completed']
    instance.save()
    return instance
