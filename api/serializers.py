from rest_framework import serializers
from .models import ServiceText,ServiceBox,ProjectBox,Profile,ContactUs,AboutUs,OurMission,ChooseUs

class ServiceTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceText
        fields = '__all__'

class ServiceBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceBox
        fields = '__all__'
    
class ProjectBoxSerializer(serializers.ModelSerializer):
    class Meta :
        model = ProjectBox
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta :
        model = Profile
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta :
        model = ContactUs
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta :
        model = AboutUs
        fields = '__all__'

class OurMissionSerializer(serializers.ModelSerializer):
    class Meta :
        model = OurMission
        fields = '__all__'

class ChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUs
        fields = '__all__'
