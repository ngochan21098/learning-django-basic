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
from django.forms.models import model_to_dict

# Create your views here.

@api_view(["POST"])
def create_user(req):
    # data = json.loads(req.body) -> Không cần do api_view đã parse data sang dictionary
    data = req.data

    # user = User(name = data['name'], age = data['age'], salary = data['salary'], hometown = data['hometown'])
    # user.save()

    ser = UserSerialize(data = data)
    # #is_valid để check xem data truyền lên có valid hay không
    if not ser.is_valid():  
        #.errors để in ra các lỗi mà framework hỗ trợ
        return Response(ser.errors, status=400) 
    
    # print("ser")

    ser.save() # => True

    return Response(ser.data)

    return HttpResponse('OK')

@api_view(["PUT"])
def update_user(req):

    # print("name", name)

    data = req.data
    user = User.objects.get(name=data.get('name'))

    # Update user using serializer.
    ser = UserSerialize(user, data=data)

    ser.is_valid(raise_exception=True)

    # if not ser.is_valid():
    #     return HttpResponse('Error', status=400)
    ser.save()

    # for user in user_name: 
    #     user = User(name = data['name'], age = data['age'], salary = data['salary'], hometown = data['hometown'])
    #     user.save()

    return Response(ser.data)

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

    app_user = Application.objects.get(apl_no=1)
    print(app_user)

    data = req.data
    user_name = data.get('user_name')
    user = User.objects.get(name=user_name)

    app = Application.objects.last()
    if not app:
        apl_no_new = 1
    else:
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
    except Exception as e:
        print(e)
        return Response("Can not find user", status = 404)
    
@api_view(["DELETE"])
def deleting_user(req, name):
    user_name = User.objects.filter(name = name) 
    for username in user_name: 
            username.delete()
    return Response("OK")

# @api_view(["PUT"])
# def update_user(req, name):
#     data = req.data
#     user_name = User.objects.get(name = name)

#     user_name.age = data['age']
#     user_name.salary = data['salary']
#     user_name.hometown = data['hometown']

#     user_name.save()

#     # name = models.CharField(primary_key=True, max_length=20)
#     # age = models.SmallIntegerField()
#     # salary = models.BigIntegerField()
#     # hometown = models.CharField(max_length=20)


#     # for username in user_name: 
#     #     username.delete()
#     return Response("OK")
