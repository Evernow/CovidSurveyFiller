username = ''
password = ''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
def CompleteSymptomSurvey():
    driver = webdriver.Chrome()
    driver.get("https://patientconnect.bu.edu/")
    driver.find_element_by_id("j_username").send_keys(username)
    driver.find_element_by_id("j_password").send_keys(password)
    driver.find_element_by_name("_eventId_proceed").click()
    driver.find_element_by_xpath('//*[@id="ctl03"]/div[3]/div/a').click()
    driver.find_element_by_xpath('//*[@id="mainbody"]/div[2]/div[1]/div/div[2]/a').click()
    driver.find_element_by_xpath('//*[@id="mainbody"]/main/form/div[2]/fieldset/div/div[1]/div').click()
    driver.find_element_by_xpath('//*[@id="mainbody"]/header/div/div[2]/input').click()
def GetBadge():
    import subprocess
    from datetime import datetime
    dt_string = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
   # dt_string = dt_string.replace('/', '-')
    dt_string = dt_string.replace(':', '-')

    directory = dt_string + ".png"
    directory = os.path.join(r"C:\Users\Daniel\Desktop",directory )
    driver = webdriver.Chrome()
    driver.get("https://patientconnect.bu.edu/")
    time.sleep(1)
    driver.find_element_by_id("j_username").send_keys(username)
    driver.find_element_by_id("j_password").send_keys(password)
    driver.find_element_by_name("_eventId_proceed").click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="showQuarantineBadge"]').click()
    time.sleep(1)
    driver.save_screenshot(directory)
    
    from PIL import Image
    im = Image.open(directory)
    im1 = im.crop((430, 0, 800, 530))
    im1.save((directory), 'png')
    rcloneexe = r"C:\Users\Daniel\Desktop\Badges\rclone.exe "
    fuckingshit = subprocess.call(rcloneexe + "copy " + directory + " DriveCovid:CovidBadges",  shell=True)
  #  print(fuckingshit)

while True:
    CompleteSymptomSurvey()
    time.sleep(120)
    GetBadge()
    time.sleep(600)

#from datetime import datetime

#dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#print("date and time =", dt_string)	