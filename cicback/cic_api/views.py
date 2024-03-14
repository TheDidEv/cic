from django.shortcuts import render

# make import
from rest_framework.views import View
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

from .models import ArrayModel
from .serializer import ArrayModelSerialize

# functional approach
@api_view(['GET'])
def getArr(request):
    if request.method == 'GET':
        output = ArrayModel.objects.all()
        serialize = ArrayModelSerialize(output, many = True)
        return Response(serialize.data, status=status.HTTP_200_OK)
    else:
        return Response({error:"error"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def postArr(request):
    if request.method == 'POST':
        serialize = ArrayModelSerialize(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response({error:"error"}, status=status.HTTP_400_BAD_REQUEST)
            

# class-basic approach
# class ArrayView(View):

#     def get(self, request):
#         output = ArrayModel.objects.all()
#         serialize = ArrayModelSerialize(output, many = True)
#         return Response(serialize.data)
    
#     def post(self, request):
#         serialize = ArrayModelSerialize(data = request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serialize.errors, status = status.HTTP_400_BAD_REQUEST)
        