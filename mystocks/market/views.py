from django.shortcuts import render, redirect
from .models import Snock
from .forms import SnockForm
from  django.contrib import messages

def stocks_temp(request):
    return render(request, 'stocks_temp.html', {})



def about_temp(request):
    
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker +"/quote?token=")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."



        return render(request, 'blog_temp.html', {'api': api})
    else:
        return render(request, 'blog_temp.html', {'ticker': "Enter symbol.."})




def add_mystock(request):
    if request.method == 'POST':
        form = SnockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Something Done!"))
            return redirect('add_mystock')

    else:
        




        ticker = Snock.objects.all()
        return render(request, 'add_mystock.html',{'ticker': ticker})




# Api key here.
