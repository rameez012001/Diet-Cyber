from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import pandas as pd
from django.urls import reverse
from .models import fdata,rcal


def temp(x):
  return loader.get_template(x)

def index(request):
  #to load the html template
  template = temp('index.html')

  #loading csv file ans setting index of it
  df=pd.read_csv(r'ctapp\csv\foodchart.csv')
  df1=pd.read_csv(r'ctapp\csv\wcal.csv')
  findex=df.set_index('Food')
  Windex=df1.set_index('weight')
  
  #to get the food by user's input and it fetch data from csv file
  if request.GET.get('food'):
    q= request.GET['food']
    qty= request.GET['quantity']
    x1=findex.loc[q,'Calories']
    x11=int(qty)*int(x1)#for quantity purpose
    x2=findex.loc[q,'Protein']
    x22=int(qty)*float(x2)#for quantity purpose
    x3=findex.loc[q,'Fat']
    x33=int(qty)*float(x3)#for quantity purpose
    x4=findex.loc[q,'Carbs']
    x44=int(qty)*float(x4)#for quantity purpose
    a = fdata(food=q,quantity = qty,calories=x11,protein=x22,fat=x33,carbs=x44)
    a.save()
  else:
      False 


  if request.GET.get('rcal'):
    rcal1= request.GET['rcal']
    we = int(rcal1)
    qq=Windex.loc[we,'netcalories']
    b = rcal(rcal = qq)
    b.save()

  #to access fdata in model.Model.
  data = fdata.objects.all().values()#food column
  item= fdata.objects.all()
  totcal = sum(item.values_list('calories', flat=True))#total calories
  totpro = sum(item.values_list('protein', flat=True))#total protein
  totfat = sum(item.values_list('fat', flat=True))#total fat
  totcarbs = sum(item.values_list('carbs', flat=True))

  cal1 = rcal.objects.all().values()

  context = {
    'fdata': data,
    'req':cal1,
    'cal':totcal,
    'pro':totpro,
    'fat':format(totfat,".1f"),
    'carbs':format(totcarbs,".1f")
  }
  return HttpResponse(template.render(context, request)) 

#to delete all food items present in the table
def deleteall(request):
  fdata.objects.all().delete()
  rcal.objects.all().delete()
  return HttpResponseRedirect(reverse('index'))

#to delete single item
def delete(request, id):
  member = fdata.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))
  