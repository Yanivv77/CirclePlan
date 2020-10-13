from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django import template
from rest_framework.decorators import action
from attendance.models import Circle, Meeting, Member, Participation
from rest_framework.viewsets import ModelViewSet
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpRequest
from rest_framework.request import Request
from django.http import HttpResponseRedirect, request
from django.contrib.auth.decorators import login_required
from .serializers import (CircleSerializer, MemberSerializer,
                          MeetingTableSerializer, SimpleCircleSerializer,
                          MeetingSerializer, ParticipationSerializer,)
import re
from django.contrib import messages

def index(request):
     circles = Circle.objects.order_by('created').filter(is_active = True)
     

     context = {
          'circles' : circles }
     return render(request,'./templates/circles/circles.html',context)


def circle(request ,circle_id):
     circle = get_object_or_404(Circle.objects.order_by('created'),pk=circle_id)
     meetings = Meeting.objects.order_by('date_time')
     context = {
          'circle' : circle,
          'meetings' : meetings }

     return render(request,'./templates/circles/circle.html',context)


def meeting(request ,circle_id,meeting_id,):
     circle = get_object_or_404(Circle,pk=circle_id)
     meeting = get_object_or_404(Meeting,pk=meeting_id)
     participations = Participation.objects.order_by('id')
    
     context = {
          'circle' : circle,
          'participations' : participations,
          'meeting' : meeting }
     return render(request,'./templates/circles/meeting.html',context)


class CircleViewSet(ModelViewSet):

    queryset = Circle.objects.all()
    serializer_class = SimpleCircleSerializer

class MeetingViewSet(ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer



    @action(detail=True)
    def participation(self, request, pk=None):
        meeting = self.get_object()
        participations = meeting.participations.all()
        participation_serializer = ParticipationSerializer(participations,
                                                           many=True)
        data = {
            'participations': participation_serializer.data,

        }

        return Response(data)

    @action(detail=True, methods=['post'],)
    def att(self, request, *args, **kwargs):
        meeting = self.get_object()
        data = request.data

        for p in data:
            if 'participation_' in p:
                participation = Participation.objects.get(id=int(re.sub('participation_','',p)))
                participation.attended = True if data[p] == 'true' else False
                participation.save()

            if 'absence_reason_' in p:
                participation = Participation.objects.get(id=int(re.sub('absence_reason_','',p)))
                participation.absence_reason = data[p]
                participation.save()   

        meeting.save()
        messages.success(request,'נוכחות נשמרה בהצלחה')

        return Response()
