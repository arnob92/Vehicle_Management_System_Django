from django.shortcuts import render, redirect
from app.models import Requisition, Teacher, CustomUser, Vehicle, Schedule
from datetime import datetime
from django.contrib import messages


def HOME(request):
    datetime1 = datetime.now()
    end_of_day_datetime = datetime1.replace(hour=23, minute=59, second=59, microsecond=999999)
    schedule = Schedule.objects.filter(date__gte=datetime1).filter(date__lte=end_of_day_datetime).filter(requisition=False)
    context = {
        'schedule': schedule,
    }
    return render(request, 'Teacher/home.html', context)


def TEACHER_APPLY_REQUISITION(request):
    teacher = Teacher.objects.filter(admin=request.user.id)
    for i in teacher:
        teacher_id = i.id
        requisition_history = Requisition.objects.filter(teacher_id=teacher_id)

        context = {
            'requisition_history': requisition_history,
        }
    return render(request, 'Teacher/apply_requisition.html', context)


def TEACHER_APPLY_REQUISITION_SAVE(request):
    if request.method == "POST":
        req_date = request.POST.get('req_date')
        arrival_time = request.POST.get('arrival_time')
        from_place = request.POST.get('from_place')
        to_place = request.POST.get('to_place')
        vehicle_type = request.POST.get('vehicle_type')
        cause = request.POST.get('cause')
        reason = request.POST.get('reason')
        place = "From " + from_place + " To " + to_place
        teacher = Teacher.objects.get(admin=request.user.id)
        req_status = 0

        requisition = Requisition(
            teacher_id=teacher,
            date=req_date,
            arrival_time=arrival_time,
            place=place,
            vehicle_type=vehicle_type,
            cause=cause,
            reason=reason,
            req_status=req_status,
        )
        requisition.save()
        messages.success(request, 'Requisition Request is Successfully Added')
        return redirect('teacher_apply_requisition')


def REQUISITION_CANCEL(request, id):
    requisition = Requisition.objects.get(id=id)
    requisition.req_status = 4
    requisition.save()
    messages.success(request, 'Requisition is Canceled Successfully')
    return redirect('teacher_apply_requisition')


def TEACHER_VIEW_VEHICLE(request):
    vehicle = Vehicle.objects.all()
    context = {
        'vehicle': vehicle,
    }
    return render(request, 'Teacher/teacher_view_vehicle.html', context)

