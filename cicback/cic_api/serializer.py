# serializer.py сonvert python object to another format

from rest_framework import serializers
from .models import ArrayModel

class ArrayModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = ArrayModel
        fields = ['Id', 'Value']