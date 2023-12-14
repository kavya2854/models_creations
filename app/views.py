from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def topic(request):
    QLTO = Topic.objects.all()
    d = {'topics':QLTO}
    return render(request,'Topic.html',d)

def webpage(request):
    QLWO = Webpage.objects.all()
    d = {'webpages':QLWO}
    return render(request,'webpage.html',d)

def accessrecord(request):
    QLARO = AccessRecord.objects.all()
    d = {'accessrecords':QLARO}
    return render(request,'accessrecord.html',d)

def insert_topic(request):
    tn = input('Enter topicname : ')
    NTO = Topic.objects.get_or_create(topic_name = tn)[0]
    NTO.save()
    return HttpResponse('Topic is Created')

def insert_webpage(request):
    tn = input('Enter topicname : ')
    n = input('Enter name : ')
    u = input('Enter url: ')
    TO = Topic.objects.get(topic_name = tn)
    NWO = Webpage.objects.get_or_create(topic_name = TO,name = n,url = u)[0]
    NWO.save()
    return HttpResponse('Webpage is created')

def insert_accessrecord(request):
    pk = int(input('Enter pk : '))
    d = input('Enter date : ')
    a = input('Enter author name : ')
    WO = Webpage.objects.get(pk = pk)
    NARO = AccessRecord.objects.get_or_create(name = WO,date = d,author = a)[0]
    NARO.save()
    return HttpResponse('AccessRecord is Created')



