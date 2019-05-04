from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core import serializers

import json, calendar

import datetime

from django.contrib.auth.models import User
from .models import *

from .utils import CodeGenerator

"""
Default index handler.
"""
def index(request):

    if request.user.is_authenticated:

        request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath

        context = {}
        context['username'] = request.user.username

        if request.user.is_staff:
            context = {}

            combined_queryset = Message.objects.filter(receiver=request.user)
            messages = combined_queryset.values('sender').distinct()

            chat_list = []

            for message in messages:
                user = User.objects.get(id=message['sender'])
                try:
                    attrib = UserAttrib.objects.get(user=user)
                    user.imgpath = attrib.imgpath
                except:
                    user.imgpath = '/media/001.png'
                print(user)
                chat_list.append(user)


            context['chat_list'] = chat_list

            return render(request, 'appointment.html', context)
        else:
            userattrib = UserAttrib.objects.get(user=request.user)
            
            scs = User.objects.get(username='scs')
            context['scs'] = UserAttrib.objects.get(user=scs)
            coet = User.objects.get(username='coet')
            context['coet'] = UserAttrib.objects.get(user=coet)
            csm = User.objects.get(username='csm')
            context['csm'] = UserAttrib.objects.get(user=csm)
            ced = User.objects.get(username='ced')
            context['ced'] = UserAttrib.objects.get(user=ced)
            cass = User.objects.get(username='cass')
            context['cass'] = UserAttrib.objects.get(user=cass)
            cbaa = User.objects.get(username='cbaa')
            context['cbaa'] = UserAttrib.objects.get(user=cbaa)
            con = User.objects.get(username='con')
            context['con'] = UserAttrib.objects.get(user=con)

            return render(request, 'index.html', context)
    else:
        return redirect('/openapp/login')


"""
API for generating a code.
Generates a code.
Then adds code to database.
"""
def generateCode(request):

    # Generate code.
    # If code already exists,
    # generate until valid for
    # 3 tries.

    response = {}
    valid = False
    code = None
    tries = 0

    while(not valid and tries <= 3):
        code = createCode()

        if(not codeExists(code)):
            valid = True
            break

        tries = tries + 1

    # If code is valid, add to database.
    # Otherwise, tell user to try again
    # with code NULL.

    if valid and addCode(code):
        response['rc'] = 'success'
        response['code'] = code
    else:
        response['rc'] = 'failed'
        response['code'] = None

    return JsonResponse(response)


