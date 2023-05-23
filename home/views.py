from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):

    peoples = [
        {'name':'abhijeet', 'age':26},
        {'name':'Rohan', 'age':13},
        {'name':'Vicky', 'age':27},
        {'name':'Depanshu', 'age':17},
        {'name':'Sandeep', 'age':50},
    ]


    vegetables = ['Pumpkin','Tomato', 'Potatoe' ]

    text ='''
      Lorem ipsum dolor sit amet consectetur, adipisicing elit. Veniam aperiam at atque vel ex accusantium adipisci, eaque fugit. Maiores cumque minus deleniti iure repellat? Esse quos id alias distinctio optio!
      '''
    
    return render(request, "index.html", context = {'page': 'Django Practice', 'peoples' : peoples, 'text': text, 'vegetables':vegetables})


def about(request):
    context = {'page': 'About'}
    return render(request, "about.html", context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "contact.html", context)

def success_pages(request):
    return HttpResponse("<h1>Hey, this is a success page</h1>")
    

