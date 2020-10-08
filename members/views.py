from django.shortcuts import get_object_or_404, render

from attendance.models import Circle, Meeting, Member

def profile(request ,member_id,): 
     member = get_object_or_404(Member,pk=member_id)
     context = {
          'member' : member,
  }
      
     return render(request,'./templates/members/member.html',context)

