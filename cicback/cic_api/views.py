from rest_framework.views import View
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view

from .models import ArrayModel, SortModel
from .serializer import ArrayModelSerialize, SortSerialize

from .sort_methods import bubble_sort, insertion_sort

# functional approach
@api_view(['GET'])
def getArr(request):
    if request.method == 'GET':
        output = ArrayModel.objects.all()
        serialize = ArrayModelSerialize(output, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def postArr(request):
    if request.method == 'POST':
        serialize = ArrayModelSerialize(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def bubbleSort(request):
    if(request.method == 'GET'):
        arrayData = ArrayModel.objects.all()
        
        # Make array values
        value = [getVal.Value for getVal in arrayData]
        
        # Use our sort methods, and get value array, operations, finalTime
        arr, operations, final_time = bubble_sort(value)

        # find object or create if not fund current object
        output, created = SortModel.objects.get_or_create(Name='BubbleSort', defaults={'Tact': 0, 'TimeComplete': 0})

        # set our variable for this object and save on DB                
        output.Tact = operations
        output.TimeComplete = final_time
        output.save()
        
        # to convert Django model objects or QuerySet queries into structured data 
        # that can be easily transferred over the network 
        serial = SortSerialize(output)
        
        return Response({"SortedArray": arr, "Operations": operations, "SortTime": final_time, "Data":serial.data}, status=status.HTTP_200_OK)
            
@api_view(['GET'])
def insertionSort(request):
    if(request.method == 'GET'):
        arrayData = ArrayModel.objects.all()
        
        # Make array values
        value = [getVal.Value for getVal in arrayData]
        
        # Use our sort methods, and get value array, operations, finalTime
        arr, operations, final_time = insertion_sort(value)

        # find object or create if not fund current object
        output, created = SortModel.objects.get_or_create(Name='InsertionSort', defaults={'Tact': 0, 'TimeComplete': 0})

        # set our variable for this object and save on DB                
        output.Tact = operations
        output.TimeComplete = final_time
        output.save()
        
        # to convert Django model objects or QuerySet queries into structured data 
        # that can be easily transferred over the network 
        serial = SortSerialize(output)
        
        return Response({"SortedArray": arr, "Operations": operations, "SortTime": final_time, "Data":serial.data}, status=status.HTTP_200_OK)
            


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
        