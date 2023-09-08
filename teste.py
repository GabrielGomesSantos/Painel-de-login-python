from selenium import webdriver
#set chromodriver.exe path
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
#implicit wait
driver.implicitly_wait(0.5)
#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://www.tutorialspoint.com/index.htm")
#identify element
l =driver.find_element_by_xpath("//button[text()='Check it Now']")
#perform click
l.click()
print("Page title is: ")
print(driver.title)
#close browser
driver.quit()