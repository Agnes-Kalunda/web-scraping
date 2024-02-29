# newsapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from selenium import webdriver
from plyer import notification

def get_machine_learning_news(request):
    location = "en-KE"
    url = f"https://news.google.com/search?q=president&hl={location}"

    driver = None

    try:
        # Use ChromeOptions to configure the ChromeDriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  
        chrome_options.add_argument('--disable-gpu')  # to avoid GPU-related issues

        # Initialize the ChromeDriver 
        driver = webdriver.Chrome(options=chrome_options)

        driver.get(url)

        
        import time
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        news_titles = [item.text for item in soup.find_all('h3')]

        return render(request, 'main.html', {'news_titles': news_titles})
    except Exception as e:
        return HttpResponse(f"Failed to fetch news. Error: {str(e)}")
    finally:
        if driver:
            driver.quit()

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Machine Learning News",
        timeout=10,
    )
