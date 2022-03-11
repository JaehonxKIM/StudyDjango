from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from .models import Course

def main(request) :
    return HttpResponse("<u>Main</u>")

def insert(request) :
    Course(name = '데이터 분석', cnt = 30).save()
    Course(name = '데이터 수집', cnt = 20).save()
    Course(name = '웹 개발', cnt = 25).save()
    Course(name = '인공지능', cnt = 20).save()

    return HttpResponse('secondapp_course 데이터 입력 완료')
