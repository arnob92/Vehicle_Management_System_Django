from django.shortcuts import render,redirect
from app.models import Requisition,Teacher,CustomUser,Schedule,Driver,Vehicle
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

def HOME(request):
    datetime1 = datetime.now()
    print(datetime1)
    end_of_day_datetime = datetime1.replace(hour=23, minute=59, second=59, microsecond=999999)
    schedule = Schedule.objects.filter(date__gte=datetime1).filter(date__lte=end_of_day_datetime).filter(requisition=False)
    print(end_of_day_datetime,"End time")
    for i in schedule:
        print(i.date)
    context = {
        'schedule' : schedule,
    }
    return render(request,'Driver/home.html',context)


def VIEW_SCHEDULE(request):
    driver = Driver.objects.filter(admin=request.user.id)
    for i in driver:
        driver_id = i.id
        schedule = Schedule.objects.filter(driver_id=driver_id)
        context = {
            'schedule' : schedule,
        }
    return render(request,'Driver/view_schedule.html', context)


def VIEW_COMPLETE_SCHEDULE(request):
    driver = Driver.objects.filter(admin=request.user.id)
    for i in driver:
        driver_id = i.id
        schedule = Schedule.objects.filter(driver_id=driver_id)
        context = {
            'schedule': schedule,
        }
    return render(request, 'Driver/view_complete_schedule.html', context)


def DRIVER_VIEW_VEHICLE(request):
    vehicle = Vehicle.objects.all()
    context = {
        'vehicle': vehicle,
    }
    return render(request, 'Driver/driver_view_vehicle.html', context)


def DRIVER_DELETE_SCHEDULE(request, id):
    schedule = Schedule.objects.get(id=id)
    schedule.delete()
    messages.success(request, 'Schedule is Successfully Deleted')
    return redirect('driver_view_schedule')


def DRIVER_COMPLETE_SCHEDULE(request, id):
    schedule = Schedule.objects.get(id=id)
    schedule.completion = True
    if schedule.requisition:
        requisition_id = schedule.requisition_id.id
        requisition = Requisition.objects.get(id=requisition_id)
        requisition.req_status = 3
        requisition.save()
    schedule.save()
    messages.success(request, 'Schedule Completion is Successful')
    return redirect('driver_complete_schedule')
