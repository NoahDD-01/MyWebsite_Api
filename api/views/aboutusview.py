from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import AboutUs
from ..serializers import AboutUsSerializer

@api_view(['GET'])
def aboutus_list(request):
    service_text =AboutUs.objects.all()
    serializer =AboutUsSerializer(service_text, many=True)
    return Response(
        {
            "Success": True,
            "message": "AboutUs List Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

      
@api_view(['POST'])
def aboutus_create(request):
    serializer = AboutUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "AboutUs Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    
    return Response(
        { 
            "Success": False,
            "message": "AboutUs Creation Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def aboutus_detail(request, pk):
    try:
        service_text = AboutUs.objects.get(pk=pk)
    except AboutUs.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "AboutUs Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AboutUsSerializer(service_text)
    return Response(
        {
            "Success": True,
            "message": "AboutUs Retrieved Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['PUT', 'PATCH'])
def aboutus_update(request, pk):
    try:
        service_text = AboutUsSerializer.objects.get(pk=pk)
    except AboutUsSerializer.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "AboutUsSerializer Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AboutUsSerializer(service_text, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "AboutUsSerializer Updated Successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    
    return Response(
        {
            "Success": False,
            "message": "AboutUsSerializer Update Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def aboutus_delete(request, pk):
    try:
        service_text = AboutUs.objects.get(pk=pk)
    except AboutUs.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "AboutUs Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    service_text.delete()
    return Response(
        {
            "Success": True,
            "message": "AboutUs Deleted Successfully"
        }, status=status.HTTP_204_NO_CONTENT)

