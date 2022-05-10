import json
# import psycopg2
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from userregistration.models import UserAuthentication
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.
# def createuser(request):
#     return HttpResponse("Create User!")

#function to create user
@csrf_exempt
def createuser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        status = "ACTIVE"
        result = UserAuthentication(name = name, username = username, password = password, status = status)
        result.save()
    return render(request, "createuser.html")

#function to ger admin users
@csrf_exempt
def getusers(request):
    

    dataArray = []
    userData = UserAuthentication.objects.values()

    for i in range(0, len(userData)):
        dataArray.append([userData[i]['name'],userData[i]['username'],userData[i]['password']])

    return JsonResponse({'data': dataArray})
