from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django import template
from attendance.models import Meeting, Participation, Circle




def index(request):
     circles = Circle.objects.all()

     paginator = Paginator(circles,10)
     page = request.GET.get('page')
     paged_circles = paginator.get_page(page)

     context = {
          'circles' : paged_circles }  
      
     return render(request,'./templates/accounts/dashboard.html',context)


def circle(request ,circle_id): 
     circle = get_object_or_404(Circle,pk=circle_id)
     meetings = Meeting.objects.all()
     


     context = {
          'circle' : circle,
          'meetings' : meetings } 

     return render(request,'./templates/circles/circle.html',context)
     

def meeting(request ,circle_id,meeting_id): 
     circle = get_object_or_404(Circle,pk=circle_id)
     meeting = get_object_or_404(Meeting,pk=meeting_id)
     participations = Participation.objects.all()
     
     context = {
          'circle' : circle,
          'participation' : participations,
          'meeting' : meeting } 

     return render(request,'./templates/circles/meeting.html',context)





register = template.Library()
@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()






