# coding:utf-8

import os

from django.http import HttpResponse
from django.shortcuts import render_to_response

from datetime import date
import utils

from InsuranceItem.models import InsuranceItem

# Create your views here.
def detail(request, applyNum):
    if applyNum:
        insurance = InsuranceItem.objects.get(apply_num=applyNum)
        print insurance.apply_num
        return render_to_response('detail.html', {'insurance':insurance})

def newone(request):
    isNew = request.GET.get('is_new', '')
    return render_to_response('detail.html', {'is_new': isNew})

def index(request):
    insurances = InsuranceItem.objects.all()
    if 'start_date' in request.GET:
        start = request.GET['start_date']
    if 'end_date' in request.GET:
        end = request.GET['end_date']
    return render_to_response('index.html', {'insurances':insurances})

def search(request):
    filteredInsurances = []
    start = request.GET.get('start_date', '')
    end = request.GET.get('end_date', '')
    startDate = utils.getDateFromString(start)
    endDate = utils.getDateFromString(end)
    insurances = InsuranceItem.objects.all()
    print insurances
    return render_to_response('index.html', {'insurances':insurances})

def add(request):
    apply_num = request.POST.get('apply_num', '')
    name = request.POST.get('name', '')
    dealer_name = request.POST.get('dealer_name', '')
    payback_status = request.POST.get('payback_status', '')
    from_where = request.POST.get('from_where', '')
    is_overdue = request.POST.get('is_overdue', '')
    is_done = request.POST.get('is_done', '')
    is_clean = request.POST.get('is_clean', '')
    update_date = request.POST.get('update_date', '')
    last_status = request.POST.get('last_status', '')
    watching_flag = request.POST.get('watching_flag', '')
    insurance = InsuranceItem(apply_num=apply_num,name=name,dealer_name=dealer_name,payback_status=payback_status,from_where=from_where,is_overdue=is_overdue,is_done=is_done,is_clean=is_clean,last_status=last_status,watching_flag=watching_flag)
    insurance.save()
    return HttpResponse(u'保存成功')

def update(request):
    print request.POST
    apply_num = request.POST.get('apply_num', '')
    name = request.POST.get('name', '')
    dealer_name = request.POST.get('dealer_name', '')
    payback_status = request.POST.get('payback_status', '')
    from_where = request.POST.get('from_where', '')
    is_overdue = request.POST.get('is_overdue', '')
    is_done = request.POST.get('is_done', '')
    is_clean = request.POST.get('is_clean', '')
    update_date = request.POST.get('update_date', '')
    last_status = request.POST.get('last_status', '')
    watching_flag = request.POST.get('watching_flag', '')
    print apply_num
    if apply_num == '':
        return HttpResponse(u'请填写申请编号')
    insurance = InsuranceItem.objects.get(apply_num=apply_num)
    insurance.name = name
    insurance.dealer_name = dealer_name
    insurance.payback_status = payback_status
    insurance.from_where = from_where
    insurance.is_overdue = is_overdue
    insurance.is_done = is_done
    insurance.is_clean = is_clean
    insurance.last_status = last_status
    insurance.update_date = update_date
    insurance.save()
    return HttpResponse(u'保存成功')
