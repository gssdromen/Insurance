# coding:utf-8

import os

from django.http import HttpResponse
from django.shortcuts import render_to_response

from InsuranceItem.models import InsuranceItem

# Create your views here.
def detail(request, applyNum):
    insurance = InsuranceItem.objects.filter(apply_num=applyNum)
    print insurance.apply_num
    return render_to_response('detail.html', {'insurance':insurance[0]})
    # return render_to_response('index.html')

def index(request):
    insurances = InsuranceItem.objects.all()
    if 'start' in request.GET:
        start = request.GET['start']
    if 'end' in request.GET:
        end = request.GET['end']
    return render_to_response('index.html', {'insurances':insurances})

def add(request):
    apply_num = request.POST.get('apply_num')
    name = request.POST.get('name')
    dealer_name = request.POST.get('dealer_name')
    payback_status = request.POST.get('payback_status')
    from_where = request.POST.get('from_where')
    is_overdue = request.POST.get('is_overdue')
    is_done = request.POST.get('is_done')
    is_clean = request.POST.get('is_clean')
    apply_date = request.POST.get('apply_date')
    update_date = request.POST.get('update_date')
    last_status = request.POST.get('last_status')
    watching_flag = request.POST.get('watching_flag')
