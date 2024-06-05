from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url).json()
    joke = response['value']
    return render(request,'index.html',context={'text':joke})
