from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'yeardetection.html')


def year_fun(request):
    year=int(request.POST['txtyear'])
    if (year %4 ==0 and year % 100 !=0) or (year % 400 ==0):
        result="Leap year"
    else:
        result='Not a leap year'
    return render(request,'yeardetection.html',{"year" : year,"res":result})
