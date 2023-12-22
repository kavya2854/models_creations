from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def topic(request):
    QLTO = Topic.objects.all()
    QLTO = Topic.objects.all().order_by('topic_name')
    QLTO = Topic.objects.all().order_by('-topic_name')
    QLTO = Topic.objects.all().order_by(Length('topic_name'))
    QLTO = Topic.objects.all().order_by(Length('topic_name').desc())
    d = {'topics':QLTO}
    return render(request,'Topic.html',d)

def webpage(request):
    QLWO = Webpage.objects.all()
    QLWO = Webpage.objects.all().order_by('name')
    QLWO = Webpage.objects.all().order_by('-name')
    QLWO = Webpage.objects.all().order_by(Length('name'))
    QLWO = Webpage.objects.all().order_by(Length('name').desc())
    QLWO = Webpage.objects.exclude(topic_name = 'Cricket').order_by(Length('name'))
    QLWO = Webpage.objects.filter(name = 'Rohit').order_by(Length('name'))
    QLWO = Webpage.objects.all()
    QLWO = Webpage.objects.filter(id__gt = 4)
    QLWO = Webpage.objects.filter(id__gte = 4)
    QLWO = Webpage.objects.filter(id__lt = 5)
    QLWO = Webpage.objects.filter(id__lte = 6)
    QLWO = Webpage.objects.filter(name__startswith = 'C')
    QLWO = Webpage.objects.filter(name__endswith = 't')
    QLWO = Webpage.objects.filter(name__contains = 'a')
    QLWO = Webpage.objects.filter(pk__in = [3,6])
    QLWO = Webpage.objects.filter(pk__in = [5,7])
    QLWO = Webpage.objects.filter(name__regex = '\w+t$')
    QLWO = Webpage.objects.all()[2:5:]
    QLWO = Webpage.objects.filter(name__regex = '\w+na$')
    QLWO = Webpage.objects.all()
    QLWO = Webpage.objects.filter(topic_name = 'Throwball',url__endswith = 'in')
    QLWO = Webpage.objects.filter(Q(topic_name = 'Basket Ball') & Q(url__endswith = 'com'))
    QLWO = Webpage.objects.filter(Q(topic_name = 'Cricket') | Q(url__endswith = 'com'))
   

    d = {'webpages':QLWO}
    return render(request,'webpage.html',d)

def accessrecord(request):
    QLARO = AccessRecord.objects.all()
    QLARO = AccessRecord.objects.filter(date__year = '2023')
    QLARO = AccessRecord.objects.filter(date__month = '12')
    QLARO = AccessRecord.objects.filter(date__day = '19')
    QLARO = AccessRecord.objects.filter(author__startswith = 'K')
    
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

def update_webpage(request):
    Webpage.objects.filter(topic_name = 'Cricket').update(name = 'Virat')
    Webpage.objects.filter(topic_name = 'Basket Ball').update(url = 'https://sidhu.in')
    Webpage.objects.filter(name = 'Teju').update(topic_name = 'Kabaddi')
    Webpage.objects.update_or_create(topic_name = 'Basket Ball',defaults = {'name':'Sharief'})
    ITO = Topic.objects.get_or_create(topic_name = 'Cricket')[0]
    ITO.save()
    Webpage.objects.update_or_create(name = 'RohitSharma',defaults = {'topic_name':ITO})
    Webpage.objects.filter(name = 'RohitSharma').update(url = 'https://rohitsharma.in')
    Webpage.objects.filter(name = 'Virat').update(url = 'https://virat.in')
    IWTO = Topic.objects.get_or_create(topic_name = 'Rugby')[0]
    IWTO.save()
    Webpage.objects.update_or_create(name = 'Richie',defaults = {'topic_name':IWTO,'url':'https://richie.in'})
    #Webpage.objects.update_or_create(name = 'Richie',defaults = {'url':'https://richie.in'})
    
    QLWO = Webpage.objects.all()
    d = {'webpages':QLWO}
    return render(request,'webpage.html',d)


def delete_webpage(request):
    Webpage.objects.filter(topic_name = 'Cricket').delete()
    #Webpage.objects.all().delete()
    QLWO = Webpage.objects.all()
    d = {'webpages':QLWO}
    return render(request,'webpage.html',d)



