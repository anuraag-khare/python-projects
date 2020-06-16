# Whatsapp automation using Selenium



 

## This is python web crawling script written using selenium module.

This script automates the whatsapp web wherein users are given the following options:

- Send a Text message to any of your contacts (Users have the option to set the frequency of the message)
- Send an image or a video file.
- Send a document.
- View your own profile.

**NOTE:-**
1. This code uses Microsoft Edge Webdriver. If you wish to run on chrome or other browser you have to edit the code 
'''
browser = Webdriver.Edge(*path to MSEdge webdriver file*)
'''

to

'''
browser = Webdriver.Chrome(*path to chrome webdriver file*)
'''
2. You have to download the webdriver of your respective browser from the web and provide the appropriate path as well.
3. Whenever entering the path of the file replace all " \ " with "/" 
example-
Path shown by windows:
> C:\Users\Anuraag\Downloads\preview.jpg
Path you need to enter:
> C:/Users/Anuraag/Downloads/preview.jpg
