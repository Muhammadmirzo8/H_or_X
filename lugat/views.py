from django.shortcuts import render
from .models import * 


def index(request):
   return render(request, "lugat\index.html")

def search(request): 
   html = request.GET.get("soz").lower()
   if Soz.objects.filter(correct=html): 
      soz = Soz.objects.filter(correct=html)
      nsoz = nosoz.objects.filter(soz_id=soz[0].id) 
      return render(request, "lugat\search.html", {"t_soz": soz[0].correct , "nsoz": nsoz})    
   elif nosoz.objects.filter(wrong=html): 
      ww = nosoz.objects.filter(wrong=html)
      cw = Soz.objects.filter(correct=ww[0].soz_id) 
      ww = nosoz.objects.filter(soz_id=cw[0].id)
      return render(request, "lugat\search.html", {"nsoz": ww , "t_soz": cw[0].correct})  
   else: 
       a = "Bazada bunday so'z yo'q!!!" 
       return render(request, "lugat\search.html", {"t_soz": a})  
