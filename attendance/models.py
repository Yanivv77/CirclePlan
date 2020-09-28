from django.db import models
from django_extensions.db.models import TitleDescriptionModel
from django_extensions.db.models import TimeStampedModel 
from instructors.models import Instructor
from yashuvim.models import Yashuv
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.validators import RegexValidator

def get_name(self):
    return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_name)

class Member(TimeStampedModel):
    full_name = models.CharField(max_length=64)
    preferred_name = models.CharField(max_length=64, blank=True)
    id_number = models.CharField(validators=[RegexValidator(regex='^.{9}$', message='Length has to be 9', code='nomatch',)],max_length =9)
    yashuv = models.ForeignKey(Yashuv, on_delete=models.CASCADE)
    phone = models.CharField(max_length =200,blank = True)
    email = models.EmailField()
    allergys_to = models.CharField(max_length =200,blank = True)
    shirt_size = models.CharField(max_length=5, blank=True)
    youth_organization = models.CharField(max_length=64, blank=True)
    hobbies = models.CharField(max_length =200,blank = True)
    

    def __str__(self):
        if self.full_name:
            return self.full_name+' תז: '+self.id_number +'\n'

        return f'{self.full_name,self.id_number}'


class Circle(TimeStampedModel, TitleDescriptionModel):
    yashuv = models.ForeignKey(Yashuv, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User,limit_choices_to={'groups__name': "Instructor"}, on_delete=models.DO_NOTHING)
    
    title = models.CharField(max_length =200)
    is_active = models.BooleanField(default=True,blank=False)
    start_date = models.DateField()
    members = models.ManyToManyField(Member,
                                     related_name='circles',
                                     blank=True)

                                     

    def __str__(self):
        return self.title

    @property
    def participates(self):
        return ' , '.join(str(member.full_name) for member in self.members.all())


class Meeting(TimeStampedModel): 
    circle = models.ForeignKey(
        Circle,
        on_delete=models.CASCADE,
        related_name="meetings",
        related_query_name="meeting",
    )
    date_time = models.DateTimeField()
    description = models.TextField(blank=True)

    @property
    def __localtime(self):
        return timezone.localtime(self.date_time)

    @property
    def date(self):
        return self.__localtime.strftime('%Y-%m-%d')

    @property
    def time(self):
        return self.__localtime.strftime('%H:%M')

    def __str__(self):
        return f'{str(self.circle)} meeting on {self.date} at {self.time}'


class Participation(TimeStampedModel):
    meeting = models.ForeignKey(
        Meeting,
        on_delete=models.CASCADE,
        related_name="participations",
        related_query_name="participation",
    )
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="participations",
        related_query_name="participation",
    )
    attended = models.BooleanField(default=False)
 

  