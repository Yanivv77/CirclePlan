from django.db import models
from django_extensions.db.models import TitleDescriptionModel
from django_extensions.db.models import TimeStampedModel 

from yashuvim.models import Yashuv
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.validators import RegexValidator

def get_name(self):
    return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_name)




class Member(TimeStampedModel):
    full_name = models.CharField(max_length=64,blank = False)
    preferred_name = models.CharField(max_length=64, blank=True)
    id_number = models.CharField(validators=[RegexValidator(regex='^.{9}$', message='Id length has to be 9', code='nomatch',)],max_length =9,unique=True)
    GENDER_CHOICES = [('זכר', 'זכר'), ('נקבה', 'נקבה')]
    gender = models.CharField(choices=GENDER_CHOICES,max_length=4,default = "")
    date_of_birth = models.DateField(blank = False,)
    yashuv = models.ForeignKey(Yashuv, on_delete=models.CASCADE)
    phone = models.CharField(validators=[RegexValidator(regex='^.{10}$', message='Phone length has to be 10', code='nomatch',)],max_length =10,unique=True)
    email = models.EmailField(blank = True)
    allergys_to = models.CharField(max_length =200,blank = True)
    SHIRTS_CHOICES = [('10', '10'), ('12', '12'), ('14', '14'), ('16', '16'), ('18', '18'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')]
    shirt_size = models.CharField(choices=SHIRTS_CHOICES,max_length=4,default = "")
    youth_organization = models.CharField(max_length=64, blank=True)
    hobbies = models.CharField(max_length =200,blank = True)
    contact_name = models.CharField(max_length=64,blank = False, default = "")
    contact_relation = models.CharField(max_length=64,blank = False, default = "")
    contact_phone = models.CharField(max_length=64, blank = False, default = "")

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
        return self.title +  " - "  +self.instructor.first_name + " " +self.instructor.last_name + " | " +self.yashuv.name

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
    date_time =  models.DateField()
   


    def __str__(self):
        return f'{str(self.circle)} - {self.date_time}'
    

   


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
    absence_reason = models.CharField(max_length=254,blank = True)
 

  