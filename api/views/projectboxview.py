from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import ProjectBox
from ..serializers import ProjectBoxSerializer

@api_view(['GET'])
def project_box_list(request):
    service_text = ProjectBox.objects.all()
    serializer = ProjectBoxSerializer(service_text, many=True)
    return Response(
        {
            "Success": True,
            "message": "Project Box List Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

      
@api_view(['POST'])
def project_box_create(request):
    serializer = ProjectBoxSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "Project Box Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    
    return Response(
        { 
            "Success": False,
            "message": "Project Box Creation Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def project_box_detail(request, pk):
    try:
        service_text = ProjectBox.objects.get(pk=pk)
    except ProjectBox.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "Project Box Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProjectBoxSerializer(service_text)
    return Response(
        {
            "Success": True,
            "message": "Project Box Retrieved Successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['PUT', 'PATCH'])
def project_box_update(request, pk):
    try:
        service_text = ProjectBox.objects.get(pk=pk)
    except ProjectBox.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "Project Box Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProjectBoxSerializer(service_text, data=request.data, partial=(request.method == 'PATCH'))
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "Success": True,
                "message": "Project Box Updated Successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
    
    return Response(
        {
            "Success": False,
            "message": "Project Box Update Failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def project_box_delete(request, pk):
    try:
        service_text = ProjectBox.objects.get(pk=pk)
    except ProjectBox.DoesNotExist:
        return Response(
            {
                "Success": False,
                "message": "Project Box Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    service_text.delete()
    return Response(
        {
            "Success": True,
            "message": "Project Box Deleted Successfully"
        }, status=status.HTTP_204_NO_CONTENT)

