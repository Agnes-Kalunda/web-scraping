# newsapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from plyer import notification

def get_machine_learning_news(request):
    location = "en-KE"  
    url = f"https://news.google.com/search?q=machine+learning&hl={location}"


#user-agent headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
     
        news_titles = [item.text for item in soup.find_all('h3')]
        return render(request, 'main.html', {'news_titles': news_titles})
    else:
        return HttpResponse(f"Failed to fetch news. Status Code: {response.status_code}")

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Machine Learning News",
        timeout=10,
    )
