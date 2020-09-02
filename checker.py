from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from time import sleep


def get_available():
    driver = webdriver.Firefox()
    driver.get("https://compass-ssb.tamu.edu/pls/PROD/bwykschd.p_disp_detail_sched?term_in=202011&crn_in=27361")
    remaining = driver.find_element_by_xpath("/html/body/div[3]/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[3]")
    print(remaining.text)
    total = driver.find_element_by_xpath("/html/body/div[3]/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[1]")
    print(total.text)
    assert "No results found." not in driver.page_source
    #driver.quit()
    return remaining.text,total.text
def send_msg(username, password, subj, msg):
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.ehlo
    s.login(username, password)
    headers = ["From: " + username, "Subject: " + subj, "To: " + username]
    headers = "\r\n".join(headers)
    s.sendmail(username, username, headers + "\r\n\r\n" + msg)
    print('Email sent!\n')
    s.quit()

#get_available()
remaining,total = get_available()
while(True):
    sleep(10)
    remainingNew,totalNew = get_available()
    if(remaining != remainingNew or total != totalNew):
        msg = str("Total Spots:" + totalNew + "\n" + "spots remaining:" + remainingNew)
        # Enter your email and password in the line below:
        send_msg("Enter Email Here","Enter Password Here",remainingNew + " spots open",msg)
        remaining, total = remainingNew,totalNew
    else:
        print("No, new spots")
driver.quit()