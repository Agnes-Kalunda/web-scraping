# newsapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from plyer import notification

def get_machine_learning_news(request):
    location = "en-KE"  # Set the location code for Nairobi
    url = f"https://news.google.com/search?q=machine+learning&hl={location}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract and process news articles
        # For simplicity, let's just extract titles for demonstration
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
