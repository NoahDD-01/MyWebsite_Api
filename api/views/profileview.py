from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Profile
from ..serializers import ProfileSerializer

@api_view(['GET'])
def profile_list(request):
    service_text = Profile.objects.all()
    serializer = ProfileSerializer(service_text, many=True)
    return Response(
        {
            "Success": True,
            "message": "Profile List Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

      
@api_view(['POST'])
def profile_create(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "Profile Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    
    return Response(
        { 
            "Success": False,
            "message": "Profile Creation Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def profile_detail(request, pk):
    try:
        service_text = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "Profile Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProfileSerializer(service_text)
    return Response(
        {
            "Success": True,
            "message": "Profile Retrieved Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['PUT', 'PATCH'])
def profile_update(request, pk):
    try:
        service_text = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "Profile Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProfileSerializer(service_text, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "Profile Updated Successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    
    return Response(
        {
            "Success": False,
            "message": "Profile Update Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def profile_delete(request, pk):
    try:
        service_text = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "Profile Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    service_text.delete()
    return Response(
        {
            "Success": True,
            "message": "Profile Deleted Successfully"
        }, status=status.HTTP_204_NO_CONTENT)

