from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import ChooseUs
from ..serializers import ChooseUsSerializer

@api_view(['GET'])
def chooseus_list(request):
    service_text = ChooseUs.objects.all()
    serializer = ChooseUsSerializer(service_text, many=True)
    return Response(
        {
            "Success": True,
            "message": "ChooseUs List Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

      
@api_view(['POST'])
def chooseus_create(request):
    serializer = ChooseUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "ChooseUs Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    
    return Response(
        { 
            "Success": False,
            "message": "ChooseUs Creation Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def chooseus_detail(request, pk):
    try:
        service_text = ChooseUs.objects.get(pk=pk)
    except ChooseUs.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "ChooseUs Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ChooseUsSerializer(service_text)
    return Response(
        {
            "Success": True,
            "message": "ChooseUs Retrieved Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['PUT', 'PATCH'])
def chooseus_update(request, pk):
    try:
        service_text = ChooseUs.objects.get(pk=pk)
    except ChooseUs.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "ChooseUs Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ChooseUsSerializer(service_text, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "ChooseUs Updated Successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    
    return Response(
        {
            "Success": False,
            "message": "ChooseUs Update Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def chooseus_delete(request, pk):
    try:
        service_text = ChooseUs.objects.get(pk=pk)
    except ChooseUs.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "ChooseUs Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    service_text.delete()
    return Response(
        {
            "Success": True,
            "message": "ChooseUs Deleted Successfully"
        }, status=status.HTTP_204_NO_CONTENT)

