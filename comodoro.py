import os
import time
from dotenv import load_dotenv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
	
def main():
	load_dotenv('.env')
	print('A empezar a joder...')
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://web.whatsapp.com/')

	name = input('Nombre del usuario o grupo: ')
	msg = input('Mensaje: ')
	count = int(input('Cantidad de mensajes: '))

	input('Presione enter una vez escaneado el QR')

	user = driver.find_element_by_xpath(f'//span[contains(@title, "{name}")]')
	user.click()
	
	# The classname of message box may vary.
	msg_box = driver.find_element_by_class_name(os.getenv('MSG_BOX')) 
		
	for i in range(count):
		msg_box.send_keys(msg)
		# The classname of send button may vary.
		button = driver.find_element_by_class_name(os.getenv('SEND_BUTTON'))
		button.click()
		# time.sleep(2)
	
	print('DONE.')

main()