# newsapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # Requires installation: pip install webdriver_manager
from plyer import notification

def get_machine_learning_news(request):
    location = "en-KE"
    url = f"https://news.google.com/search?q=machine+learning&hl={location}"

    # Use ChromeDriverManager to automatically download the appropriate ChromeDriver version
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    try:
        driver.get(url)

        # Wait for some time to allow JavaScript to execute (adjust the sleep time if needed)
        import time
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        news_titles = [item.text for item in soup.find_all('h3')]

        return render(request, 'main.html', {'news_titles': news_titles})
    except Exception as e:
        return HttpResponse(f"Failed to fetch news. Error: {str(e)}")
    finally:
        driver.quit()

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Machine Learning News",
        timeout=10,
    )
