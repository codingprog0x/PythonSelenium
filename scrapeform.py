#scrape a submission form and input the information into a .txt and .csv

import sys
import time
import datetime
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

textfield = 9
matrixfield_P1 = 12
radiobutton_P1 = 11
counter = 0
beginning_marking = "=" * 20
today = datetime.date.today()
csv_name = "Request%s.csv" % (today)

def init_driver() :
	driver = webdriver.Firefox()
	driver.wait = WebDriverWait(driver, 10)
	return driver

def clean_ax(ax_uncleaned) :
	ax_list_char = list(ax_uncleaned)
	ax_list = []
	
	#iterate through each character and remove any hyphens
	for x in range(len(ax_list_char)) :
		if ax_list_char[x] != "-" :
			ax_list.append(ax_list_char[x])
		else :
			pass

	#turn list into a string
	ax_string = "".join(ax_list)
	
	return ax_string
	
def keepGoing(address, the_file, website, pmc) :
	global textfield
	global matrixfield_P1
	global radiobutton_P1
	global counter
	global csv_name
	
	#.csv name for file for script that creates
	csv_to_create = "info.csv"
	
	#prefilled variables
	city = ""
	state = ""
	zip_code = ""
	ID = ""
	
	#static variables for element ID verbiage
	matrixfield_hyphen = "-"
	radiobutton_under = "_"
	
	#element ID verbiage
	matrixfield_P2 = 0
	radiobutton_P2 = 0
	
	#counter for number submitted
	counter += 1
	
	text = "RESULT_TextField-%s" % (textfield)
	matrix = "RESULT_MatrixTextField-%d%s%d" % (matrixfield_P1, matrixfield_hyphen, matrixfield_P2)
	radio = "RESULT_RadioButton-%d%s%d" % (radiobutton_P1, radiobutton_under, radiobutton_P2)
	
	#grab units / textfield should be 10, 18, 26, 33, 40, 47, 54, 61...
	textfield += 1
	text = "RESULT_TextField-%s" % (textfield)
	units = driver.find_element_by_id(text).get_attribute("value")
	
	#grab existing_acct / textfield should be 13, 21, 29, 36, 43, 50, 57, 64...
	textfield += 3
	text = "RESULT_TextField-%s" % (textfield)
	existing_acct = driver.find_element_by_id(text).get_attribute("value")
	
	#grab account
	account = driver.find_element_by_id(matrix).get_attribute("value")
	
	#increment matrixfield_P2 to grab route
	matrixfield_P2 += 1
	matrix = "RESULT_MatrixTextField-%d%s%d" % (matrixfield_P1, matrixfield_hyphen, matrixfield_P2)
	route = driver.find_element_by_id(matrix).get_attribute("value")
	
	#increment matrixfield_P2 to grab different_name
	matrixfield_P2 += 1
	matrix = "RESULT_MatrixTextField-%d%s%d" % (matrixfield_P1, matrixfield_hyphen, matrixfield_P2)
	different_name = driver.find_element_by_id(matrix).get_attribute("value")
	
	#increment matrixfield_P2 to grab ax
	matrixfield_P2 += 1
	matrix = "RESULT_MatrixTextField-%d%s%d" % (matrixfield_P1, matrixfield_hyphen, matrixfield_P2)
	ax_uncleaned = driver.find_element_by_id(matrix).get_attribute("value")
	
	#call function to remove hyphens, if present
	ax = clean_ax(ax_uncleaned)
	
	#grab new or existing account info
	new = driver.find_element_by_id(radio).get_attribute("checked")
	
	#increment radio to grab old account info
	radiobutton_P2 += 1
	radio = "RESULT_RadioButton-%d%s%d" % (radiobutton_P1, radiobutton_under, radiobutton_P2)
	old = driver.find_element_by_id(radio).get_attribute("checked")
	
	#write to .csv file the info needed for request: ax, different_name, acct, route, website
	the_file.write("Building: " + str(counter) + "\n")
	the_file.write("Name: " + different_name + "\n")
	the_file.write("Address: " + address + "\n")
	the_file.write("Units: " + units + "\n")
	the_file.write("Account: " + account + "\n")
	the_file.write("Route: " + route + "\n")
	the_file.write("Ax: " + ax + "\n")
	
	#create and fill .csv file for script that creates
	propInfo = [pmc, different_name, address, city, state, zip_code, ID, route, account]
	with open(csv_to_create, "ab") as csv_create :
		csv_write_this = csv.writer(csv_create, quoting=csv.QUOTE_ALL)
		csv_write_this.writerow(propInfo)
	
	#write to file old/new/NA account info
	if new :
		the_file.write("This is a new account.\n\n")
	elif old :
		the_file.write("Use existing account: %s.\n\n" % (existing_acct))
	else :
		the_file.write("New or existing was not specified.\n\n")
	
	the_file.write(beginning_marking + "\n\n")
	
	#open .csv and write needed information
	with open (csv_name, "ab") as csvfile :
		csv_write = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
		merch_req = [ax, different_name, different_name, account, route, website]
		csv_write.writerow(merch_req)	
	
