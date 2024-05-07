from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import Department, CustomUser, Teacher, Driver, Vehicle, Requisition, Schedule
from django.contrib import messages
from datetime import datetime


@login_required(login_url='/')
def HOME(request):
    datetime1 = datetime.now()
    end_of_day_datetime = datetime1.replace(hour=23, minute=59, second=59, microsecond=999999)
    schedule = Schedule.objects.filter(date__gte=datetime1).filter(date__lte=end_of_day_datetime)
    context = {
        'schedule': schedule,
    }
    return render(request, 'Office/home.html', context)


@login_required(login_url='/')
def ADD_TEACHER(request):
    department = Department.objects.all()
    if request.method == 'POST':
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        department_id = request.POST.get("department_id")
        designation = request.POST.get("designation")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is Already Taken')
            return redirect('add_teacher')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'UserName is Already Taken')
            return redirect('add_teacher')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2

            )
            user.set_password(password)
            user.save()
            department = Department.objects.get(id=department_id)

            teacher = Teacher(
                admin=user,
                phone_number=phone_number,
                department_id=department_id,
                designation=designation,

            )

            teacher.save()
            messages.success(request, user.first_name + ' ' + user.last_name + ' is successfully added')
            return redirect('view_teacher')

        # print(profile_pic,first_name,last_name,department_id,designation,phone_number,email,username,password)
    context = {
        'department': department,
    }
    return render(request, 'Office/add_teacher.html', context)


@login_required(login_url='/')
def VIEW_TEACHER(request):
    teacher = Teacher.objects.all()

    context = {
        'teacher': teacher,
    }
    return render(request, 'Office/view_teacher.html', context)


@login_required(login_url='/')
def EDIT_TEACHER(request, id):
    teacher = Teacher.objects.filter(id=id)
    department = Department.objects.all()
    context = {
        'teacher': teacher,
        'department': department,
    }
    return render(request, 'Office/edit_teacher.html', context)


@login_required(login_url='/')
def UPDATE_TEACHER(request):
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        department_id = request.POST.get("department_id")
        designation = request.POST.get("designation")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = CustomUser.objects.get(id=teacher_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != '':
            user.set_password(password)
        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic
        user.save()

        teacher = Teacher.objects.get(admin=teacher_id)
        teacher.designation = designation
        teacher.phone_number = phone_number

        department = Department.objects.get(id=department_id)
        teacher.department_id = department_id

        teacher.save()

        messages.success(request, 'Updated Teacher is successful')
        return redirect('view_teacher')

    return render(request, 'Office/edit_teacher.html')


@login_required(login_url='/')
def DELETE_TEACHER(request, admin):
    teacher = CustomUser.objects.get(id=admin)
    teacher.delete()
    messages.success(request, 'Teacher is Successfully Deleted')
    return redirect('view_teacher')


@login_required(login_url='/')
def ADD_DRIVER(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is Already Taken')
            return redirect('add_driver')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'UserName is Already Taken')
            return redirect('add_driver')
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3

            )
            user.set_password(password)
            user.save()

            driver = Driver(
                admin=user,
                phone_number=phone_number,
            )
            driver.save()
            messages.success(request, 'Driver is Added Successfully')
            return redirect('view_driver')

    return render(request, 'Office/add_driver.html')


@login_required(login_url='/')
def VIEW_DRIVER(request):
    driver = Driver.objects.all()

    context = {
        'driver': driver,
    }
    return render(request, 'Office/view_driver.html', context)


@login_required(login_url='/')
def EDIT_DRIVER(request, id):
    driver = Driver.objects.filter(id=id)
    context = {
        'driver': driver,

    }
    return render(request, 'Office/edit_driver.html', context)


