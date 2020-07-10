import os
import time
import logging

from dotenv import load_dotenv
from selenium import webdriver, common
from webdriver_manager.chrome import ChromeDriverManager
	
def main():
	try:
		logging.getLogger().setLevel(logging.ERROR)
		logging.basicConfig(filename='error.log', level=logging.ERROR)
		load_dotenv('.env')
		print('A empezar a joder...')

		# Guarda la sesion
		options = webdriver.ChromeOptions()
		options.add_argument('--user-data-dir=./SessionData')
		driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
		driver.get('https://web.whatsapp.com/')

		name = input('Nombre del usuario o grupo: ')
		msg = input('Mensaje: ')
		count = int(input('Cantidad de mensajes: '))

		input('Presione enter para comenzar a enviar.')

		user = driver.find_element_by_xpath(f'//span[contains(@title, "{name}")]')
		user.click()
		
		# The classname of message box may vary.
		msg_box = driver.find_element_by_class_name('sasdasd')
		# msg_box = driver.find_element_by_class_name(os.getenv('MSG_BOX')) 
			
		for i in range(count):
			msg_box.send_keys(msg)
			# The classname of send button may vary.
			button = driver.find_element_by_class_name(os.getenv('SEND_BUTTON'))
			button.click()
			# time.sleep(2)
	except common.exceptions.NoSuchElementException:
		print("VERIFICAR LOS NOMBRES EN .ENV")
	except Exception as e:
		logging.error(e)
		print('Hubo un error, guardado en el archivo ./error.log')
	print('DONE.')

main()