"""

"""
def register(request):

    if request.method == 'GET':
        context = {}
        return render(request, 'register.html', context)

    elif request.method == 'POST':
        refcode = request.POST.get('refcode', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        response = {}

        if not codeUsed(refcode):
            # Create user if code is valid
            try:
                logout(request)
                user = User.objects.create_user(username=username)
                user.set_password(password)
                user.is_staff = False
                user.active = True
                user.save()
                print('Creating UserAttrib')
                attrib = UserAttrib(user=user, imgpath='/media/vector.jpg')
                attrib.save()
                print('Successful UserAttrib')
                # Invalidate code
                setCodeStatus(refcode)

                response['rc'] = 'OK'
            except:
                response['rc'] = 'NOT OK'
                response['errormessage'] = 'Invalid username or password.'
        else:
            response['rc'] = 'NOT OK'
            response['errormessage'] = 'Ref code does not exist or is already used.'

        return JsonResponse(response)


"""

"""
def loginUser(request):

    context = {}

    if request.method == 'GET':
        return render(request, 'login.html', context)
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print('user is not none')
            login(request, user)
            context['rc'] = 'OK'
        else:
            print('user is none')
            context['rc'] = 'NOT OK'
            context['errormessage'] = 'Invalid credentials.'

        return JsonResponse(context)


def logoutUser(request):

    logout(request)
    return redirect('/openapp/login')


def settings(request):
    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath
    request.user.attrib = UserAttrib.objects.get(user=request.user)
    context = {}
    context['username'] = request.user.username
    if request.user.is_staff:
        
        return render(request, 'settings_gcc.html', context)
    else:
        
        return render(request, 'settings.html', context)


def information(request, schedule):
    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath
    context = {}
    context['username'] = request.user.username
    context['schedule'] = schedule
    return render(request, 'information.html', context)


def book(request):
    context = {}
    context['schedule'] = request.GET['schedule']
    context['name'] = request.GET['name']
    context['idno'] = request.GET['id']
    context['college'] = request.GET['college']
    context['yrcourse'] = request.GET['yrcourse']
    context['gender'] = request.GET['inlineRadioOptions']
    context['location'] = request.GET['location']
    context['success'] = True
    try:
        schedule = Schedule.objects.get(id=context['schedule'])
        schedule.assignee = request.user.username
        schedule.info_name = context['name']
        schedule.info_id = context['idno']
        schedule.info_college = context['college']
        schedule.info_yrcourse = context['yrcourse']
        schedule.info_gender = context['gender']
        schedule.info_location = context['location']
        schedule.save()

    except:
        return HttpResponse('Bad Request!')

    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath
    context['username'] = request.user.username

    return render(request, 'information.html', context)

def updatepseudoname(request):
    pseudoname = request.GET['changePseudoNameInput']

    if pseudoname is '':
        request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath
        context = {}
        context['namemessage'] = 'Invalid username.'
        context['username'] = request.user.username
        return render(request, 'settings.html', context)

    try:
        user = User.objects.get(username=request.user.username)
        user.username = pseudoname
        user.save()
    except:
        request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath
        context = {}
        context['namemessage'] = 'Invalid username.'
        context['username'] = request.user.username
        return render(request, 'settings.html', context)
        
    return redirect('/openapp/settings')

def updatepassword(request):
    oldpassword = request.GET['oldPasswordInput']
    newpassword = request.GET['newPasswordInput']
    confirmationpassword = request.GET['retypePasswordInput']

    if oldpassword is '' or newpassword is '' or confirmationpassword is '':
        request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath
        context = {}
        context['passmessage'] = 'Please fill out all forms.'
        context['username'] = request.user.username
        return render(request, 'settings.html', context)

    if newpassword != confirmationpassword:
        request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath
        context = {}
        context['passmessage'] = 'Password did not match.'
        context['username'] = request.user.username
        return render(request, 'settings.html', context)

    user = User.objects.get(username=request.user.username)
    user = authenticate(request, username=request.user.username, password=oldpassword)

    if user is not None:
        user.set_password(newpassword)
        user.save()
    else:
        request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath
        context = {}
        context['passmessage'] = 'Password mismatch.'
        context['username'] = request.user.username
        return render(request, 'settings.html', context)

    return redirect('/openapp/login')


def collegeprofile(request, college):

    context = {}
    context['college'] = college

    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath

    if request.user.is_authenticated:
        # Get councilor for college
        try:
            user = User.objects.get(username__icontains=college)
            userAttrib = UserAttrib.objects.get(user=user)

            if user is not None:
                context['user'] = user
                context['guidancefirstname'] = user.first_name
                context['guidancelastname'] = user.last_name
                context['imgpath'] = userAttrib.imgpath
                context['guidancecourse'] = userAttrib.course
                context['guidancebirthday'] = userAttrib.birthday
                context['guidancelocation'] = userAttrib.location
            else:
                print('no user')
                context['errormessage'] = 'BAD OUTPUT'
        except:
            print('errro errors')
            context['errormessage'] = 'BAD OUTPUT'

        # Return requested info
        return render(request, 'profile.html', context)
    else:
        return redirect('/openapp/login')


def chat(request):

    context = {}

    if request.method == 'GET':
        return HttpResponse('GET')

    elif request.method == 'POST':
        sender = request.user
        receiver = User.objects.get(username=request.POST.get('college', ''))
        message = request.POST.get('message', '')

        message = Message(sender=sender, receiver=receiver, message=message)
        message.save()

        return JsonResponse(context)


def getMessages(request):
    context = {}

    receiver = request.GET['receiver']
    user = User.objects.get(username=receiver)
    combined_queryset = Message.objects.filter(sender=request.user, receiver=user) | Message.objects.filter(sender=user, receiver=request.user)
    print(combined_queryset)
    messages = combined_queryset.order_by('date_created')

    res = list(messages.values('message', 'sender', 'receiver', 'date_created'))

    context['messages'] = []

    for message in res:
        u = User.objects.get(id=message['sender'])
        message['sender'] = u.username

        u = User.objects.get(id=message['receiver'])
        message['receiver'] = u.username

        context['messages'].append(message)

    return JsonResponse(context)

def collegechat(request, college):
    context = {}

    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath

    user = User.objects.get(username__icontains=college)
    userAttrib = UserAttrib.objects.get(user=user)
    context['imgpath'] = userAttrib.imgpath
    context['college'] = college

    combined_queryset = Message.objects.filter(sender=user, receiver=request.user) | Message.objects.filter(sender=request.user, receiver=user)
    print(combined_queryset)
    messages =  combined_queryset.order_by('date_created')
    print(messages)
    for message in messages:
        print(message.date_created)
    context['messages'] = messages

    return render(request, 'chat.html', context)


def appoint(request, college):
    context = {}

    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath

    date_today = datetime.date.today()
    year_today = date_today.year
    month_today = date_today.month

    num_days = calendar.monthrange(year_today, month_today)[1]
    days = [datetime.date(year_today, month_today, day) for day in range(1, num_days+1)]

    context['today'] = date_today
    context['days'] = days
    context['college'] = college

    w = str(days[0].weekday())
    v = str(days[-1].weekday())

    if w in '0':
        context['ran'] = range(1)
    elif w in '1':
        context['ran'] = range(2)
    elif  w in '2':
        context['ran'] = range(3)
    elif w in '3':
        context['ran'] = range(4)
    elif w in '4':
        context['ran'] = range(5)
    elif w in '5':
        context['ran'] = range(6)
    elif w in '6':
        context['ran'] = range(0)

    if v in '0':
        context['end'] = range(5)
    elif v in '1':
        context['end'] = range(4)
    elif  v in '2':
        context['end'] = range(3)
    elif v in '3':
        context['end'] = range(2)
    elif v in '4':
        context['end'] = range(1)
    elif v in '5':
        context['end'] = range(0)
    elif v in '6':
        context['end'] = range(6)

    return render(request, 'appoint.html', context)


def appointments(request):
    context = {}

    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath

    date_today = datetime.date.today()
    year_today = date_today.year
    month_today = date_today.month

    num_days = calendar.monthrange(year_today, month_today)[1]
    days = [datetime.date(year_today, month_today, day) for day in range(1, num_days + 1)]

    context['today'] = date_today
    context['days'] = days

    w = str(days[0].weekday())
    v = str(days[-1].weekday())

    if w in '0':
        context['ran'] = range(1)
    elif w in '1':
        context['ran'] = range(2)
    elif w in '2':
        context['ran'] = range(3)
    elif w in '3':
        context['ran'] = range(4)
    elif w in '4':
        context['ran'] = range(5)
    elif w in '5':
        context['ran'] = range(6)
    elif w in '6':
        context['ran'] = range(0)

    if v in '0':
        context['end'] = range(5)
    elif v in '1':
        context['end'] = range(4)
    elif v in '2':
        context['end'] = range(3)
    elif v in '3':
        context['end'] = range(2)
    elif v in '4':
        context['end'] = range(1)
    elif v in '5':
        context['end'] = range(0)
    elif v in '6':
        context['end'] = range(6)

    return render(request, 'appointments.html', context)


def createappointments(request):

    context = {}

    schedule = request.GET['schedule']
    day = request.GET['day']

    sched = Schedule(counselor=request.user, time=schedule, date=datetime.datetime.strptime(day, '%B %d, %Y').date())
    sched.save()

    context['rc'] = 'OK'
    return JsonResponse(context)

def deleteappointments(request):

    id = request.GET['id']

    sched = Schedule.objects.get(id=id)
    sched.delete()

    return JsonResponse({})

def getAppointmentSchedules(request, college):

    date_str = request.GET['day']
    sched = datetime.datetime.strptime(date_str, '%B %d, %Y').date()


    context = {}
    context['rc'] = 'OK'

    try:
        counselor = User.objects.get(username__icontains=college)
        scheds = Schedule.objects.filter(counselor=counselor, date=sched)

        context['0'] = False
        context['1'] = False
        context['2'] = False
        context['3'] = False
        context['4'] = False
        context['5'] = False
        context['6'] = False
        context['7'] = False

        if scheds is None  or len(scheds) == 0:
            context['scheds'] = 'None'

        else:
            context['scheds'] = list(scheds.values())
            for sched in scheds:
                if sched.time == '8:00AM - 9:00AM':
                    context['0'] = True if (sched.status == 'AVAILABLE' and sched.assignee == '')  else False
                    context['id0'] = sched.id                    
                elif sched.time == '9:00AM - 10:00AM':
                    context['1'] = True if sched.status == 'AVAILABLE' and sched.assignee == ''  else False
                    context['id1'] = sched.id
                elif sched.time == '10:00AM - 11:00AM':
                    context['2'] = True if sched.status == 'AVAILABLE' and sched.assignee == ''  else False
                    context['id2'] = sched.id
                elif sched.time == '11:00AM - 12:00AM':
                    context['3'] = True if sched.status == 'AVAILABLE' and sched.assignee == ''  else False
                    context['id3'] = sched.id
                elif sched.time == '1:00PM - 2:00PM':
                    context['4'] = True if sched.status == 'AVAILABLE' and sched.assignee == ''  else False
                    context['id4'] = sched.id
                elif sched.time == '2:00PM - 3:00PM':
                    context['5'] = True if sched.status == 'AVAILABLE' and sched.assignee == ''  else False
                    context['id5'] = sched.id
                elif sched.time == '3:00PM - 4:00PM':
                    context['6'] = True if sched.status == 'AVAILABLE' and sched.assignee == ''  else False
                    context['id6'] = sched.id
                elif sched.time == '4:00PM - 5:00PM':
                    context['7'] = True if sched.status == 'AVAILABLE' and sched.assignee == ''  else False
                    context['id7'] = sched.id

    except:
        context['rc'] = 'NOT OK'


    return JsonResponse(context)


def gccAppointmentSchedules(request, college):

    context = {}
    context['guidance'] = college

    date_str = request.GET['day']
    sched = datetime.datetime.strptime(date_str, '%B %d, %Y').date()
    context['sched'] = sched

    counselor = User.objects.get(username__icontains=college)
    scheds = Schedule.objects.filter(counselor=counselor, date=sched)

    context['0'] = False
    context['1'] = False
    context['2'] = False
    context['3'] = False
    context['4'] = False
    context['5'] = False
    context['6'] = False
    context['7'] = False

    if scheds is None  or len(scheds) == 0:
        context['scheds'] = 'None'
        
    else:
        context['scheds'] = 'Exists'
        for sched in scheds:
            if sched.time == '8:00AM - 9:00AM':
                context['0'] = True if sched.status == 'AVAILABLE'  else False
            elif sched.time == '9:00AM - 10:00AM':
                context['1'] = True if sched.status == 'AVAILABLE'  else False
            elif sched.time == '10:00AM - 11:00AM':
                context['2'] = True if sched.status == 'AVAILABLE'  else False
            elif sched.time == '11:00AM - 12:00AM':
                context['3'] = True if sched.status == 'AVAILABLE'  else False
            elif sched.time == '1:00PM - 2:00PM':
                context['4'] = True if sched.status == 'AVAILABLE'  else False
            elif sched.time == '2:00PM - 3:00PM':
                context['5'] = True if sched.status == 'AVAILABLE'  else False
            elif sched.time == '3:00PM - 4:00PM':
                context['6'] = True if sched.status == 'AVAILABLE'  else False
            elif sched.time == '4:00PM - 5:00PM':
                context['7'] = True if sched.status == 'AVAILABLE'  else False
            
        print(scheds)        

    return JsonResponse(context)


def setGccAppointmentSchedule(request):
    
    context = {}

    date_str = request.GET['day']
    sched = datetime.datetime.strptime(date_str, '%B %d, %Y').date()
    context['sched'] = sched

    context['time'] = request.GET['sched']

    schedule = None

    try:
        schedule = Schedule.objects.get(counselor=request.user, date=context['sched'], time=context['time'])
    except:
        schedule = Schedule(counselor=request.user, date=context['sched'], time=context['time'], status='NOT_AVAILABLE')
        schedule.save()

    context['status'] = request.GET['status']
    schedule.status = context['status']
    schedule.save()

    return JsonResponse(context)


def setAppointmentSchedule(request):
    context = {}

    id = request.GET['id']
    assignee = request.user.username

    schedule = Schedule.objects.get(id=id)
    schedule.assignee = assignee
    schedule.save()

    return JsonResponse(context)

def cancelAppointment(request):
    context = {}

    id = request.GET['id']

    schedule = Schedule.objects.get(id=id)
    schedule.assignee = ''
    schedule.save()

    return JsonResponse(context)

"""
API for checking if code exists.
"""
def hasCode(request):

    code = request.GET['code']

    response = {}
    response['code'] = code

    if codeExists(code):
        response['exists'] = True
    else:
        response['exists'] = False

    return JsonResponse(response)

"""
API for getting code status.
"""
def getCodeStatus(request):

    code = request.GET['code']
    response = {}

    if codeExists(code):
        response['rc'] = 'success'
        response['code'] = code
        response['isUsed'] = codeUsed(code)
    else:
        response['rc'] = 'failed'
        response['message'] = 'No code  exists.'

    return JsonResponse(response)


"""
API for setting code is used.
"""
def setCodeAsUsed(request):

    code = request.GET['code']

    response = {}
    response['code'] = code

    if codeExists(code) and not codeUsed(code):
        setCodeStatus(code)
        response['rc'] = 'success'
        response['isUsed'] = True

    else:
        response['rc'] = 'failed'
        response['isUsed'] = False

    return JsonResponse(response)

"""
Generates a code.
"""
def createCode():

    codeGenerator = CodeGenerator()
    id = codeGenerator.getCode()

    return id

"""
Check if code already exists.
"""
def codeExists(code):

    # Check database if code exists

    isExists = False
    try:
        res = Code.objects.get(code=code)
        isExists = True
    except:
        isExists = False

    return isExists

"""
Gets code status.
"""
def codeUsed(code):

    # Check code status in database
    isError = False
    try:
        res = Code.objects.get(code=code)
        if res.used:
            isError = True
    except:
        isError = True

    return isError

"""
Sets the code is already used.
"""
def setCodeStatus(code):

    res = Code.objects.get(code=code)
    res.used = True
    res.save()

"""
Adds the code to the database
"""
def addCode(code):

    rc = True

    # Add code to the database
    newCode = Code(code=code)
    newCode.save()

    return rc


def admin(request):
    if request.method == 'GET':
        if request.user.is_staff:
            context = {}
            return render(request, 'admin.html', context)
        return HttpResponse('404 ERROR NOT FOUND')
    elif request.method == 'POST':
        try:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            firstname = request.POST.get('firstname', '')
            lastname = request.POST.get('lastname', '')
            course = request.POST.get('course', '')
            birthday = request.POST.get('birthday', '')
            location = request.POST.get('location', '')
            user = User.objects.create_user(username=username)
            user.set_password(password)
            user.is_staff = True
            user.first_name = firstname
            user.last_name = lastname            
            user.save()

            attrib = UserAttrib(user=user, imgpath='/media/vector.jpg')
            attrib.course = course
            attrib.birthday = birthday
            attrib.location = location
            attrib.save()

            # Generate default schedules


            return HttpResponse('User created successfully!')
        except:
            return HttpResponse('ERROR CREATING USER')


from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        attrib = UserAttrib.objects.get(user=request.user)
        attrib.imgpath = uploaded_file_url
        attrib.save()
        request.user.imgpath = uploaded_file_url
        print('Uploaded to: ' + uploaded_file_url)
        return redirect('/openapp')

def updatedata(request):

    context = {}
    
    if request.method == 'POST':
        context['degree'] = request.POST['degree']
        context['birthdate'] = request.POST['birthdate']
        context['address'] = request.POST['address']

        attrib = UserAttrib.objects.get(user=request.user)
        attrib.course = context['degree']
        attrib.birthday = context['birthdate']
        attrib.location = context['address']
        attrib.save()

        return redirect('/openapp/settings')