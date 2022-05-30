from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from joblib import load
model=load('./model/model.pk1')

# Create your views here.
def index(request):
    context={}
    return render(request,'firstpage/index.html',context)

def predictSent(request):
    context={}
    if request.method=='POST':
        #context['p1']=request.POST.get('p1')
        p1=request.POST.get('p1')
        context['result']=model.predict([p1])
        context['p1']=request.POST.get('p1')
    return render(request,'firstpage/result.html',context)