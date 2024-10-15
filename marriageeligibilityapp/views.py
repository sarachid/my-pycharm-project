from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'marriageeligibility.html')


def read_fun(request):
    age = int(request.POST['txtage'])
    gender = (request.POST['eligible'])

    if gender == 'Female':
        if age >= 18:
            result = 'Eligible for Marriage'
        else:
            result = "Not Eligible"
    elif gender == 'Male':
        if age >= 21:
            result = 'Eligible for Marriage'
        else:
            result = 'Not Eligible'
    else:
        result = "Please give proper integer value or gender "

    return render(request, 'marriageeligibility.html', {'age': age, 'res': result})
