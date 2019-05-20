from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
import time
import json
import calendar
from json import JSONEncoder


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

            # Date computations
            date_today = datetime.date.today()
            year_today = date_today.year
            month_today = date_today.month
            day_today = date_today.day

            num_days = calendar.monthrange(year_today, month_today)[1]
            days = [datetime.date(year_today, month_today, day)
                    for day in range(1, num_days + 1)]

            w = str(days[0].weekday())
            v = str(days[-1].weekday())

            context = {}
            context['date_today'] = date_today
            context['year_today'] = year_today
            context['month_today'] = month_today
            context['day_today'] = day_today
            context['num_days'] = num_days
            context['days'] = days
            context['starting_day'] = w
            context['ending_day'] = v

            # Get appointments
            schedules = Schedule.objects.filter(
                counselor=request.user, approved='APPROVED', date=date_today)
            if schedules is None or len(schedules) == 0:
                context['scheds'] = 'None'

            else:
                print('ENTERING MAZE')

                # sort based on time schedule
                sortedSched = []
                for sched in schedules:
                    sched.startTime = sched.time.split(' ')[0]

                format = '%I:%M%p'

                sortedSched = sorted(schedules, key=lambda sched: time.strptime(sched.startTime, format))
                print('PRINTING RESULTS:::')
                print(sortedSched)
                context['schedules'] = []

                for sched in sortedSched:
                    x = {}
                    x['sched_id'] = sched.id
                    x['time'] = sched.time
                    x['info_location'] = sched.info_location
                    x['info_name'] = sched.info_name
                    x['sched_available'] = True if (sched.status == 'AVAILABLE' and sched.assignee == '') else False
                    context['schedules'].append(x)

            # Compute
            lead = int(w) + 1
            lag = 5 - int(v)

            dayArray = []
            for day in days:
                dayArray.append(day.day)

            for i in range(lead):
                dayArray.insert(0, -1)
            for i in range(lag):
                dayArray.append(-1)

            day_per_week = []
            dayList = []

            counter = 0
            for day in dayArray:
                if counter < 7:
                    dayList.append(day)
                    counter = counter + 1
                else:
                    day_per_week.append(dayList)
                    dayList = []
                    dayList.append(day)
                    counter = 1

            day_per_week.append(dayList)

            context['day_per_week'] = day_per_week

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
    try:
        context['schedule'] = request.GET['schedule']
        context['name'] = request.GET['name']
        context['info_contact_number'] = request.GET['info_contact_number']
        context['idno'] = request.GET['id']
        context['college'] = request.GET['college']
        context['yrcourse'] = request.GET['yrcourse']
        context['studentyear'] = request.GET['studentyear']
        context['gender'] = request.GET['inlineRadioOptions']
        context['location'] = request.GET['location']
        context['success'] = True
    except:
        return redirect('/openapp/information')

    # if context['schedule'] == '' or context['name'] == '' or context['idno'] == '' or context['college'] == '' or context['yrcourse'] == '' or context['gender'] == '' or context['location'] == '' or context['studentyear'] == '':
    #     print(context)
    #     request.user.imgpath = UserAttrib.objects.get(
    #         user=request.user).imgpath
    #     context['success'] = False
    #     context['username'] = request.user.username
    #     context['errormessage'] = 'Please fill all required inputs.'
    #     return render(request, 'information.html', context)

    try:
        schedule = Schedule.objects.get(id=context['schedule'])
        schedule.assignee = request.user.username
        schedule.info_name = context['name']
        schedule.info_contact_number = context['info_contact_number']
        schedule.info_id = context['idno']
        schedule.info_college = context['college']
        schedule.info_yrcourse = context['yrcourse']
        schedule.info_studentyear = context['studentyear']
        schedule.info_gender = context['gender']
        schedule.info_location = context['location']
        schedule.save()
        print(schedule)
        notif = Notification(sourceUser=request.user, destUser=schedule.counselor, notifType="APPOINTMENT",
                             notifId=schedule.id, status="UNREAD", message=(schedule.info_name + " sent a request."))
        notif.save()

    except:
        return HttpResponse('Bad Request!')

    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath
    context['username'] = request.user.username

    return render(request, 'information.html', context)


