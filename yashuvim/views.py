from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Yashuv


def index(request):
     yashuvim = Yashuv.objects.order_by('id')

     paginator = Paginator(yashuvim,34)
     page = request.GET.get('page')
     paged_yashuvim = paginator.get_page(page)

     context = {
          'yashuvim' : paged_yashuvim }  
      
     return render(request,'yashuvim/yashuvim.html',context)

    

def yashuv(request ,yashuv_id): 
     yashuv = get_object_or_404(Yashuv,pk=yashuv_id)

     context = {
          'Yashuv' : Yashuv } 

     return render(request,'yashuvim/yashuv.html',context)



def search(request):
     return render(request,'yashuvim/search.html')


