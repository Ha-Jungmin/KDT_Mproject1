from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    #return HttpResponse("Hello World!")
    name = "하정민"
    age = 25
    interest_area = "A.I."
    hobby = "Watch Youtube, movie and baseball"
    return render(request, 'index.html', {'my_name': name, 'my_age' : age, 'my_interest_area' : interest_area, 'my_hobby' : hobby})