def updatepseudoname(request):
    pseudoname = request.GET['changePseudoNameInput']

    if pseudoname is '':
        request.user.imgpath = UserAttrib.objects.get(
            user=request.user).imgpath
        context = {}
        context['namemessage'] = 'Invalid username.'
        context['username'] = request.user.username
        return render(request, 'settings.html', context)

    try:
        user = User.objects.get(username=request.user.username)
        user.username = pseudoname
        user.save()
    except:
        request.user.imgpath = UserAttrib.objects.get(
            user=request.user).imgpath
        context = {}
        context['namemessage'] = 'Invalid username.'
        context['username'] = request.user.username
        return render(request, 'settings.html', context)

    context = {}
    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath
    request.user.attrib = UserAttrib.objects.get(user=request.user)
    request.user.username = pseudoname
    context['success'] = 'OK'

    if request.user.is_staff:

        return render(request, 'settings_gcc.html', context)
    else:

        return render(request, 'settings.html', context)


def updatepassword(request):
    oldpassword = request.GET['oldPasswordInput']
    newpassword = request.GET['newPasswordInput']
    confirmationpassword = request.GET['retypePasswordInput']

    if oldpassword is '' or newpassword is '' or confirmationpassword is '':
        request.user.imgpath = UserAttrib.objects.get(
            user=request.user).imgpath
        context = {}
        context['passmessage'] = 'Please fill out all forms.'
        context['username'] = request.user.username
        return render(request, 'settings.html', context)

    if newpassword != confirmationpassword:
        request.user.imgpath = UserAttrib.objects.get(
            user=request.user).imgpath
        context = {}
        context['passmessage'] = 'Password did not match.'
        context['username'] = request.user.username
        return render(request, 'settings.html', context)

    user = User.objects.get(username=request.user.username)
    user = authenticate(
        request, username=request.user.username, password=oldpassword)

    if user is not None:
        user.set_password(newpassword)
        user.save()
    else:
        request.user.imgpath = UserAttrib.objects.get(
            user=request.user).imgpath
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


def gccChat(request):
    if request.user.is_authenticated:

        request.user.imgpath = UserAttrib.objects.get(
            user=request.user).imgpath

        context = {}
        context['username'] = request.user.username

        if request.user.is_staff:
            context = {}

            # Get the chat list
            chat_list = []
            messages = Message.objects.filter(receiver=request.user).order_by('-date_created')            
            for message in messages:
                user = User.objects.get(id=message.sender.id)
                if user.username not in chat_list:
                    chat_list.append(user.username)

            # combined_queryset = Message.objects.filter(receiver=request.user)
            # m = combined_queryset.values('sender').distinct()
            # x = []
            # for message in m:
            #     user = User.objects.get(id=message['sender'])
            #     try:
            #         attrib = UserAttrib.objects.get(user=user)
            #         user.imgpath = attrib.imgpath
            #     except:
            #         user.imgpath = '/media/001.png'
            #     x.append(user)

            context['chat_list'] = chat_list

            return render(request, 'gcc.html', context)


def getchatlist(request):
    context = {}

     # Get the chat list
    chat_list = []
    messages = Message.objects.filter(receiver=request.user).order_by('-date_created')            
    for message in messages:
        user = User.objects.get(id=message.sender.id)
        if user.username not in chat_list:
            chat_list.append(user.username)

    context['chat_list'] = chat_list
    
    return JsonResponse(context)

def getMessages(request):
    context = {}

    receiver = request.GET['receiver']
    user = User.objects.get(username=receiver)
    combined_queryset = Message.objects.filter(
        sender=request.user, receiver=user) | Message.objects.filter(sender=user, receiver=request.user)
    context['imgpath'] = UserAttrib.objects.get(user=user).imgpath
    print('IMGPATH: ' + context['imgpath'])
    print(combined_queryset)
    messages = combined_queryset.order_by('date_created')

    res = list(messages.values(
        'message', 'sender', 'receiver', 'date_created'))

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

    combined_queryset = Message.objects.filter(
        sender=user, receiver=request.user) | Message.objects.filter(sender=request.user, receiver=user)
    print(combined_queryset)
    messages = combined_queryset.order_by('date_created')
    print(messages)
    for message in messages:
        print(message.date_created)
    context['messages'] = messages

    return render(request, 'chat.html', context)