@login_required(login_url='/')
def UPDATE_DRIVER(request):
    if request.method == 'POST':
        driver_id = request.POST.get('driver_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = CustomUser.objects.get(id=driver_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != '':
            user.set_password(password)
        if profile_pic != None and profile_pic != '':
            user.profile_pic = profile_pic
        user.save()

        driver = Driver.objects.get(admin=driver_id)
        driver.phone_number = phone_number

        driver.save()

        messages.success(request, 'Driver Update is successful')
        return redirect('view_driver')

    return render(request, 'Office/edit_driver.html')


@login_required(login_url='/')
def DELETE_DRIVER(request, admin):
    driver = CustomUser.objects.get(id=admin)
    driver.delete()
    messages.success(request, 'Driver is Successfully Deleted')
    return redirect('view_driver')


def ADD_VEHICLE(request):
    driver = Driver.objects.all()
    if request.method == "POST":
        vehicle_name = request.POST.get('vehicle_name')
        licence_number = request.POST.get('licence_number')
        driver_id = request.POST.get('driver_id')

        driver = Driver.objects.get(id=driver_id)

        vehicle = Vehicle(
            name=vehicle_name,
            licence_number=licence_number,
            driver=driver,

        )
        vehicle.save()
        messages.success(request, 'Vehicle is Successfully Added')
        return redirect('add_vehicle')
    context = {
        'driver': driver,
    }

    return render(request, 'Office/add_vehicle.html', context)


def VIEW_VEHICLE(request):
    vehicle = Vehicle.objects.all()
    context = {
        'vehicle': vehicle,
    }
    return render(request, 'Office/view_vehicle.html', context)


def EDIT_VEHICLE(request, id):
    vehicle = Vehicle.objects.filter(id=id)
    driver = Driver.objects.all()
    context = {
        'vehicle': vehicle,
        'driver': driver,
    }

    return render(request, 'Office/edit_vehicle.html', context)


def UPDATE_VEHICLE(request):
    if request.method == "POST":
        vehicle_id = request.POST.get('vehicle_id')
        name = request.POST.get('name')
        licence_number = request.POST.get('licence_number')
        driver_id = request.POST.get('driver')
        status = request.POST.get('status')

        driver = Driver.objects.get(id=driver_id)

        vehicle = Vehicle(
            id=vehicle_id,
            name=name,
            licence_number=licence_number,
            driver=driver,
            status=status,
        )
        vehicle.save()
        messages.success(request, 'Vehicle is Successfully Updated')
        return redirect('view_vehicle')
    return None


def DELETE_VEHICLE(request, id):
    vehicle = Vehicle.objects.get(id=id)
    vehicle.delete()
    messages.success(request, 'Vehicle is Successfully Deleted')
    return redirect('view_vehicle')


def ADD_DEPARTMENT(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        department = Department(
            name=name,
        )
        department.save()
        messages.success(request, 'Department is Added Successfully')
        redirect('add_department')
    return render(request, 'Office/add_department.html')


def VIEW_DEPARTMENT(request):
    department = Department.objects.all()
    context = {
        "department": department,
    }
    return render(request, 'Office/view_department.html', context)


def EDIT_DEPARTMENT(request, id):
    department = Department.objects.filter(id=id)
    context = {
        'department': department,
    }
    return render(request, 'Office/edit_department.html', context)


def UPDATE_DEPARTMENT(request):
    if request.method == "POST":
        department_id = request.POST.get('department_id')
        name = request.POST.get('name')
        department = Department(
            id=department_id,
            name=name,

        )
        department.save()
        messages.success(request, 'Department is Successfully Updated')
        return redirect('view_department')
    return None


def DELETE_DEPARTMENT(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    messages.success(request, 'Department is Successfully Deleted')
    return redirect('view_department')


def REQUISITION_VIEW(request):
    requisition = Requisition.objects.all()
    context = {
        'requisition': requisition,
    }
    return render(request, 'Office/requisition_view.html', context)


def TEACHER_APPROVE_REQUISITION(request, id):
    requisition = Requisition.objects.filter(id=id)
    schedule = Schedule.objects.filter(completion=False)
    teacher = Teacher.objects.all()
    driver = Driver.objects.all()
    vehicle = Vehicle.objects.all()
    notvehicle_list = []
    notdriver_list = []
    for i in requisition:
        for j in schedule:
            if j.date < i.date < j.arrival_time:
                notdriver_list.append(j.driver_id)
                notvehicle_list.append(j.vehicle_id)
            elif j.date < i.arrival_time < j.arrival_time:
                notdriver_list.append(j.driver_id)
                notvehicle_list.append(j.vehicle_id)

    context = {
        'requisition': requisition,
        'teacher': teacher,
        'driver': driver,
        'vehicle': vehicle,
        'notvehicle_list':notvehicle_list,
        'notdriver_list':notdriver_list,
    }
    return render(request, 'Office/requisition_approval.html', context)


def TEACHER_DISAPPROVE_REQUISITION(request, id):
    requisition = Requisition.objects.get(id=id)
    requisition.req_status = 2
    requisition.save()
    return redirect('requisition_view')


def TEACHER_APPROVE_REQUISITION_SAVE(request):
    if request.method == "POST":
        req_id = request.POST.get('req_id')
        driver_id = request.POST.get('driver_id')
        vehicle_id = request.POST.get('vehicle_id')

        if driver_id is None:
            messages.warning('Please Fill Driver')

        elif vehicle_id is None:
            messages.warning("Please Fill Vehicle")

        driver = Driver.objects.get(id=driver_id)
        vehicle = Vehicle.objects.get(id=vehicle_id)
        requisition = Requisition.objects.get(id=req_id)
        requisition.driver_id = driver
        requisition.vehicle_id = vehicle
        requisition.req_status = 1
        requisition.save()
        date = requisition.date
        arrival_time = requisition.arrival_time
        place = requisition.place
        requisition_status = True
        completion = False

        schedule = Schedule(
            date=date,
            arrival_time=arrival_time,
            place=place,
            vehicle_id=vehicle,
            driver_id=driver,
            requisition=requisition_status,
            requisition_id=requisition,
            completion=completion,
        )
        schedule.save()

        messages.success(request, f'Requisition no. {req_id} is Approved Successfully')
        return redirect('requisition_view')


def ADD_SCHEDULE(request):

    if request.method == "POST":
        date = request.POST.get('date')
        arrival_time = request.POST.get('arrival_time')
        from_place = request.POST.get('from_place')
        to_place = request.POST.get('to_place')
        via_place = request.POST.get('via_place')
        """vehicle_id = request.POST.get('vehicle_id')
        driver_id = request.POST.get('driver_id')"""
        completion = False
        requisition = False
        if len(via_place) > 0:
            place = "From " + from_place + " To " + to_place + " Via " + via_place
        else:
            place = "From " + from_place + " To " + to_place

        """vehicle = Vehicle.objects.get(id=vehicle_id)
        driver = Driver.objects.get(admin=driver_id)"""

        """check_schedule = Schedule.objects.filter(completion=False)

        for i in check_schedule:
            if (i.date < date < i.arrival_time) or (i.date < arrival_time < i.arrival_time):
                if i.driver_id == driver:
                    messages.warning(request,'Driver has schedule')
                    if i.vehicle_id == vehicle:
                        messages.warning(request,'Vehicle has schedule')
                    return redirect('add_schedule')"""

        schedule = Schedule(
            date=date,
            arrival_time=arrival_time,
            place=place,
            requisition=requisition,
            completion=completion,
        )
        schedule.save()
        messages.warning(request, 'Add Driver and Vehicle')
        return redirect('add_schedule_other')

    return render(request, 'Office/add_schedule.html')


def ADD_SCHEDULE_OTHER(request):

    schedule = Schedule.objects.last()
    nschedule = Schedule.objects.filter(completion=False)
    notvehicle_list = []
    notdriver_list = []

    for j in nschedule:
            if j.date<schedule.date<j.arrival_time:
                notdriver_list.append(j.driver_id)
                notvehicle_list.append(j.vehicle_id)
            elif j.date<schedule.arrival_time<j.arrival_time:
                notdriver_list.append(j.driver_id)
                notvehicle_list.append(j.vehicle_id)
    print(notvehicle_list)
    print(notdriver_list)

    vehicle = Vehicle.objects.all()

    driver = Driver.objects.all()
    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle_id')
        driver_id = request.POST.get('driver_id')
        vvehicle = Vehicle.objects.get(id=vehicle_id)
        ddriver = Driver.objects.get(admin=driver_id)
        schedule.vehicle_id=vvehicle
        schedule.driver_id=ddriver
        schedule.save()
        messages.success(request,'Add Schedule is successful')
        return redirect('view_schedule')
    context = {
        'vehicle': vehicle,
        'driver': driver,
        'schedule': schedule,
        'notvehicle_list':notvehicle_list,
        'notdriver_list':notdriver_list,

    }
    return render(request,'Office/add_schedule_other.html',context)


def VIEW_SCHEDULE(request):
    schedule = Schedule.objects.filter(completion=False)
    context = {
        'schedule': schedule,
    }
    return render(request, 'Office/view_schedule.html', context)


def VIEW_COMPLETE_SCHEDULE(request):
    schedule = Schedule.objects.filter(completion=True)
    context = {
        'schedule': schedule,
    }
    return render(request, 'Office/view_complete_schedule.html', context)


def DELETE_SCHEDULE(request, id):
    schedule = Schedule.objects.get(id=id)
    schedule.delete()
    messages.success(request, 'Schedule is Successfully Deleted')
    return redirect('view_schedule')


def COMPLETE_SCHEDULE(request, id):
    schedule = Schedule.objects.get(id=id)
    schedule.completion = True
    if schedule.requisition:
        requisition_id = schedule.requisition_id.id
        requisition = Requisition.objects.get(id=requisition_id)
        requisition.req_status = 3
        requisition.save()
    schedule.save()
    messages.success(request, 'Schedule Completion is Successful')
    return redirect('view_schedule')


