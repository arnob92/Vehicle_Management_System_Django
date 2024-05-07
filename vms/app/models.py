from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1, 'OFFICE'),
        (2, 'TEACHERS'),
        (3, 'DRIVER'),
    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')


class Department(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    designation = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class Driver(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    licence_number = models.CharField(max_length=100)
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    status_choices = (
        ('Resting', 'Resting'),
        ('Scheduled', 'Scheduled'),
        ('Traveling', 'Traveling'),
        ('Maintenance', 'Maintenance')
    )
    status = models.CharField(choices=status_choices, max_length=50, default='Resting')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Requisition(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateTimeField()
    arrival_time = models.DateTimeField(null=True)
    place = models.CharField(null=True,max_length=200)
    vehicle_type = models.CharField(max_length=100)
    cause = models.IntegerField(default=0)
    reason = models.TextField()
    req_status = models.IntegerField(default=0)
    driver_id = models.ForeignKey(Driver, null=True, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.teacher_id.admin.first_name + self.teacher_id.admin.last_name


class Schedule(models.Model):
    date = models.DateTimeField()
    arrival_time = models.DateTimeField()
    place = models.CharField(max_length=200)
    vehicle_id = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Driver, null=True, on_delete=models.CASCADE)
    requisition_id = models.ForeignKey(Requisition, null=True, on_delete=models.CASCADE)
    requisition = models.BooleanField(default=False)
    completion = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


