from django.http import JsonResponse
from django.shortcuts import render
import requests
import random

def home(request):
    return render(request, 'templates/home.html')

def index(request):
    
    r1 = requests.get('https://api.github.com/events')
    if r1.status_code == 200:
        data = r1.json()
        events = [{'name': event['repo']['name'], 'url': event['repo']['url']} for event in data]
        random_event = random.choice(events) if events else None


    
    r2 = requests.get('https://www.boredapi.com/api/activity')
    data = r2.json()
    activity = data['activity']

    
    r3 = requests.get('https://dog.ceo/api/breeds/image/random')
    res3 = r3.json()
    dog_image_url = res3['message']

    
    breed_name = None
    if dog_image_url:
        
        breed_name_response = requests.get('https://dog.ceo/api/breeds/list/all')
        breed_data = breed_name_response.json()
        for breed, sub_breeds in breed_data['message'].items():
            if dog_image_url.startswith(f'https://images.dog.ceo/breeds/{breed}/'):
                breed_name = breed.capitalize()
                break

    return render(request, 'templates/index.html', {'random_event': random_event, 'activity': activity, 'dog_image_url': dog_image_url, 'breed_name': breed_name, 'sub_breeds': sub_breeds})

def refresh_data(request):
    
    r = requests.get('https://dog.ceo/api/breeds/image/random')
    res = r.json()
    dog_image_url = res['message']

    
    r = requests.get('https://www.boredapi.com/api/activity')
    data = r.json()
    activity = data['activity']

    
    r = requests.get('https://api.github.com/events')
    data = r.json()
    events = [{'name': event['repo']['name'], 'url': event['repo']['url']} for event in data]

    
    return JsonResponse({'dog_image_url': dog_image_url, 'activity': activity, 'events': events})