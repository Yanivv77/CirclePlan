from django.shortcuts import get_object_or_404, render

from attendance.models import Member

def profile(request ,member_id): 
     member = get_object_or_404(Member,pk=member_id)

     context = {
          'member' : member } 


     return render(request,'members/member.html',context)
