from django.db import models
import uuid


# Create your models here.
class ServiceText(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_text_en = models.TextField()
    service_text_mm = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    
class ServiceBox(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable=False)
    icon = models.ImageField(upload_to ="servicebox/")
    title_en = models.CharField(max_length=50)
    title_mm = models.CharField(max_length=50)
    des_en = models.TextField()
    des_mm = models.TextField()
    service_list_en = models.JSONField(default=list)
    service_list_mm = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title_en)
    
class ProjectBox(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    project_num = models.IntegerField()
    project_title = models.CharField(max_length=50)
    project_des = models.TextField()
    project_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.project_title)
    
class Profile(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    profile_title = models.CharField(max_length=255)
    profile_des  = models.TextField()
    image = models.ImageField(upload_to="profile/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.profile_title)
    
class ContactUs(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)




    
