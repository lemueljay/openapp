from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

import json

from django.contrib.auth.models import User
from .models import Code, UserAttrib, Message

from .utils import CodeGenerator

"""
Default index handler.
"""
def index(request):

    if request.user.is_authenticated:
        context = {}
        context['username'] = request.user.username
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
                user = User.objects.create_user(username=username)
                user.set_password(password)
                user.is_staff = False
                user.active = True
                user.save()

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

"""

"""
def logoutUser(request):

    logout(request)
    return redirect('/openapp/login')


def collegeprofile(request, college):

    context = {}
    context['college'] = college

    if request.user.is_authenticated:
        # Get councilor for college
        try:
            user = User.objects.get(username__icontains=college)
            userAttrib = UserAttrib.objects.get(user=user)

            if user is not None:
                context['user'] = user
                context['firstname'] = user.first_name
                context['lastname'] = user.last_name
                context['imgpath'] = userAttrib.imgpath
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
        fromUser = request.user
        toUser = User.objects.get(username=request.POST.get('college', ''))
        message = request.POST.get('message', '')

        message = Message(fromUser=fromUser, toUser=toUser, message=message)
        message.save()

        return JsonResponse(context)


def collegechat(request, college):
    context = {}

    user = User.objects.get(username__icontains=college)
    userAttrib = UserAttrib.objects.get(user=user)
    context['imgpath'] = userAttrib.imgpath
    context['college'] = college

    outgoingmessages = Message.objects.filter(fromUser=request.user, toUser=user)
    ingoingmessages = Message.objects.filter(fromUser=user, toUser=request.user)

    context['outgoingmessages'] = outgoingmessages
    context['ingoingmessages'] = ingoingmessages

    return render(request, 'chat.html', context)


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


