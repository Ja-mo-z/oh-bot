# """OH"""
# # https://www.youtube.com/watch?v=YbGAUEjTKg4
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

# # Set up the webdriver (replace 'path/to/chromedriver' with the actual path)
# driver = webdriver.Chrome()

# # Navigate to the form page
# driver.get('https://eecsoh.eecs.umich.edu/queues/2P5KQ4RyodHmLtTStEj24kcn7LH')

# # Find form elements and fill them (replace 'your_description_id' and 'your_location_id')
# description = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div[2]/div/div/section[2]/div/div[2]/div/div[2]/div/div[1]/div/input')
# location = driver.find_element(By.XPATH, '/html/body/div[1]/section/div/div/div[2]/div/div/section[2]/div/div[2]/div/div[2]/div/div[2]/div/input')
# submit = driver.find_element(By.XPATH, '/html/body/div[1]/section/div/div/div[2]/div/div/section[2]/div/div[2]/div/div[2]/div/div[3]/div/button')

# description.send_keys('your_description_text')
# location.send_keys('your_location_text')

# # Submit the form
# submit.send_keys(Keys.RETURN)

# # Close the browser
# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def submit_form():
    """Submits the form."""
    # Set up the webdriver (replace 'path/to/chromedriver' with the actual path)
    driver = webdriver.Chrome()
    
    # Navigate to the form page
    driver.get('https://eecsoh.eecs.umich.edu/queues/2P5KQ4RyodHmLtTStEj24kcn7LH')

    try:
        # Find form elements (replace 'your_description_id' and 'your_location_id')
        # description = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div[2]/div/div/section[2]/div/div[2]/div/div[2]/div/div[1]/div/input')
        description = driver.find_element(By.XPATH, '(//input)[1]')
        # location = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div[2]/div/div/section[2]/div/div[2]/div/div[2]/div/div[2]/div/input')
        location = driver.find_element(By.XPATH, '(//input)[2]')

        submit = driver.find_element('//button[text()="Sign Up"]')
        

        # Fill in form elements (replace 'your_description_text' and 'your_location_text')
        description.send_keys('your_description_text')
        location.send_keys('your_location_text')

        # Wait for the submit button to be clickable
        submit_button_enabled = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(submit))

        # Submit the form
        submit_button_enabled.click()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

# Keep trying to submit until successful
while True:
    try:
        submit_form()
        break  # Break out of the loop if submission is successful
    except Exception as e:
        print(f"Submission failed. Retrying...")
