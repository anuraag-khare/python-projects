#!/usr/bin/env python
# coding: utf-8

 ### whatsapp automation
# Whatsapp automation using selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep



def text_message():
    global target
    string=input('Enter a message:')
    count=int(input('Enter the times to send message: '))
    if(user_located==0):                                                    # this section executes only if user not already located by other functions.
        x_arg ='//span[contains(@title, ' + target +' )]'
        target= wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
        target.click()
    input_box = browser.find_element_by_class_name('_1Plpp')
    for i in range(count):
        input_box.send_keys(string + Keys.ENTER)                            # sending messages and hitting ENTER key.

def send_image():
    global target
    filepath=input('Enter the path to image')                               # replace all backward slashes in file path by forward slashes whenever path is asked.
    if(user_located==0):
        x_arg ='//span[contains(@title, ' + target +' )]'
        target= wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
        target.click()
    attach=browser.find_element_by_xpath('//div[@title="Attach"]')
    attach.click()
    send_photo=browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    send_photo.send_keys(filepath)
    sleep(3)                                                                # wait for image preview to load then click send
    click_send=browser.find_element_by_xpath('//span[@data-icon="send-light"]')
    click_send.click()
def send_doc():
    global target
    filepath=input("Enter path to document")
    if(user_located==0):
        x_arg ='//span[contains(@title, ' + target +' )]'
        target= wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
        target.click()
    attach=browser.find_element_by_xpath('//div[@title="Attach"]')
    attach.click()
    send_file=browser.find_element_by_xpath('//input[@accept="*"]')
    send_file.send_doc(filepath)
    sleep(2)
    click_send=browser.find_element_by_xpath('//span[@data-icon="send-light"]')
    click_send.click()
    
def show_profile():
    global target
    if(user_located==0):
        x_arg ='//span[contains(@title, ' + target +' )]'
        target= wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
        target.click()
    profile=browser.find_element_by_class_name('_1WliW')
    profile.click()
    

browser=webdriver.Edge("/Users/Anuraag/Downloads/Compressed/edgedriver_win32/msedgedriver")
browser.get("https://web.whatsapp.com")
wait = WebDriverWait(browser, 400)                                          # wait for QR code scanning by user
user= input('Enter name of the user: ')
target = '"%s"'%user
flag=True                                                                   # flag variable used to exit loop
user_located=0                                                              # set this value 1 if user is located
while(flag==True):                                                          # Driver code section
    print('''
    1.Send a Text Messaage
    2.Send a photo/video
    3.Send a document
    4.View Your profile
    5.Exit''')
    choice=int(input('Enter your choice: '))
    if choice==1:
        text_message()
        user_located=1                                                      
        continue
    elif choice==2:
        send_image()
        user_located=1
        continue
    elif choice==3:
        send_doc()
        user_located=1
        continue
    elif choice==4:
        show_profile()
        user_located=1
        continue
    elif choice==5:
        break
    else:
        print('Enter a valid option')  
    
    

