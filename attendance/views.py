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
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .serializers import (CircleSerializer, MemberSerializer,
                          MeetingTableSerializer, SimpleCircleSerializer,
                          MeetingSerializer, ParticipationSerializer,)
import re

def index(request):
     circles = Circle.objects.all()
     paginator = Paginator(circles,10)
     page = request.GET.get('page')
     paged_circles = paginator.get_page(page)
     context = {
          'circles' : paged_circles }
     return render(request,'./templates/circles/circles.html',context)


def circle(request ,circle_id):
     circle = get_object_or_404(Circle,pk=circle_id)
     meetings = Meeting.objects.all()
     context = {
          'circle' : circle,
          'meetings' : meetings }
     return render(request,'./templates/circles/circle.html',context)


def meeting(request ,circle_id,meeting_id,):
     circle = get_object_or_404(Circle,pk=circle_id)
     meeting = get_object_or_404(Meeting,pk=meeting_id)
     participations = Participation.objects.all()
     circlee = Circle.objects.all()
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

        meeting.save()

        return Response()
