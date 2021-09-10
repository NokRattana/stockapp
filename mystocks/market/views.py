from django.shortcuts import render

def stocks_temp(request):
    return render(request, 'stocks_temp.html', {})



def about_temp(request):
    
    import requests
    import json


    api_request = requests.get("")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."



    return render(request, 'blog_temp.html', {'api': api})

# Api key here.
