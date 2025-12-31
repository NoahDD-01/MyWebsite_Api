from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..models import ServiceBox
from ..serializers import ServiceBoxSerializer

# Create your views here.
@api_view(['GET'])
def service_box_list(request):
    service_text = ServiceBox.objects.all()
    serializer = ServiceBoxSerializer(service_text, many=True)
    return Response(
        {
            "Success": True,
            "message": "Service Texts List Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

      
@api_view(['POST'])
def service_box_create(request):
    serializer = ServiceBoxSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "Service Text Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    
    return Response(
        { 
            "Success": False,
            "message": "Service Text Creation Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def service_box_detail(request, pk):
    try:
        service_text = ServiceBox.objects.get(pk=pk)
    except ServiceBox.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "Service Text Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ServiceBoxSerializer(service_text)
    return Response(
        {
            "Success": True,
            "message": "Service Text Retrieved Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['PUT', 'PATCH'])
def service_box_update(request, pk):
    try:
        service_text = ServiceBox.objects.get(pk=pk)
    except ServiceBox.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "Service Text Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ServiceBoxSerializer(service_text, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "Service Text Updated Successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    
    return Response(
        {
            "Success": False,
            "message": "Service Text Update Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def service_box_delete(request, pk):
    try:
        service_text = ServiceBox.objects.get(pk=pk)
    except ServiceBox.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "Service Text Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    service_text.delete()
    return Response(
        {
            "Success": True,
            "message": "Service Text Deleted Successfully"
        }, status=status.HTTP_204_NO_CONTENT)



    