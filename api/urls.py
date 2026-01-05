from django.urls import path
from .views import (
    servicetextview,serviceboxview,projectboxview,profileview,contactusview,aboutusview,ourmissionview,chooseusview
)

urlpatterns = [

    # Service Text URLs
    path('servicetexts/', servicetextview.service_text_list, name='service_text_list'),
    path('servicetexts/create/', servicetextview.service_text_create, name='service_text_create'),
    path('servicetexts/<uuid:pk>/', servicetextview.service_text_detail, name='service_text_detail'),
    path('servicetexts/<uuid:pk>/update/', servicetextview.service_text_update, name='service_text_update'),
    path('servicetexts/<uuid:pk>/delete/', servicetextview.service_text_delete, name='service_text_delete'),

    # Service Box URLS
    path('servicebox/',serviceboxview.service_box_list,name='service_box_list'),
    path('servicebox/create/',serviceboxview.service_box_create,name='service_box_create'),
    path('servicebox/<uuid:pk>/',serviceboxview.service_box_detail,name='service_box_detail'),
    path('servicebox/<uuid:pk>/update',serviceboxview.service_box_update,name='service_box_update'),
    path('servicebox/<uuid:pk>/delete',serviceboxview.service_box_delete,name='service_box_delete'),

    # Project Box URLs
    path('projectbox/',projectboxview.project_box_list,name='project_box_list'),
    path('projectbox/create/',projectboxview.project_box_create,name="project_box_create"),
    path('projectbox/<uuid:pk>/',projectboxview.project_box_detail,name='project_box_detail'),
    path('projectbox/<uuid:pk>/update/',projectboxview.project_box_update,name='project_box_update'),
    path('projectbox/<uuid:pk>/delete/',projectboxview.project_box_delete,name='project_box_delete'),

    # Profile URLs
    path('profile/',profileview.profile_list,name='profile_list'),
    path('profile/create/',profileview.profile_create,name='profile_create'),
    path('profile/<uuid:pk>/',profileview.profile_detail,name='profile_detail'),
    path('profile/<uuid:pk>/update/',profileview.profile_update,name='profile_update'),
    path('profile/<uuid:pk>/delete/',profileview.profile_delete,name='profile_delete'),

    #ContactUs URLs
    path('contactus/',contactusview.contactus_list,name='contactus_list'),
    path('contactus/create/',contactusview.contactus_create,name='contactus_create'),
    path('contactus/<uuid:pk>/',contactusview.contactus_detail,name='contactus_detail'),
    path('contactus/<uuid:pk>/update/',contactusview.contactus_update,name='contactus_update'),
    path('contactus/<uuid:pk>/delete/',contactusview.contactus_delete,name='contactus_delete'),

    # AboutUs URLs 
    path('aboutus/',aboutusview.aboutus_list,name='aboutus_list'),
    path('aboutus/create/',aboutusview.aboutus_create,name='aboutus_create'),
    path('aboutus/<uuid:pk>/',aboutusview.aboutus_detail,name='aboutus_detail'),
    path('aboutus/<uuid:pk>/update/',aboutusview.aboutus_update,name='aboutus_update'),
    path('aboutus/<uuid:pk>/delete/',aboutusview.aboutus_delete,name='aboutus_delete'),

    # OurMission URLs 
    path('mission/',ourmissionview.mission_list,name='mission_list'),
    path('mission/create/',ourmissionview.mission_create,name='mission_create'),
    path('mission/<uuid:pk>/',ourmissionview.mission_detail,name='mission_detail'),
    path('mission/<uuid:pk>/update/',ourmissionview.mission_update,name='mission_update'),
    path('mission/<uuid:pk>/delete/',ourmissionview.mission_delete,name='mission_delete'),

    # ChooseUs URLs 
    path('chooseus/',chooseusview.chooseus_list,name='chooseus_list'),
    path('chooseus/create/',chooseusview.chooseus_create,name='chooseus_create'),
    path('chooseus/<uuid:pk>/',chooseusview.chooseus_detail,name='chooseus_detail'),
    path('chooseus/<uuid:pk>/update/',chooseusview.chooseus_update,name='chooseus_update'),
    path('chooseus/<uuid:pk>/delete/',chooseusview.chooseus_delete,name='chooseus_delete'),

    



  
]