def appoint(request, college):

    if request.method == 'POST':
        # Popoulate Assessment
        question1 = request.POST['genderInput']
        question2 = request.POST['ageInput']
        question3 = request.POST['statusInput']
        question4 = request.POST['supportInput']
        question5 = request.POST['counselingInput']
        question6 = request.POST['healthRatingInput']
        question7 = request.POST['sleepingHabitsInput']
        question8 = request.POST['eatingRatingInput']
        question9 = request.POST['depressionInput']
        question10 = request.POST['worryingInput']
        question11 = request.POST['heartbeatsInput']

        assessment = Assessment.objects.filter(user=request.user)

        if assessment is not None and len(assessment) == 1:
            assessment = assessment[0]
            assessment.question1 = question1
            assessment.question2 = question2
            assessment.question3 = question3
            assessment.question4 = question4
            assessment.question5 = question5
            assessment.question6 = question6
            assessment.question7 = question7
            assessment.question8 = question8
            assessment.question9 = question9
            assessment.question10 = question10
            assessment.question11 = question11
            assessment.save()
        else:
            assessment = Assessment(user=request.user, question1=question1, question2=question2, question3=question3,
                                    question4=question4, question5=question5, question6=question6, question7=question7,
                                    question8=question8, question9=question9, question10=question10, question11=question11)
            assessment.save()
        

        context = {}

        request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath

        date_today = datetime.date.today()
        year_today = date_today.year
        month_today = date_today.month

        num_days = calendar.monthrange(year_today, month_today)[1]
        days = [datetime.date(year_today, month_today, day)
                for day in range(1, num_days+1)]

        context['today'] = date_today
        context['days'] = days
        context['college'] = college

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

        return render(request, 'appoint.html', context)


def appointments(request):
    context = {}

    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath

    date_today = datetime.date.today()
    year_today = date_today.year
    month_today = date_today.month

    num_days = calendar.monthrange(year_today, month_today)[1]
    days = [datetime.date(year_today, month_today, day)
            for day in range(1, num_days + 1)]

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

    doesExist = True
    try:
        sched = Schedule.objects.get(
            counselor=request.user, time=schedule, date=datetime.datetime.strptime(day, '%B %d, %Y').date())
    except:
        doesExist = False

    if not doesExist:
        sched = Schedule(counselor=request.user, time=schedule, status='AVAILABLE',
                         date=datetime.datetime.strptime(day, '%B %d, %Y').date())
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

        if scheds is None or len(scheds) == 0:
            context['scheds'] = 'None'

        else:
            print('ENTERING MAZE')

            # sort based on time schedule
            sortedSched = []
            for sched in scheds:
                sched.startTime = sched.time.split(' ')[0]

            format = '%I:%M%p'

            sortedSched = sorted(
                scheds, key=lambda sched: time.strptime(sched.startTime, format))

            # time_hours = [time.strptime(t, format) for t in sortedSched]
            # result = [time.strftime(format, h) for h in sorted(time_hours)]

            print('PRINTING RESULTS:::')
            print(sortedSched)
            context['morning_sched'] = []
            context['noon_sched'] = []

            for sched in sortedSched:

                if sched.startTime[-2:] == 'AM':
                    x = {}
                    x['sched_id'] = sched.id
                    x['sched_time'] = sched.time
                    x['sched_available'] = True if (
                        sched.status == 'AVAILABLE' and sched.assignee == '') else False
                    context['morning_sched'].append(x)
                else:
                    x = {}
                    x['sched_id'] = sched.id
                    x['sched_time'] = sched.time
                    x['sched_available'] = True if (
                        sched.status == 'AVAILABLE' and sched.assignee == '') else False
                    context['noon_sched'].append(x)

            # context['scheds'] =  json.dumps(sortedSched)
            # for sched in scheds:
            #     if sched.time == '8:00AM - 9:00AM':
            #         context['0'] = True if (
            #             sched.status == 'AVAILABLE' and sched.assignee == '') else False
            #         context['id0'] = sched.id
            #     elif sched.time == '9:00AM - 10:00AM':
            #         context['1'] = True if sched.status == 'AVAILABLE' and sched.assignee == '' else False
            #         context['id1'] = sched.id
            #     elif sched.time == '10:00AM - 11:00AM':
            #         context['2'] = True if sched.status == 'AVAILABLE' and sched.assignee == '' else False
            #         context['id2'] = sched.id
            #     elif sched.time == '11:00AM - 12:00PM':
            #         context['3'] = True if sched.status == 'AVAILABLE' and sched.assignee == '' else False
            #         context['id3'] = sched.id
            #     elif sched.time == '1:00PM - 2:00PM':
            #         context['4'] = True if sched.status == 'AVAILABLE' and sched.assignee == '' else False
            #         context['id4'] = sched.id
            #     elif sched.time == '2:00PM - 3:00PM':
            #         context['5'] = True if sched.status == 'AVAILABLE' and sched.assignee == '' else False
            #         context['id5'] = sched.id
            #     elif sched.time == '3:00PM - 4:00PM':
            #         context['6'] = True if sched.status == 'AVAILABLE' and sched.assignee == '' else False
            #         context['id6'] = sched.id
            #     elif sched.time == '4:00PM - 5:00PM':
            #         context['7'] = True if sched.status == 'AVAILABLE' and sched.assignee == '' else False
            #         context['id7'] = sched.id

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

    if scheds is None or len(scheds) == 0:
        timeList  = ['8:00AM - 9:00AM', '9:00AM - 10:00AM', '10:00AM - 11:00AM', '11:00AM - 12:00PM', '1:00PM - 2:00PM', '2:00PM - 3:00PM', '3:00PM - 4:00PM', '5:00PM - 6:00PM']

        for t in timeList:
            Schedule(counselor=counselor, date=sched, time=t, status='NOT_AVAILABLE').save()

    scheds = Schedule.objects.filter(counselor=counselor, date=sched)

    # sort based on time schedule
    sortedSched = []
    for sched in scheds:
        sched.startTime = sched.time.split(' ')[0]

    format = '%I:%M%p'

    sortedSched = sorted(scheds, key=lambda sched: time.strptime(sched.startTime, format))

    # time_hours = [time.strptime(t, format) for t in sortedSched]
    # result = [time.strftime(format, h) for h in sorted(time_hours)]

    print('PRINTING RESULTS:::')
    print(sortedSched)
    context['morning_sched'] = []
    context['noon_sched'] = []

    for sched in sortedSched:
        if sched.startTime[-2:] == 'AM':
            x = {}
            x['sched_id'] = sched.id
            x['sched_time'] = sched.time
            x['sched_available'] = True if (
            sched.status == 'AVAILABLE') else False
            context['morning_sched'].append(x)
        else:
            x = {}
            x['sched_id'] = sched.id
            x['sched_time'] = sched.time
            x['sched_available'] = True if (
            sched.status == 'AVAILABLE') else False
            context['noon_sched'].append(x)

    return JsonResponse(context)


