from django.shortcuts import render

from .models import *
import time
from time import sleep
from selenium import webdriver

def Home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        Login_credentials.objects.create(username=username,password=password)
    return render(request,"index.html")


def Test(request):
    driver = webdriver.Chrome(r'''C:\\Users\\bhara\\Desktop\\LikeBot\\chromedriver.exe''')
    request.driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/')
    sleep(5)
    username_input = driver.find_element_by_css_selector("input[name='username']")
    password_input = driver.find_element_by_css_selector("input[name='password']")
    username_input.send_keys("@coderbhaiya")
    password_input.send_keys("mohsin madarchod")

    links = ["https://www.instagram.com/p/B_wxXGSJ5D4",
             "https://www.instagram.com/p/B_RTSQFJdaj",
             "https://www.instagram.com/p/B-_0UyOpWZd"]

    login_button = driver.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep(6)
    for i in links:
        driver.get(i)
        sleep(4)
        pic = driver.find_element_by_class_name("wpO6b")
        sleep(2)
        pic.click()
        sleep(2)

    #driver.get("https://www.instagram.com/p/B-xSinZJFAh/")
    #sleep(5)
    #pic = driver.find_element_by_class_name("wpO6b")

    #sleep(2)
    #pic.click()
    #logout_button = driver.find_element_by_xpath('//div[@class="text" and text()="Logout"] ')
    #sleep(3)
   # logout_button.click()




    sleep(5)

    driver.close()


