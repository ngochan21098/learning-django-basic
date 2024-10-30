from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket, Application, User, Traveller, Member
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods 
import json 
from rest_framework.decorators import api_view
from rest_framework.response import Response #Import để dùng được các response mà fw hỗ trợ
from .serializers import UserSerialize
from django.forms.models import model_to_dict

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
    
    ser.save()
    return HttpResponse('OK')

@api_view(["PUT"])
def update_user(req):
    data = req.data
    name = data.get('name')
    user_name = User.objects.filter(name=name)
    for user in user_name: 
        user = User(name = data['name'], age = data['age'], salary = data['salary'], hometown = data['hometown'])
        user.save()

    return HttpResponse('OK')

@api_view(["DELETE"])
def delete_user(req):
    data = req.data
    name = data.get('name')
    user_name = User.objects.filter(name=name)
    for user in user_name: 
        user.delete()

    return HttpResponse('OK')

@api_view(["POST"])
def application_create(req):
    ##app = Application(apl_no = 1, user_id = 'Han')
    ##app = Application(apl_no = 2, user = user)
    # print('-------------------')
    # print(req.method)
    # print(req.body)
    data = req.data
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

@api_view(["GET"])
def listing_user(req, name):
    try:
        user = User.objects.get(name = name) 
        serializer = UserSerialize(user)
        return Response(serializer.data)
    except:
        return Response("Can not find user", status = 404)
    
@api_view(["DELETE"])
def deleting_user(req, name):
        user_name = User.objects.filter(name = name) 
        for username in user_name: 
             username.delete()
        return Response("OK")

@api_view(["PUT"])
def updating_user(req, name):
        data = req.data
        user = User.objects.get(name = name) 
        user.age = data['age']
        user.salary = data['salary']
        user.hometown = data['hometown']
        user.save()
        return Response("OK")

@api_view(["POST"])
def creating_user(req):
        data = req.data
        serialize= UserSerialize(data = data)
        if not serialize.is_valid():
            return Response(serialize.errors, status = 400)
        if serialize:
            return Response('User already exists')
        serialize.save()

        return Response(serialize.data)
        

@api_view(["POST"])
def traveller_create(req):
    data = req.data
    member = Member.objects.get(mem_no = data['mem_no'])
    app = Application.objects.get(apl_no = data['apl_no'])
    tvl_no = Traveller.objects.last()
    tvlno_new = tvl_no.traveller_no + 1
    traveller = Traveller(traveller_no = tvlno_new, mem_no = member['mem_no'], apl_no = app['apl_no'], mem_birth = data['mem_birth'], mem_status = data['mem_status'], mem_name = data['mem_name'])
    traveller.save()
    return Response("OK")