def setGccAppointmentSchedule(request):

    context = {}

    date_str = request.GET['day']
    sched = datetime.datetime.strptime(date_str, '%B %d, %Y').date()
    context['sched'] = sched

    context['time'] = request.GET['sched']

    schedule = None

    try:
        schedule = Schedule.objects.get(
            counselor=request.user, date=context['sched'], time=context['time'])
    except:
        schedule = Schedule(
            counselor=request.user, date=context['sched'], time=context['time'], status='NOT_AVAILABLE')
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
        context['first_name'] = request.POST['first_name']
        context['last_name'] = request.POST['last_name']
        context['degree'] = request.POST['degree']
        context['birthdate'] = request.POST['birthdate']
        context['address'] = request.POST['address']

        request.user.first_name = context['first_name']
        request.user.last_name = context['last_name']
        request.user.save()

        attrib = UserAttrib.objects.get(user=request.user)
        attrib.course = context['degree']
        attrib.birthday = context['birthdate']
        attrib.location = context['address']
        attrib.save()

        request.user.imgpath = UserAttrib.objects.get(
            user=request.user).imgpath
        request.user.attrib = UserAttrib.objects.get(user=request.user)
        context['username'] = request.user.username
        context['success'] = True
        if request.user.is_staff:

            return render(request, 'settings_gcc.html', context)


def notifications(request):
    context = {}

    notifs = list(Notification.objects.filter(destUser=request.user,
                                              status='UNREAD').order_by('-date_created').values())
    print(notifs)
    context['notifs'] = notifs
    context['len'] = len(notifs)

    return JsonResponse(context)


def requests(request):
    context = {}

    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath

    if request.user.is_staff:
        notifs = Notification.objects.filter(
            destUser=request.user, status='UNREAD', notifType='APPOINTMENT').order_by('-date_created')
    else:
        notifs = Notification.objects.filter(
            destUser=request.user, notifType='APPOINTMENT').order_by('-date_created')

    context['notifs'] = []
    for notif in notifs:
        print(notif)
        notif.fromUser = User.objects.get(id=notif.sourceUser.id).username
        context['notifs'].append(notif)

    context['len'] = len(notifs)
    context['is_staff'] = False
    if request.user.is_staff:
        context['is_staff'] = True
    else:
        for notif in notifs:
            notif.status = 'READ'
            notif.save()

    return render(request, 'requests.html', context)


def getRequest(request):
    context = {}

    notif = Notification.objects.get(id=request.GET['id'])

    print(notif.notifType)

    if notif.notifType == 'APPOINTMENT':
        sched = Schedule.objects.get(id=notif.notifId)
        context['sched_id'] = sched.id        
        context['sched_date'] = sched.date.strftime('%b %d, %Y')
        context['sched_time'] = sched.time
        context['info_name'] = sched.info_name
        context['info_contact_number'] = sched.info_contact_number
        context['info_id'] = sched.info_id
        context['info_college'] = sched.info_college
        context['info_yrcourse'] = sched.info_yrcourse
        context['info_studentyear'] = sched.info_studentyear
        context['info_gender'] = sched.info_gender
        context['info_location'] = sched.info_location
    print(context)
    return JsonResponse(context)


