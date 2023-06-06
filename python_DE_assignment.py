from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
# Set up Selenium options
options = Options()
options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

# Set up Chrome driver path
webdriver_service = Service('chromedriver.exe')  # Replace with the path to your chromedriver executable

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=webdriver_service, options=options)

# Navigate to the website
url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
driver.get(url)

# AUTOMATE SEARCH INFORMATION
# Est,ValueNotes, Description,
# ClosingDate
output_list=[]
all_selected_lines=[]
for i in range(1, 6):
    # Construct the XPath by replacing [2] with [i]
    xpath = "/html/body/div[2]/div[2]/div[2]/div/div[3]/div[6]/div/div/div/div[3]/div/table/tbody/tr[" + str(i) + "]"
    # Find the element using the constructed XPath
    element = driver.find_element(By.XPATH, xpath)

    output=element.text
    lines = output.splitlines()  # Split the output into lines and create a list
    selected_lines = {
        'Information': lines[2],
        'ValueNotes': lines[0].split()[1],
        'Closing Date': lines[3]
    }
    all_selected_lines.append(selected_lines)

# Define the CSV file path
csv_file = 'output.csv'

# Define the fieldnames for the CSV file
fieldnames = ['Information', 'ValueNotes', 'Closing Date']

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(all_selected_lines)

print("Data successfully written to CSV file:", csv_file)

driver.quit()
