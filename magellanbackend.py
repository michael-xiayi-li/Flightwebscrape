import requests
import json
import pycurl
import io
from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

url = 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=AIzaSyAFdRl9kusGYLoxBvNt5xAlGYqGDjOq8Es'
email="youremailhere"
telephonenumber='yourphonenumberhere"
month="monthofbirthhere"
day="dayofbirthhere"
year="yearofbirthhere"
firstname="yourfirstnamehere"
lastname="yourlastnamehere"
gender="yourgenderhere"

payload = json.load(open("search.json"))
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=json.dumps(payload), headers=headers)

def lookforflights():
    search=r.json()['trips']['tripOption']



    prices=[]
    slices=[]
    segments=[]
    legs=[]
    bookingcodes=[]

    trips=[]


    #trips.tripOption[].slice[].segment[].leg[].origin


    #tripoption is a dictionary


    for i in search:
        prices.append(i['saleTotal'])



    #different slices of the trip options
    for i in search:
        slices.append(i['slice'])


    #slices are lists with lists in them

    for i in slices:
        segments.append(i[0]['segment'])



    for i in segments:
        totaltrips=[]
        for j in i:
            totaltrips.append(j['leg'])
        legs.append(totaltrips)

    for i in legs:
        redtrips=[i[0][0]['origin']]
        for j in i:
            redtrips.append(j[0]['destination'])
        trips.append(redtrips)



    for i in segments:
        redcodes=[]
        flightbookingcarrier=""
        flightbookingnumber=""
        for j in i:
            flight=j["flight"]
            flightbookingcarrier=flight['carrier']
            flightbookingnumber=flight['number']
            redcodes.append(flightbookingcarrier+flightbookingnumber)
        



        bookingcodes.append(redcodes)







#browser=webdriver.Chrome('C:\Python35\Scripts\chromedriver.exe')
#browser.get('https://www.kayak.com/flights')
#####onewaylist =browser.find_elements_by_css_selector("input[type='radio'][value='y']")
#onewaylist=browser.find_element_by_id('onewaytrip-label')
#onewaylist.click()



   #browser=webdriver.Chrome('C:\Python35\Scripts\chromedriver.exe')   
   # browser.get('https://www.kayak.com/flights/'+ origin + '-'+destination + '/'+date)

#origin=browser.find_element_by_css_selector("input[placeholder='From']")
#origin.send_keys('LLL')

#destination=browser.find_element_by_css_selector("input[placeholder='To']")
#destination.send_keys('RDU')

#date='07/24/2016'

#datefield= browser.find_element_by_id('')


#date format: year-month-day
def flightorder(origin,destination,date):
    browser=webdriver.Chrome('C:\Python35\Scripts\chromedriver.exe')   
    browser.get('https://www.kayak.com/flights/'+ origin + '-'+destination + '/'+date)

    carriers=browser.find_elements_by_tag_name("span")

    deallist=[];

    for i in carriers:
        if (i.get_attribute('innerHTML')=='View Deal'):
            deallist.append(i)

    
    deallist[1].click()




   



    browser.switch_to.window(browser.window_handles[1])


    browser.implicitly_wait(15)

    
    buttons = browser.find_elements_by_id("tripSummarySubmitBtn")
   


    for i in buttons:
        if (i.get_attribute('innerHTML')=='CONTINUE'):
            i.click()
            break
        print(i.get_attribute('innerHTML'))



    firstnamefield= browser.find_element_by_id("firstName0")
    firstnamefield.send_keys(firstname)

   
    lastnamefield= browser.find_element_by_id('lastName0')
    lastnamefield.send_keys(lastname)


   
    select = browser.find_element_by_id('gender0')
    genderoptions =select.find_elements_by_tag_name("option")

    for i in genderoptions:
        if (i.get_attribute("value")==gender):
            i.click()
    #select.click()

    
    

    monthselect= browser.find_element_by_id('month0')
    monthoptions = monthselect.find_elements_by_tag_name("option")
    for i in monthoptions:
        if (i.get_attribute("value")==month):
            i.click()
    #monthselect.click()

    dayselect = browser.find_element_by_id('day0')
    dayoptions= dayselect.find_elements_by_tag_name('option')
    for i in dayoptions:
        if(i.get_attribute('value')==day):
            i.click()
    #dayselect.click()

    yearselect = browser.find_element_by_id('year0')
    yearoptions=yearselect.find_elements_by_tag_name('option')
    for i in yearoptions:
        if(i.get_attribute('value')==year):
            i.click()
    #yearselect.click()


    #no_button = browser.find_element_by_id('declineContactN_0')
    #print(type(no_button))
    #no_button.click()
    
   
    telephoneinput=browser.find_element_by_id("telephoneNumber0")
    telephoneinput.send_keys(telephonenumber)

    

    emailinput=browser.find_element_by_id('email')
    remailinput=browser.find_element_by_id('reEmail')

    emailinput.send_keys(email)
    remailinput.send_keys(email)


    noselect=browser.find_element_by_xpath('//label[@for="declineContactN_0"]')

    nobutton= noselect.find_elements_by_tag_name('span')
   
    nobutton[0].click()



    continuebutton=browser.find_element_by_id("paxReviewPurchaseBtn")
    continuebutton.click()

    print(s)


flightorder('RDU','CUN','2016-12-27')




#############################################

#search_box = driver.find_element_by_id('q')





#url = "https://www.kayak.com/flights"

 #   c.setopt(pycurl.URL, url)
 #   c.setopt(pycurl.VERBOSE, 1)

#post_data = {'origin': 'RDU','destination': 'YYZ', }
#postfields = urlencode(post_data)



###############################################################################
#url = urllib.request.urlopen("https://www.kayak.com/")

#content = url.read()

#soup = BeautifulSoup(content,"html.parser")

#links = soup.findAll("button")

#for href in links:
 #   print(href)