def approverequest(request):

    context = {}

    sched = Schedule.objects.get(id=request.GET['sched_id'])

    sched.approved = 'APPROVED'
    sched.save()

    notif = Notification.objects.get(id=request.GET['request_id'])
    notif.status = 'READ'
    notif.save()

    notif = Notification(sourceUser=request.user, destUser=notif.sourceUser, notifType="APPOINTMENT",
                         notifId=sched.id, status="UNREAD", message=('Appointment with ' + request.user.get_full_name() + ' approved.'))
    notif.save()

    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath

    notifs = list(Notification.objects.filter(destUser=request.user, status='UNREAD',
                                              notifType='APPOINTMENT').order_by('-date_created').values())

    context['notifs'] = notifs
    context['len'] = len(notifs)

    context['approved'] = True

    if request.user.is_staff:
        context['is_staff'] = True

    return render(request, 'requests.html', context)


def declinerequest(request):

    print('declinerequest()')

    context = {}

    info_reason = request.GET['info_reason']

    sched = Schedule.objects.get(id=request.GET['sched_id'])
    sched.assignee = ''
    sched.save()

    notif = Notification.objects.get(id=request.GET['request_id'])
    notif.status = 'READ'
    notif.save()

    newNotif = Notification(sourceUser=request.user, destUser=notif.sourceUser, notifType="APPOINTMENT",
                         notifId=sched.id, status="UNREAD", message=(request.user.get_full_name() + ' requested to reschedule your appointment.\nReason: ' + info_reason))
    newNotif.save()

    request.user.imgpath = UserAttrib.objects.get(user=request.user).imgpath

    notifs = list(Notification.objects.filter(destUser=request.user, status='UNREAD',
                                              notifType='APPOINTMENT').order_by('-date_created').values())

    context['notifs'] = notifs
    context['len'] = len(notifs)
    context['declined'] = True

    if request.user.is_staff:
        context['is_staff'] = True

    return redirect('/openapp/requests')
    # return render(request, 'requests.html', context)


def gccdashboard(request):

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

        # Date computations
        date_today = datetime.date.today()
        ddd = int(request.GET['ddd'])
        date_today = datetime.date(date_today.year, date_today.month, ddd)

        year_today = date_today.year
        month_today = date_today.month
        day_today = date_today.day

        num_days = calendar.monthrange(year_today, month_today)[1]
        days = [datetime.date(year_today, month_today, day)
                for day in range(1, num_days + 1)]

        w = str(days[0].weekday())
        v = str(days[-1].weekday())

        context = {}
        context['date_today'] = date_today
        context['year_today'] = year_today
        context['month_today'] = month_today
        context['day_today'] = day_today
        context['num_days'] = num_days
        context['days'] = days
        context['starting_day'] = w
        context['ending_day'] = v

        # Get appointments
        schedules = Schedule.objects.filter(
            counselor=request.user, approved='APPROVED', date=date_today)

        if schedules is None or len(schedules) == 0:
            context['scheds'] = 'None'

        else:
            print('ENTERING MAZE')

            # sort based on time schedule
            sortedSched = []
            for sched in schedules:
                sched.startTime = sched.time.split(' ')[0]

            format = '%I:%M%p'

            sortedSched = sorted(schedules, key=lambda sched: time.strptime(sched.startTime, format))
            print('PRINTING RESULTS:::')
            print(sortedSched)
            context['schedules'] = []

            for sched in sortedSched:
                x = {}
                x['sched_id'] = sched.id
                x['time'] = sched.time
                x['info_location'] = sched.info_location
                x['info_name'] = sched.info_name
                x['info_contact_number'] = sched.info_contact_number
                x['sched_available'] = True if (sched.status == 'AVAILABLE' and sched.assignee == '') else False
                context['schedules'].append(x)

        # Compute
        lead = int(w) + 1
        lag = 5 - int(v)

        dayArray = []
        for day in days:
            dayArray.append(day.day)

        for i in range(lead):
            dayArray.insert(0, -1)
        for i in range(lag):
            dayArray.append(-1)

        day_per_week = []
        dayList = []

        counter = 0
        for day in dayArray:
            if counter < 7:
                dayList.append(day)
                counter = counter + 1
            else:
                day_per_week.append(dayList)
                dayList = []
                dayList.append(day)
                counter = 1

        day_per_week.append(dayList)

        context['day_per_week'] = day_per_week

        return render(request, 'appointment.html', context)
