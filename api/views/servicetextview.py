from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..models import ServiceText
from ..serializers import ServiceTextSerializer

# Create your views here.
@api_view(['GET'])
def service_text_list(request):
    service_text = ServiceText.objects.all()
    serializer = ServiceTextSerializer(service_text, many=True)
    return Response(
        {
            "Success": True,
            "message": "Service Texts List Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

      
@api_view(['POST'])
def service_text_create(request):
    serializer = ServiceTextSerializer(data=request.data)
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
def service_text_detail(request, pk):
    try:
        service_text = ServiceText.objects.get(pk=pk)
    except ServiceText.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "Service Text Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ServiceTextSerializer(service_text)
    return Response(
        {
            "Success": True,
            "message": "Service Text Retrieved Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['PUT', 'PATCH'])
def service_text_update(request, pk):
    try:
        service_text = ServiceText.objects.get(pk=pk)
    except ServiceText.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "Service Text Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ServiceTextSerializer(service_text, data=request.data, partial=(request.method == 'PATCH'))
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
def service_text_delete(request, pk):
    try:
        service_text = ServiceText.objects.get(pk=pk)
    except ServiceText.DoesNotExist:
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
