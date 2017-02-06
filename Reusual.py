'''
#	This class and its child classes are used for automating tasks on
#	a specific website
#	Tasks include navigating to certain webpages, inputting data into fields,
#	clicking buttons, and scraping data
####
#	Some methods are written generically so that they can be reused by passing in
#	the html element
#	These are mostly located in the parent class Reusual
#	Other methods, mostly in the child classes, are written for a specific page
#	and specific html elements that are not present in any other pages of
#	this specific website and therefore are best not generically written, as 
#	that would add more overhead when writing a new script
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import time


'''
##
#	Every method returns a boolean--unless otherwise stated--for the scriptor to use
#	as flow control
##
'''
class Reusual:
	def __init__(self, driver_choice = None, timeout_time = None):
		##
		#	If browser choice is not specified or not a valid choice, then default to Firefox
		#	No boolean is returned, as False will never occur
		##
		if driver_choice != "":
			if driver_choice.lower() == "chrome":
				self.driver = webdriver.Chrome()
			elif driver_choice.lower() == "firefox":
				self.driver = webdriver.Firefox()
			else:
				print("Choice for browser not understood. Defaulting to Firefox.")
				self.driver = webdriver.Firefox()
		else:
			print("Defaulting to Firefox")
			self.driver = webdriver.Firefox()
		
		##
		#	If timeout time is not defined, then default to 5
		##
		if timeout_time != "":
			if isinstance(timeout_time, int):
				self.driver_wait = WebDriverWait(self.driver, int(timeout_time))
		else:
			print("Choice for timeout not understood. Defaulting to timeout of 5s.")
			self.driver_wait = WebDriverWait(self.driver, 5)
		
	##
	#	Log in method; returns boolean in case user wants to use it for whatever purpose
	#	such as checking whether the desired action was successful
	#	logging in 
	##
	def log_into_portal_wait(self, username, pw):
		self.load_url("https://afakeportalwebsite.com")
		
		##
		#	Wait to find username-box element. Once found continue with inputting 
		#	password and then click login button
		##
		try:
			user_box = self.driver_wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_ucLogin_login_UserName")))
			user_box.clear()
			time.sleep(.5)
			user_box.send_keys(username)
			
			try:
				pw_box = self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucLogin_login_Password")
				pw_box.clear()
				time.sleep(.5)
				pw_box.send_keys(pw)
				
				try:
					self.driver.find_element_by_id("LoginButton").click()
					return True
				except NoSuchElementException:
					print("No such element of button_id element at " + button_id)
					return False
				except TimeoutException:
					print("Timed out. Couldn't find button_id element at " + button_id)
					return False
				except Exception as e0:
					print(e0)
					return False
			except NoSuchElementException:
				print("No such element of pw_id element at " + pw_id)
				return False
			except TimeoutException:
				print("Timed out. Couldn't find pw_id element at " + pw_id)
				return False
			except Exception as e0:
				print(e0)
				return False
		except NoSuchElementException:
			print("No such element of button_id element at " + user_id)
			return False
		except TimeoutException:
			print("Timed out. Couldn't find user_id element at " + user_id)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	Same as above but not using driver_wait
	##
	def log_into_portal(self, username, pw):
		self.load_url("https://afakeportalwebsite.com")
		
		try:
			user_box = self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucLogin_login_UserName")
			user_box.clear()
			time.sleep(.5)
			user_box.send_keys(username)
			
			try:
				pw_box = self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_ucLogin_login_Password")
				pw_box.clear()
				time.sleep(.5)
				pw_box.send_keys(pw)
				
				try:
					self.driver.find_element_by_id("LoginButton").click()
					return True
					
				except NoSuchElementException:
					print("No such element of button_id element at " + button_id)
					return False
				except TimeoutException:
					print("Timed out. Couldn't find button_id element at " + button_id)
					return False
				except Exception as e0:
					print(e0)
					return False
			except NoSuchElementException:
				print("No such element of pw_id element at " + pw_id)
				return False
			except TimeoutException:
				print("Timed out. Couldn't find pw_id element at " + pw_id)
				return False
			except Exception as e0:
				print(e0)
				return False
		except NoSuchElementException:
			print("No such element of button_id element at " + user_id)
			return False
		except TimeoutException:
			print("Timed out. Couldn't find user_id element at " + user_id)
			return False
		except Exception as e0:
			print(e0)
			return False
	
	##
	#	Generic method used to check whether page has loaded or not before continuing
	#	Useful for when driver_wait isn't working as should when looking for
	#	a specific element
	##
	def check_element_presence_wait_xpath(self, element_id):
		try:
			isPresent = self.driver_wait.until(EC.presence_of_element_located((By.XPATH, element_id)))
			return True
		except NoSuchElementException as e:
			print("check_element_presence_wait_xpath has no such element")
			print(e)
			return False
		except TimeoutException as e1:
			print("check_element_presence_wait_xpath has timed out")
			print(e1)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	Same as above but not using driver_wait
	##
	def check_element_presence_xpath(self, element_id):
		try:
			isPresent = self.driver.find_element_by_xpath(id)
			return True
		except NoSuchElementException as e:
			print("check_element_presence_xpath has no such element")
			print(e)
			return False
		except Exception as e0:
			print(e0)
			return False
	
	##
	#	Similar to above but using Selenium's link_text
	##
	def check_element_presence_link_text(self, element_id):
		try:
			isPresent = self.driver.find_element_by_link_text(element_id)
			return True
		except NoSuchElementException as e:
			print("check_element_presence_link_text has no such element")
			print(e)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	Generic method used to click on an element's xpath
	##
	def click_this_wait_xpath(self, element_id):
		try:
			self.driver_wait.until(EC.presence_of_element_located((By.XPATH, element_id))).click()
		except NoSuchElementException as e:
			print("click_this_wait_xpath has no such element")
			print(e)
			return False
		except TimeoutException as e1:
			print("click_this_wait_xpath has timed out")
			print(e1)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	Same as above but not using driver_wait
	##
	def click_this_xpath(self, element_id):
		try:
			self.driver.find_element_by_xpath(element_id).click()
		except NoSuchElementException as e:
			print("click_this_xpath has no such element")
			print(e)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	Similar to above but using Selenium's id
	##
	def click_this_wait_id(self, element_id):
		try:
			self.driver_wait.until(EC.presence_of_element_located((By.ID, element_id))).click()
			return True
		except NoSuchElementException as e:
			print("click_this_wait_id has no such element")
			print(e)
			return False
		except TimeoutException as e1:
			print("click_this_wait_id has timed out")
			print(e1)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	Similar to above but not using driver_wait
	##
	def click_this_id(self, element_id):
		try:
			self.driver.find_element_by_id(element_id).click()
			return True
		except NoSuchElementException as e:
			print("click_this_id has no such element")
			print(e)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	Similar to above but using Selenium's link_text
	##
	def click_this_link_text(self, link_text):
		try:
			self.driver.find_element_by_link_text(link_text).click()
			return True
		except NoSuchElementException as e:
			print("click_this_link_text has no such element")
			print(e)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	Generic method to pass data to user-defined field on the webpage
	##
	def send_keys_wait_xpath(self, element_id, a_key):
		try:
			key_field = self.driver_wait.until(EC.presence_of_element_located((By.XPATH, element_id)))
			key_field_text = key_field.text
			print(key_field_text)
			key_field.clear()
			time.sleep(.5)
			key_field.send_keys(a_key)
			return (True, key_field_text)
		except NoSuchElementException as e:
			print("send_keys_wait_xpath has no such element")
			print(e)
			return False
		except TimeoutException as e1:
			print("send_keys_wait_xpath has timed out")
			print(e1)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	A non-generic method used for pagination of the specific website
	##
	def check_for_next_page_wait_link_text(self):
		try:
			next_page = self.driver_wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Next >")))
			next_page.click()
			return True
		except NoSuchElementException as e:
			print("check_for_next_page_wait_link_text has no such element")
			print(e)
			return False
		except TimeoutException as e1:
			print("check_for_next_page_wait_link_text has timed out")
			print(e1)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	Same as above but not using driver_wait
	##
	def check_for_next_page_link_text(self):
		try:
			next_page = self.driver.find_element_by_link_text("Next >")
			next_page.click()
			return True
		except NoSuchElementException as e:
			print("check_for_next_page_link_text has no such element")
			print(e)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	open specified webpage
	##
	def load_url(self, url):
		self.driver.get(url)

	def get_driver(self):
		return self.driver
	
	def get_driver_wait(self):
		return self.driver_wait
		
	def quit_driver(self):
		self.driver.quit()

'''
##
#	Child class that concentrates on a specific page of the website
#	HTML elements on this page is specific and to reduce overhead for scriptor, non-generic
#	methods were created
##
'''
class PMCPage(Reusual):
	def __init__(self, driver, driver_wait):
		Reusual.__init__(self, driver, driver_wait)
	
	def load_PMC_page():
		Reusual.load_url(self, "https://afakepmcpage.com")
	
	##
	#	A non-generic method to display 100 results for this specific page
	##
	def load_more_results_PMC_page_wait(self):
		try:
			self.driver_wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucCompanies_pagingChanger']/option[4]"))).click()
			return True
		except NoSuchElementException as e:
			print("Invalid element for load_more_results_PMC_page_wait")
			print(e)
			return False
		except TimeoutException as e1:
			print("load_more_results_PMC_page_wait elements never loaded or something.")
			print(e1)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	A non-generic method to iterate over a list on the website, append each 
	#	item into a list variable, and then return that variable
	#	If NoSuchElementException is encountered, break out of for loop and then allow the return
	#	of the variable list, as this exception simply means the end of website list was reached.
	#	If TimeoutException or Exception is encountered, return False since something went wrong
	##
	def get_PMC_list_wait_xpath(self):
		PMC_list = []
		for x in range(2, 110):
			try:
				if x < 10:
					the_PMC = self.driver_wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucCompanies_gvCompanies_ctl0%s_hlCompany']" % (x))))
				else:
					the_PMC = self.driver_wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucCompanies_gvCompanies_ctl%s_hlCompany']" % (x))))
				the_PMC_text = the_PMC.text
				PMC_list.append(the_PMC_text)
			except NoSuchElementException as e:
				print("End of PMC page")
				#print(e)
				break
			except TimeoutException as e1:
				print("get_PMC_list_wait_xpath element never loaded or something.")
				print(e1)
				return False
			except Exception as e0:
				print(e0)
				return False
		return PMC_list
	
	##
	#	Same as above but not using driver_wait
	##
	def get_PMC_list_xpath(self):
		PMC_list = []
		for x in range(2, 110):
			try:
				if x < 10:
					the_PMC = self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_ucCompanies_gvCompanies_ctl0%s_hlCompany']" % (x))
				else:
					the_PMC = self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_ucCompanies_gvCompanies_ctl%s_hlCompany']" % (x))
				the_PMC_text = the_PMC.text
				PMC_list.append(the_PMC_text)
			except NoSuchElementException as e:
				print("End of PMC page")
				break
			except Exception as e0:
				print(e0)
				return False
		return PMC_list

'''
##
#	child class that concentrates on a specific page of the website
##
'''
class PaymentsPage(Reusual):
	def __init__(self, driver, driver_wait):
		Reusual.__init__(self, driver, driver_wait)
	
	def load_payments_page(self):
		Reusual.load_url(self, "https://afakepaymentspage.com")

	##
	#	A non-generic method to display 100 results for this specific page
	##
	def load_more_results_payments_page_wait(self):
		try:
			self.driver_wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucPayments_pagingChanger']/option[4]"))).click()
			return True
		except NoSuchElementException as e:
			print("Invalid element for load_more_results_payments_page_wait")
			print(e)
			return False
		except TimeoutException as e1:
			print("load_more_results_payments_page_wait elements never loaded or something.")
			print(e1)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	Same as above but not using driver_wait
	##
	def load_more_results_payments_page(self):
		try:
			self.driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_ucPayments_pagingChanger']/option[4]").click()
			return True
		except NoSuchElementException as e:
			print("Invalid element for load_more_results_payments_page")
			print(e)
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	input data into date from field
	##
	def set_date_from_wait(self, month, day, year):
		date_final = "%s/%s/%s" % (month, day, year)
		
		try:
			date_from_field = self.driver_wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_dtDateFrom_dtDateFrom_dtFrom")))
			date_from_field.clear()
			time.sleep(.5)
			date_from_field.send_keys(date_final)
			return True
		except NoSuchElementException:
			print("Invalid element for set_date_from_wait")
			return False
		except TimeoutException:
			print("set_date_from_wait element never loaded or something.")
			return False

	##
	#	Same as above but not using driver_wait
	##	
	def set_date_from(self, month, day, year):
		date_final = "%s/%s/%s" % (month, day, year)
		
		try:
			date_from_field = self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_dtDateFrom_dtDateFrom_dtFrom")
			date_from_field.clear()
			time.sleep(.5)
			date_from_field.send_keys(date_final)
			return True
		except NoSuchElementException:
			print("Invalid element for set_date_from")
			return False
		except TimeoutException:
			print("set_date_from element never loaded or something.")
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	input data into date to field
	##
	def set_date_to_wait(self, month, day, year):
		date_final = "%s/%s/%s" % (month, day, year)
		
		try:
			date_to_field = self.driver_wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_dtDateTo_dtDateTo_dtFrom")))
			date_to_field.clear()
			time.sleep(.5)
			date_to_field.send_keys(date_final)
			return True
		except NoSuchElementException:
			print("Invalid element for set_date_to_wait")
			return False
		except TimeoutException:
			print("set_date_to_wait element never loaded or something.")
			return False
		except Exception as e0:
			print(e0)
			return False
	
	##
	#	Same as above but not using driver_wait
	##
	def set_date_to(self, month, day, year):
		date_final = "%s/%s/%s" % (month, day, year)
		
		try:
			date_to_field = self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_dtDateTo_dtDateTo_dtFrom")
			date_to_field.clear()
			time.sleep(.5)
			date_to_field.send_keys(date_final)
			return True
		except NoSuchElementException:
			print("Invalid element for set_date_to")
			return False
		except Exception as e0:
			print(e0)
			return False
	
	##
	#	Filter by PMC
	##
	def set_pmc_wait(self, pmc_name):
		try:
			pmc_field = self.driver_wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtSearchText")))
			pmc_field.clear()
			time.sleep(.5)
			pmc_field.send_keys(pmc_name)
			return True
		except NoSuchElementException:
			print("Invalid element for set_pmc_wait")
			return False
		except TimeoutException:
			print("set_pmc_wait element never loaded or something.")
			return False
		except Exception as e0:
			print(e0)
			return False
	
	##
	#	Same as above but not using driver_wait
	##
	def set_pmc(self, pmc_name):
		try:
			pmc_field = self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_txtSearchText")
			pmc_field.clear()
			time.sleep(.5)
			pmc_field.send_keys(pmc_name)
			return True
		except NoSuchElementException:
			print("Invalid element for set_pmc")
			return False
		except Exception as e0:
			print(e0)
			return False

	##
	#	Use Selenium's xpath wild card to create list variable containing data of requested information
	#	User will then utilize the list for whatever needs
	##
	def get_payment_information_wildcard(self, element_id):
		try:
			payment_info_list = []
			payment_info = self.driver.find_elements_by_xpath(element_id)
			
			for one_piece in payment_info:
				payment_info_list.append(one_piece.text)
				
			return payment_info_list
		except Exception as e0:
			print(e0)
			return False
