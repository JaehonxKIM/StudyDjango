import pandas as pd 
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from pandasapp.df.melon.melon_df import getDf_Melon

def melon(request) :
    df = pd.DataFrame()
    df["mem_id"]    = ["a001", "b001", "c001"]
    df["mem_pass"]  = ["a001pwd", "b001pwd", "c001pwd"]
    df["mem_name"]  = ["홍길동", "춘향이", "길동이"]
    
    # DataFrame 데이터의 행과 열을 
    # HTML의 Table 형태로 변환하기
    context = {"df" : df.to_html()}
    
    return render(
        request, 'pandasapp/melon.html', context
    )
    
def melon_df(request) :
    df = getDf_Melon()
    
    context = {"df" : df.to_html()}
    
    return render(
        request, 'pandasapp/melon_df.html', context
    )    