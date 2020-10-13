from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import yasuvim_choices
from attendance.models import Circle ,Member
from attendance.models import Meeting, Participation
from asyncio.locks import Event
from django.http import request

def adminCircles(request):
     circles = Circle.objects.order_by('created').filter(is_active = True)

     paginator = Paginator(circles,5)
     page = request.GET.get('page')
     paged_circles = paginator.get_page(page)

     context = {
          'circles' : paged_circles,
          'yasuvim_choices': yasuvim_choices,
          
          }  
     return render(request,'./templates/admin_circles/circles.html',context)




def adminCircle(request ,circle_id): 
     circle = get_object_or_404(Circle.objects.order_by('created'),pk=circle_id)
     circlee = get_object_or_404(Circle,pk=circle_id)
     meetings = Meeting.objects.order_by('date_time')
     participations = Participation.objects.all()
     members = Member.objects.all()
     membersId = circle.members.values_list('id_number', flat=True)

     print(membersId)



     context = {
          'circle' : circle,
          'meetings' : meetings,
          'participations' : participations,
          'members' : members,
          'membersId' : membersId
          }

     return render(request,'admin_circles/circle.html',context)




def adminMeeting(request ,circle_id,meeting_id,):
     circle = get_object_or_404(Circle,pk=circle_id)
     meeting = get_object_or_404(Meeting,pk=meeting_id)
     participations = Participation.objects.all()
    
     context = {
          'circle' : circle,
          'participations' : participations,
          'meeting' : meeting }

     return render(request,'admin_circles/meetings.html',context)


def search(request):
     queryset_list = Circle.objects.order_by('created')

     # keywords
     if 'keywords' in request.GET:
          keywords = request.GET['keywords']
          if keywords:
               queryset_list = queryset_list.filter(title__icontains = keywords)


     # yashuv
     if 'yashuv' in request.GET:
          yashuv = request.GET['yashuv']
          if yashuv:
               queryset_list = queryset_list.filter(yashuv__name__iexact = yashuv)
               student_attending__studentclasshistory__year__exact=2011


     context = {
          'yasuvim_choices': yasuvim_choices,
          'circles' : queryset_list,
          'values' : request.GET
           
     }


     return render(request,'admin_circles/search.html',context)# Create your views here.
