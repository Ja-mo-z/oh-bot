"""OH"""
# https://www.youtube.com/watch?v=YbGAUEjTKg4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the webdriver (replace 'path/to/chromedriver' with the actual path)
driver = webdriver.Chrome()

# Navigate to the form page
driver.get('https://eecsoh.eecs.umich.edu/queues/2P5KQ4RyodHmLtTStEj24kcn7LH')

# Find form elements and fill them (replace 'your_description_id' and 'your_location_id')
description = driver.find_element('/html/body/div/section/div/div/div[2]/div/div/section[2]/div/div[2]/div/div[2]/div/div[1]/div/input')
location = driver.find_element('id', 'your_location_id')

description.send_keys('your_description_text')
location.send_keys('your_location_text')

# Submit the form
location.send_keys(Keys.RETURN)

# Close the browser
driver.quit()