def lookup(driver) :
	global textfield
	global matrixfield_P1
	global radiobutton_P1
	global counter
	global beginning_mark
	global today
	global csv_name
	
	#prefill variable
	is_address_filled = ""

	#variable for beauty-marking purposes
	new_marking = "-" * 20
	
	#variable to hold password (currently a fake one for security purposes)
	pw_word = "mgforms"
	
	#get website from terminal argument
	driver.get(sys.argv[1])
	
	try :
		#locate html element for password field, enter password, click submit
		login_pw = driver.wait.until(EC.presence_of_element_located((By.NAME, "Password")))
		login_pw.send_keys(pw_word)
		
		login_button = driver.find_element_by_name("Submit")
		login_button.click()
		
		time.sleep(3)
		 
	except TimeoutException :
		print "Something wasn't found. Script ending..."
	
	#create and name file using name of <filler>
	the_file_name = driver.find_element_by_id("RESULT_TextField-4").get_attribute("value")
	the_file = open(the_file_name + str(today) + ".txt", "a")
	
	#print submitter and info and date into file
	submitter = driver.find_element_by_id("RESULT_TextField-2").get_attribute("value")
	contact_info = driver.find_element_by_id("RESULT_TextField-3").get_attribute("value")
	website = driver.find_element_by_id("RESULT_TextField-5").get_attribute("value")
	
	the_file.write(new_marking + "\n")
	the_file.write(submitter + "\n")
	the_file.write(contact_info + "\n")
	the_file.write(website + "\n")
	the_file.write(new_marking + "\n\n")
	the_file.write(beginning_marking + "\n\n")
	
	#write (obfuscated) headers into .csv file
	with open (csv_name, "ab") as csvfile :
		headers = ["ID", "Name", "Something Here", "A Number", "B Number", "Website"]
		csv_headers = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
		csv_headers.writerow(headers)	
	
	#max of 15 searches
	for x in range(15) :
		#don't increment element ID variables for first run
		if counter < 1 :
			textfield_text = "RESULT_TextField-%d" % (textfield)
			is_address_filled = driver.find_element_by_id(textfield_text).get_attribute("value")
			
			#if address field in form isn't empty, continue
			if is_address_filled != "" :
				keepGoing(is_address_filled, the_file, website, the_file_name)
		elif counter < 3 :
			#increment element ID variables by 4/8 for next two runs
			#due to html element ID incrementing differently after first run
			textfield += 4
			matrixfield_P1 += 8
			radiobutton_P1 += 8
			textfield_text = "RESULT_TextField-%d" % (textfield)
			is_address_filled = driver.find_element_by_id(textfield_text).get_attribute("value")
			
			#if address field in form isn't empty, continue; else, stop
			if is_address_filled != "" :
				keepGoing(isAddressFilled, the_file, website, the_file_name)
			else :
				break
		else :
			#html element ID increments differently after previous two runs
			#change int variables' incrementation accordingly
			textfield += 3
			matrixfield_P1 += 7
			radiobutton_P1 += 7
			textfield_text = "RESULT_TextField-%d" % (textfield)
			is_address_filled = driver.find_element_by_id(textfield_text).get_attribute("value")
			
			#if address field in form isn't empty, continue; else, stop
			if is_address_filled != "" :
				keepGoing(is_address_filled, the_file, website, the_file_name)
			else :
				break
	
	#if there are comments by submitter, write them to file
	comments = driver.find_element_by_id("RESULT_TextArea-115").get_attribute("value")
	if comments != "" :
		the_file.write("Comments: " + comments + "\n\n\n")
	else :
		the_file.write("Comments: None" + "\n\n\n")
		
	print "Total submitted: %d." % (counter)
	time.sleep(1)
	print "File closing..."
	the_file.close()
	driver.quit()
	time.sleep(2)

if __name__ == "__main__" :
	driver = init_driver()
	lookup(driver)
