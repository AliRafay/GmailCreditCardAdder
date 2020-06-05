from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import tkinter
import pathlib
directory= pathlib.Path(__file__).parent.absolute().__str__()
directory=directory.replace('\\','\\\\')
directory+="\\\\chromedriver.exe"

def hi():
    global email
    global password
    email=startEntry.get()
    password=startEntry2.get()
    root.destroy()


root = tkinter.Tk()
root.geometry('500x300')
root.title("login Information")
startLabel = tkinter.Label(root,font=35, text="Enter Gmail ID: ")
startEntry = tkinter.Entry(root,width=50)

startLabel2 = tkinter.Label(root,font=35, text="Enter Password: ",)
startEntry2 = tkinter.Entry(root,width=50)

startLabel.pack()
startEntry.pack()
startLabel2.pack()
startEntry2.pack()

plotButton = tkinter.Button(root, text="Submit", command=hi,width=20)

plotButton.pack()
root.mainloop()

print('Now please wait a minute :)')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

Options().page_load_strategy = 'normal'
driver = webdriver.Chrome(directory,options=Options(),chrome_options=chrome_options)
driver.get('https://namso-gen.com')
time.sleep(1.5)
driver.find_element_by_xpath('//*[@id="main"]/div/div/div[3]/div[1]/form/div[1]/label/input').send_keys('376409')
driver.find_element_by_xpath('//*[@id="main"]/div/div/div[3]/div[1]/form/div[5]/button').click()

result_textarea=driver.find_element_by_xpath('//*[@id="result"]').get_attribute('value')
card_number=result_textarea[:15]
MM=result_textarea[16:18]
YY=result_textarea[21:23]
CVC=result_textarea[24:28]

driver.execute_script('''window.open("https://payments.google.com","_blank");''')
driver.close()
driver.switch_to_window(driver.window_handles[0])
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="identifierNext"]/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
time.sleep(3)
try:
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/c-wiz/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div/span/span').click()
except:
    pass
driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[1]/div[2]/div/c-wiz/div/div/div[4]/div/span/div/button/div[2]').click()
time.sleep(1)
driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="signUpWidget_:0Iframe"]'))
time.sleep(1)
driver.find_element_by_xpath('//*[@id="creditCardForm-1"]/div[3]/div[2]/div/div[1]/div/div/div[1]').click()
driver.find_element_by_xpath('//*[@id="creditCardForm-1"]/div[3]/div[2]/div/div[2]/div/div[2]/div/dl/dd/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]').click()
driver.find_element_by_xpath('//*[@id=":81"]/div').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="iframeBody"]/div[3]/div[3]/div[3]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div[1]/input').send_keys('036.582.528-04')
driver.find_element_by_xpath('//*[@id="iframeBody"]/div[3]/div[3]/div[3]/div[3]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div/div/div[1]/div/div[1]/input').send_keys('03/01/1993')
driver.find_element_by_xpath('//*[@id="iframeBody"]/div[3]/div[3]/div[4]/div[1]/div').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="iframeBody"]/div[3]/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/dl/dd/div[2]/div/div[2]/div/div/div/div[8]/div/div/div[1]/input').send_keys('None')
driver.find_element_by_xpath('//*[@id="iframeBody"]/div[3]/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/dl/dd/div[2]/div/div[2]/div/div/div/div[14]/div/div[1]/div[2]').click()
driver.find_element_by_xpath('//*[@id=":7g"]/div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="iframeBody"]/div[3]/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/dl/dd/div[2]/div/div[2]/div/div/div/div[16]/div/div[1]/div[2]').click()
driver.find_element_by_xpath('//*[@id=":ho"]/div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="iframeBody"]/div[3]/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/dl/dd/div[2]/div/div[2]/div/div/div/div[18]/div/div/div[1]/input').send_keys('41500290')
driver.find_element_by_xpath('//*[@id="creditCardForm-1"]/div[1]/div[1]/div/div/div[1]/input').send_keys(card_number)
driver.find_element_by_xpath('//*[@id="creditCardForm-1"]/div[1]/div[2]/div[1]/div[1]/div/div[1]/input').send_keys(MM)
driver.find_element_by_xpath('//*[@id="creditCardForm-1"]/div[1]/div[2]/div[1]/div[2]/div/div[1]/input').send_keys(YY)
driver.find_element_by_xpath('//*[@id="creditCardForm-1"]/div[1]/div[2]/div[2]/div/div/div[1]/input').send_keys(CVC)
driver.find_element_by_xpath('//*[@id="iframeBody"]/div[3]/div[3]/div[2]/div[1]/div').click()
time.sleep(1.5)
driver.close()
print('DONE!!')