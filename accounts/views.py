from django.shortcuts import render , redirect
from django.contrib import messages , auth
from django.contrib.auth.models import User




def index(request):
     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = auth.authenticate(username=username,password=password)

          if user is not None:
               auth.login(request,user)
               messages.success(request,'התחברת בהצלחה')
               return redirect('/circles')

          else:
               messages.error(request,'הכנסת פריט שגוי ')
               return redirect('index')

     else:

          auth.logout(request)
          return render(request,'accounts/index.html')



def logout(request):
     if request.method == 'POST':
          auth.logout(request)
          messages.success(request,'התנתקת בהצלחה')
          return redirect('http://127.0.0.1:8000/')


def dashboard(request):
     return render(request,'accounts/dashboard.html')



def register(request):
     if request.method == 'POST':
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          username = request.POST['username']
          email = request.POST['email']
          password = request.POST['password']
          password2 = request.POST['password2']

          # Cehck if password match
          if password == password2:
               #Cehck username
               if User.objects.filter(username = username).exists():
                    messages.error(request,' שם משתמש תפוס נסה אחר')
                    return redirect('register')
               else:
                    if User.objects.filter(email = email).exists():
                         messages.error(request,'מייל תפוס נסה אחר')
                         return redirect('register')
                    else:
                         # not taken
                         user = User.objects.create_user(username=username,password=password
                         ,email=email,first_name=first_name,last_name=last_name)

                         #wtiout login after register
                         #auth.login(request,user)
                         #messages.success(request, 'Your are now logged in')
                         #return redirect('index')

                         #with login after register
                         user.save()
                         messages.success(request,'נרשמת בהצלחה')
                         return redirect('index')


          else:
               messages.error(request,'הסיסמה לא תואמת ')
               return redirect('register')
     else:
          return render(request,'accounts/register.html')
