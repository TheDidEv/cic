# serializer.py сonvert python object to another format

from rest_framework import serializers
from .models import ArrayModel, SortModel

class ArrayModelSerialize(serializers.ModelSerializer):
    class Meta:
        model = ArrayModel
        fields = '__all__'
        
class SortSerialize(serializers.ModelSerializer):
    class Meta:
        model = SortModel
        fields = ['Id', 'Name', 'Tact', 'TimeComplete']