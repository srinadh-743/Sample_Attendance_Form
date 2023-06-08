from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def att(request):
    return render(request,"mainpage.html")

def dash(request):
    return render(request,"dashboard.html")

def login_val(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print (username,"***********%%%%%%%%%%%%%%%%%")
        # Check if the user exists in the model

        #import pdb;pdb.set_trace()
        try:
            user = Employees.objects.get(username=username)
        except Employees.DoesNotExist:
            return render(request, 'mainpage.html', {'error': 'Invalid username or password'})

        # Verify the password
        if user.password != password:
            return render(request, 'mainpage.html', {'error': 'Invalid username or password'})
        return redirect('/dashboard/')

        # If the username and password match, redirect to another webpage
    else:
        return render(request, 'mainpage.html')

def submit_attendance(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        shift = request.POST.get('shift')
        project_type = request.POST.get('project-type')
        login_time = request.POST.get('login-time')
        Attendance.objects.create(date=date,shift=shift,project_type=project_type,login_time=login_time)
        return render(request,'dashboard.html')

        # Create a new instance of the Attendance model
        # attendance = Attendance(
        #     date=date,
        #     shift=shift,
        #     project_type=project_type,
        #     login_time=login_time
        # )
        #
        # # Save the instance to the database
        # attendance.save()

        return redirect('dashboard')  # Redirect to the dashboard or any other page

    return render(request, 'dashboard.html')