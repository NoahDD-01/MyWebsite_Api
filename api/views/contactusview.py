from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import ContactUs
from ..serializers import ContactUsSerializer

@api_view(['GET'])
def contactus_list(request):
    service_text = ContactUs.objects.all()
    serializer = ContactUsSerializer(service_text, many=True)
    return Response(
        {
            "Success": True,
            "message": "ContactUs List Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

      
@api_view(['POST'])
def contactus_create(request):
    serializer = ContactUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "ContactUs Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    
    return Response(
        { 
            "Success": False,
            "message": "ContactUs Creation Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def contactus_detail(request, pk):
    try:
        service_text = ContactUs.objects.get(pk=pk)
    except ContactUs.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "ContactUs Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ContactUsSerializer(service_text)
    return Response(
        {
            "Success": True,
            "message": "ContactUs Retrieved Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['PUT', 'PATCH'])
def contactus_update(request, pk):
    try:
        service_text = ContactUs.objects.get(pk=pk)
    except ContactUs.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "ContactUs Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ContactUsSerializer(service_text, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "ContactUs Updated Successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    
    return Response(
        {
            "Success": False,
            "message": "ContactUs Update Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def contactus_delete(request, pk):
    try:
        service_text = ContactUs.objects.get(pk=pk)
    except ContactUs.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "ContactUs Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    service_text.delete()
    return Response(
        {
            "Success": True,
            "message": "ContactUs Deleted Successfully"
        }, status=status.HTTP_204_NO_CONTENT)

