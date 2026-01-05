from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import OurMission
from ..serializers import OurMissionSerializer

@api_view(['GET'])
def mission_list(request):
    service_text = OurMission.objects.all()
    serializer = OurMissionSerializer(service_text, many=True)
    return Response(
        {
            "Success": True,
            "message": "OurMission List Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

      
@api_view(['POST'])
def mission_create(request):
    serializer = OurMissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "OurMission Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    
    return Response(
        { 
            "Success": False,
            "message": "OurMission Creation Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def mission_detail(request, pk):
    try:
        service_text = OurMission.objects.get(pk=pk)
    except OurMission.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "OurMission Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = OurMissionSerializer(service_text)
    return Response(
        {
            "Success": True,
            "message": "OurMission Retrieved Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['PUT', 'PATCH'])
def mission_update(request, pk):
    try:
        service_text = OurMission.objects.get(pk=pk)
    except OurMission.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "OurMission Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = OurMissionSerializer(service_text, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "OurMission Updated Successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    
    return Response(
        {
            "Success": False,
            "message": "OurMission Update Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def mission_delete(request, pk):
    try:
        service_text = OurMission.objects.get(pk=pk)
    except OurMission.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "OurMission Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    service_text.delete()
    return Response(
        {
            "Success": True,
            "message": "OurMission Deleted Successfully"
        }, status=status.HTTP_204_NO_CONTENT)

