from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import re


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://usethekeyboard.com/figma/')

title_data = [
    'Essential', 'Tools', 'View', 'Zoom', 'Text', 'Shape', 'Selection', 'Cursor', 'Edit', 'Transform', 'Arrange', 'Components'
]

dict = {}
count = 1
for item in title_data:
    id_item = driver.find_element(By.ID, item)
    shortcuts = id_item.find_element(By.CLASS_NAME, 'shortcuts')
    shortcuts_list = shortcuts.find_elements(By.CLASS_NAME, 'shortcut')
    for shortcut in shortcuts_list:
        description = shortcut.find_element(By.CLASS_NAME, 'description')
        dict[f'{count} {description.text}'] = ''
        key_id = shortcut.find_element(By.CLASS_NAME, 'keys')
        keys = key_id.find_elements(By.TAG_NAME, 'li')
        for key in keys:
            dict[f'{count} {description.text}'] += key.text + ' '
        count += 1

with open('mycsvfile.csv', 'w') as f:
    w = csv.DictWriter(f, fieldnames=['Action', 'Combination'])
    w.writeheader()
    for key, value in dict.items():
        key = re.sub('\d+ ', '', key)
        w.writerow({'Action': key, 'Combination': value})
    
