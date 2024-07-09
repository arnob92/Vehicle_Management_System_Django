"""
URL configuration for vms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from.import views,Office_views, Driver_views, Teacher_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE , name='base'),

    #login_path
    path('', views.LOGIN, name="login"),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),


    #profile Update
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),

    #this is office panel
    path('office/home',Office_views.HOME, name='office_home'),

    path('office/teacher/add',Office_views.ADD_TEACHER,name='add_teacher'),
    path('office/teacher/views',Office_views.VIEW_TEACHER,name='view_teacher'),
    path('office/teacher/edit/<str:id>',Office_views.EDIT_TEACHER,name='edit_teacher'),
    path('office/teacher/update',Office_views.UPDATE_TEACHER,name='update_teacher'),
    path('office/teacher/delete/<str:admin>',Office_views.DELETE_TEACHER,name='delete_teacher'),

    path('office/driver/add',Office_views.ADD_DRIVER,name='add_driver'),
    path('office/driver/view',Office_views.VIEW_DRIVER,name='view_driver'),
    path('office/driver/edit/<str:id>', Office_views.EDIT_DRIVER, name='edit_driver'),
    path('office/driver/update', Office_views.UPDATE_DRIVER, name='update_driver'),
    path('office/driver/delete/<str:admin>',Office_views.DELETE_DRIVER,name='delete_driver'),


    path('office/vehicle/add',Office_views.ADD_VEHICLE,name='add_vehicle'),
    path('office/vehicle/view', Office_views.VIEW_VEHICLE, name='view_vehicle'),
    path('office/vehicle/edit/<str:id>', Office_views.EDIT_VEHICLE, name='edit_vehicle'),
    path('office/vehicle/update', Office_views.UPDATE_VEHICLE, name='update_vehicle'),
    path('office/vehicle/delete/<str:id>', Office_views.DELETE_VEHICLE, name='delete_vehicle'),


    path('office/vehicle/schedule/add',Office_views.ADD_SCHEDULE,name='add_schedule'),
    path('office/vehicle/schedule/add_other',Office_views.ADD_SCHEDULE_OTHER,name='add_schedule_other'),
    path('office/vehicle/schedule/view',Office_views.VIEW_SCHEDULE,name='view_schedule'),
    path('office/vehicle/schedule/view_complete', Office_views.VIEW_COMPLETE_SCHEDULE, name='view_complete_schedule'),
    path('office/vehicle/schedule/delete/<str:id>', Office_views.DELETE_SCHEDULE, name='delete_schedule'),
    path('office/vehicle/schedule/complete/<str:id>', Office_views.COMPLETE_SCHEDULE, name='complete_schedule'),


    path('office/department/add',Office_views.ADD_DEPARTMENT,name='add_department'),
    path('office/department/view', Office_views.VIEW_DEPARTMENT, name='view_department'),
    path('office/department/edit/<str:id>', Office_views.EDIT_DEPARTMENT, name='edit_department'),
    path('office/department/update', Office_views.UPDATE_DEPARTMENT, name='update_department'),
    path('office/department/delete/<str:id>', Office_views.DELETE_DEPARTMENT, name='delete_department'),

    path('office/teacher/requisition_view',Office_views.REQUISITION_VIEW,name='requisition_view'),
    path('office/teacher/approve_requisition/<str:id>',Office_views.TEACHER_APPROVE_REQUISITION,name='teacher_approve_requisition'),
    path('office/teacher/disapprove_requisition/<str:id>', Office_views.TEACHER_DISAPPROVE_REQUISITION,name='teacher_disapprove_requisition'),
    path('office/teacher/approve_requisition_save', Office_views.TEACHER_APPROVE_REQUISITION_SAVE,name='teacher_approve_requisition_save'),





    #Teacher panel
    path('teacher/home', Teacher_views.HOME, name='teacher_home'),
    path('teacher/vehicle/view', Teacher_views.TEACHER_VIEW_VEHICLE, name='teacher_view_vehicle'),
    path('teacher/apply_requisition',Teacher_views.TEACHER_APPLY_REQUISITION,name='teacher_apply_requisition'),
    path('teacher/apply_requisition_save',Teacher_views.TEACHER_APPLY_REQUISITION_SAVE,name='teacher_apply_requisition_save'),
    path('teacher/requisition_cancel/<str:id>',Teacher_views.REQUISITION_CANCEL,name='requisition_cancel'),


    path('driver/home',Driver_views.HOME,name='driver_home'),
    path('driver/view_schedule',Driver_views.VIEW_SCHEDULE,name='driver_view_schedule'),
    path('driver/view_schedule/delete/<str:id>',Driver_views.DRIVER_DELETE_SCHEDULE,name='driver_delete_schedule'),
    path('driver/view_schedule/complete/<str:id>',Driver_views.DRIVER_COMPLETE_SCHEDULE,name='driver_complete_schedule'),
    path('driver/view_complete_schedule', Driver_views.VIEW_COMPLETE_SCHEDULE, name='driver_view_complete_schedule'),
    path('driver/vehicle/view',Driver_views.DRIVER_VIEW_VEHICLE,name='driver_view_vehicle'),



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
