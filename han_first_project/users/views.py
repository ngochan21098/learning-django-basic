from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket, Application, User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods 
import json 
from rest_framework.decorators import api_view
from rest_framework.response import Response #Import để dùng được các response mà fw hỗ trợ
from .serializers import UserSerialize

# Create your views here.

@api_view(["POST"])
def create_user(req):
    # data = json.loads(req.body) -> Không cần do api_view đã parse data sang dictionary
    data = req.data
    # user = User(name = data['name'], age = data['age'], salary = data['salary'], hometown = data['hometown'])
    # user.save()
    ser = UserSerialize(data = data)
    #is_valid để check xem data truyền lên có valid hay không
    if not ser.is_valid():  
        #.errors để in ra các lỗi mà framework hỗ trợ
        return Response(ser.errors, status=400) 
    

    return HttpResponse('OK')

@csrf_exempt 
@require_http_methods(["PUT"])
def update_user(req):
    data = json.loads(req.body)
    name = data.get('name')
    user_name = User.objects.filter(name=name)
    for user in user_name: 
        user = User(name = data['name'], age = data['age'], salary = data['salary'], hometown = data['hometown'])
        user.save()

    return HttpResponse('OK')

@csrf_exempt 
@require_http_methods(["DELETE"])
def delete_user(req):
    data = json.loads(req.body)
    name = data.get('name')
    user_name = User.objects.filter(name=name)
    for user in user_name: 
        user.delete()

    return HttpResponse('OK')

@csrf_exempt 
@require_http_methods(["POST"])
def application_create(req):
    ##app = Application(apl_no = 1, user_id = 'Han')
    ##app = Application(apl_no = 2, user = user)
    # print('-------------------')
    # print(req.method)
    # print(req.body)
    data = json.loads(req.body)
    user_name = data.get('user_name')
    user = User.objects.get(name=user_name)

    app = Application.objects.last()
    apl_no_new = app.apl_no + 1

    app = Application(user = user, apl_no = apl_no_new)
    
    # print(user.__dict__)
    app.save()
    return HttpResponse('OK')

def ticket_create(req):
    ticket = Ticket(ticket_no = 1, apl_no = 1)
    ticket.save()

    return HttpResponse('OK')
