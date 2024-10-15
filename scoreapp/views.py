from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'scorevalidation.html')


def read_fun(request):
    name=request.POST["txtname1"]
    n1=int(request.POST["txtpython"])
    n2=int(request.POST["txtjava"])
    n3=int(request.POST["txtmsql"])
    n4=int(request.POST["txthtml"])
    n5=int(request.POST["txtdjango"])
    operation = request.POST["operation"]
    if operation=='Total':
        result=n1+n2+n3+n4+n5
    elif operation=='Percentage':
        percentage=(n1+n2+n3+n4+n5)/500*100
        result=percentage
    elif operation=='Grade':
        percentage = (n1 + n2 + n3 + n4 + n5 )/500 * 100
        if percentage>90:
            result='A'
        elif 80<percentage<=90:
            result='B'
        elif 70<percentage<=80:
            result='C'
        elif 60<percentage<=70:
            result='D'
        elif 50<percentage<=60:
            result='E'
        elif percentage<=50:
            result='F'
    elif operation=='Status':
            percentage = (n1 + n2 + n3 + n4 + n5) / 500 * 100
            if percentage>50:
                result='Pass'
            else:
                result='Fail'
    return render(request,'scorevalidation.html',{"name": name,"n1":n1,"n2":n2,"n3":n3,"n4":n4,"n5":n5,"res": result})
