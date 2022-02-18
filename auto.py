#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time
import calendar
curr_date = datetime.date.today()
week = calendar.day_name[curr_date.weekday()]
now=datetime.datetime.now()
hr=now.hour
path=0

#Subjects
digitalElec = 'https://cuchd.blackboard.com/ultra/courses/_49604_1/outline' #DE
physics = 'https://cuchd.blackboard.com/ultra/courses/_52863_1/outline' #Physics
communication = 'https://cuchd.blackboard.com/ultra/courses/_53327_1/outline' #CS
maths = 'https://cuchd.blackboard.com/ultra/courses/_51903_1/outline' #Maths
lsm = 'https://cuchd.blackboard.com/ultra/courses/_51297_1/outline' #LSM
oops = 'https://cuchd.blackboard.com/ultra/courses/_52516_1/outline' #OOPS
dt = 'https://cuchd.blackboard.com/ultra/courses/_49768_1/outline' #DT
indepPro = 'https://cuchd.blackboard.com/ultra/courses/_55685_1/outline' #Independent
cgcad = 'https://cuchd.blackboard.com/ultra/courses/_48944_1/outline' #CGCAD
ipr = 'https://cuchd.blackboard.com/ultra/courses/_55176_1/outline' #IPR

if week=="Monday":
    if hr==9:
        path= digitalElec
    elif hr==10:
        path= physics
    elif hr==11:
        path= communication
    elif hr==12:
        path= maths
    elif hr==13 or hr==14:
        path = physics
    elif hr==15:
        path = lsm
elif week=="Tuesday":
    if hr==9 or hr==10:
        path= oops
    elif hr==11:
        path = physics
    elif hr==12:
        path= digitalElec
    elif hr==13:
        path= maths
    elif hr==14 or hr==15:
        path = dt
elif week=="Wednesday":
    if hr==9:
        path = dt
    elif hr==10:
        path= indepPro
    elif hr==11:
        path= communication
    elif hr==13:
        path= maths
    elif hr==14 or hr==15:
        path= oops
elif week=="Thursday":
    if hr==9:
        path= maths
    elif hr==10:
        path = physics
    elif hr ==11 or hr==13:
        path = digitalElec
    elif hr ==14 or hr==15:
        path = cgcad
elif week =="Friday":
    if hr ==9 or hr==10:
        path= oops
    elif hr==11:
        path= maths
    elif hr==13:
        path= communication
elif week=="Saturday":
    if hr==9:
        path= ipr
path= 'https://cuchd.blackboard.com/ultra/courses/_51903_1/outline'
if path:
    emai= '21BCS10561'
    pas= 'UIms@123' #input("Enter Password: ")
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    opt.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1, 
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1, 
        "profile.default_content_setting_values.notifications": 1 
    })
    driver = webdriver.Chrome(chrome_options=opt)
    driver.get(path)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="agree_button"]').click()
    id1 = driver.find_element_by_xpath('//*[@id="loginFormList"]/li[1]/label')
    id1.click()
    id2 = driver.find_element_by_xpath('//*[@id="user_id"]')
    id2.send_keys(emai)
    passw = driver.find_element_by_xpath('//*[@id="password"]')
    passw.send_keys(pas)
    login = driver.find_element_by_xpath('//*[@id="entry-login"]')
    login.click()
    print("Logging in to Blackboard")
    time.sleep(10)
    print("Logged in to Blackboard")
    print("Finding Current Class")
    time.sleep(15)
    print("Starting Class")
    link = driver.find_element_by_xpath('//*[@id="sessions-list-dropdown"]/span')
    link.click()
    openclass = driver.find_element_by_xpath('//*[@id="sessions-list"]/li/a')
    # if(openclass.text=='Course Room'):
    #     print("First class is Course Room. Selecting 2nd one.")
    #     openclass=driver.find_element_by_xpath('//*[@id="sessions-list"]/li[2]/a')
    openclass.click()
    time.sleep(5)
    print("Class Started")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(10)
    print("Skipping the tutorial")
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="dialog-description-audio"]/div[2]/button').click()
    print("Audio Check Done")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="techcheck-video-ok-button"]').click()
    print("Video Check Done")
    time.sleep(5)
    print("Setting up")
    time.sleep(5)
    print("Clicking Later")
    driver.find_element_by_xpath('//*[@id="announcement-modal-page-wrap"]/div/div[4]/button').click()
    print("Tutorial Cancelled")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="exit-tutorial"]').click()
    print("Class Successfully Opened")
else:
    print("No class right now")