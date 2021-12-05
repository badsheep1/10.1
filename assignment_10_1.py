#Name: Andrew Xu
#Assignment: 10.1


import time
class Contacts: #A Contacts Class is created, its purpose is to model after messenger applications or your phone's contact list, where it stores
# Contacts name and essential information. And from this you can perform other tasks.
	status = "offline" # A class variable known as status, will be accessible for everyone and will remain as offline, since the texting mechanic only allows once sided messaging, it made the most sense to make all contacts offline.
	def __init__(self, name, number): # Initializes four attributes.
		self.__name = name # Taking in instance varaiables and passing them as private attributes.
		self.__number = number
		self.__contactbio = "" # This data variable simulates one of many information that can be stored in contacts.
		self.__nickname = "" # Another data variable that simulates a common information label in modern contact lists.
		
	def add_contact(self): #Class Method created.
		try: # This Try and following exerpt statements is in anticipation a raised error related to a file not existing.
			names_bank = [] # An empty list is created to store things.
			f = open("contact_list.txt", "r") #The file Contact_list is opened in read mode.
			for namez in f.readlines(): # The readlines method takes lines from the file and takes them in as list items.
				commaloc = namez.find(",") # the find method finds the index of the commas location, it is then saved as a variable.
				t = namez[:commaloc] #Using the index, it is spliced so that it includes everything in the string before the comma.
				names_bank.append(t) # The empty list then appends that string.
			if self.__name in names_bank: # Checks if the name of the object is in the list.
				print(f"{self.__name} already exists in your contacts list, you cannot add a contact more than once.") #That method returns a dictionary, it checks if the name exists as a key, if it does, it prints this statement.
			else: #An else statement that executes the following block of code, if the if statement's condition fails.
				f = open("contact_list.txt", "a") #It opens a file in "append mode." If this file does not exist, it creates one, and if it does, it allows editing of the file in its current state.
				f.write(f"{self.__name}, {self.__number}\n") # It writes a string that includes the name and number.
				f.close() # Closes the file once its done with it.
				print(f"{self.__name} has been added to your contacts list.") # Afterwards prints out a string confirming that a contact has been added.
		except FileNotFoundError: # If the file does not exist already, the following code creates it and does other stuff.
			f = open("contact_list.txt", "a") #It opens a file in "append mode." If this file does not exist, it creates one, and if it does, it allows editing of the file in its current state.
			f.write(f"{self.__name}, {self.__number}\n") # It writes a string that includes the name and number.
			f.close() # Closes the file once its done with it.
			print(f"{self.__name} has been added to your contacts list.") # Afterwards prints out a string confirming that a contact has been added.

		
	
	def remove_contact(self): # A remove contact method is created.
		all_names = [] # An empty list is created to store these keys.
		f = open("contact_list.txt", "r") # opens the file in read mode
		for contacts in f.readlines():  # iterates through the lines of the file.
			point = contacts.find(",") # finds the index of the comma
			k = contacts[:point]
			all_names.append(k)
		contact_holder = [] # ANother empty list is created.
		if self.__name in all_names: # An if statement that see if the inputed string by the user is in the list that stores all contact names.
			f = open("contact_list.txt", "r") #if that condition is met, then the contact_list.txt file is opened in "read" mode.
			for contact_info in f.readlines(): # f.readlines() is a method that creates a list consisting of lines from the file, this for loop then iterates through all of them.
				split_point = contact_info.find(",") # A variable finds the index in which the comma is found.
				contact_name = contact_info[:split_point] # Then uses it to splice off the comma and everything that is after it, leaving only the name portion.
				if self.__name == contact_name: # An if statement checks if the inputed string is equal to the string of the name.
					continue # if it does, that the loop moves on to the next interation, not doing anything.
				else:
					contact_holder.append(contact_info) #If the name isn't equal, then it is appended into an empty string.
			f.close()

			o = open("contact_list.txt", "w") #The contact list is open in "write" mode, which over rides the previous file and starts a new.
			for lines in contact_holder: # Each of the strings in the list will be iterated through.
				if lines != "\n": #if the lines is not equal to the \n character
					o.write(f"{lines}")# It is written in
				else:
					continue # if not it iterates past it, getting rid of it.
			o.close()
		else:
			print("This contact does not exist, please try again.")
			#if the first if statement fails, then only a string plays out, not the entire block of code before this.
					
	def open_contacts(self): # a simple method that prints out a header, and then prints out all items out of the
		try:
			print("Phone List Contacts.")# Prints out the header
			f = open("contact_list.txt", "r") #opens the file in read mode
			for lines in f.readlines():
				print(f"({lines[:-1]})") #Prints everything out individually
		except FileNotFoundError:
			print("Contacts List\nEmpty...") #If the file doesn't exist a string will be printed out.

############# Get Set Methods ################################################################################################
	def set_contact_bio(self): # Get method for contact bio is created.
		bio_input = input("Leave a Bio or a note for this contact.") # Accepts a users input stores it as a variable.
		self.__contactbio += str(bio_input) # it is being added to and equal to the existing public attribute data variable
	
	def get_contact_bio(self): # This method actually prints out the variable
		if self.__contactbio != "":
			print(self.__contactbio)
		else: #The if statement checks if is not equal to an empty string, the pre-set. If it is it assumes that no bio has been set, and prints this string out.
			print("You have not set a bio for this contact.") 


	def set_contact_nickname(self):# This uses the same method as for the bio.
		nickname = input("Input a Nickname for your Contact.")
		self.__nickname += str(nickname)
	
	def get_contact_nickname(self):
		if self.__nickname != "":
			print(self.__nickname)
		else:
			print("You have not set a nickname for this contact.")

	

class Messenger: # A Class that models after messengers software, with methods that help create a messaging
#environment, where you may select a contact, send messages instantaneously, leave and return.

	def __init__(self, name, number): # Constructor method inherits the attributes of name and number from Contacts.
		self.__name = name
		self.__number = number

	def text(self): # A text method is created.
		try: # A try method is created in anticipation for a Raised Error.
			contact_chatlog = self.__name.replace(" ","_").lower() +"_chatlog.txt" # A variable holds a concatenated string, the private attribute for name, is converted to lower case letters, has its comma space replaced by a _, and at the end has a string of _chatlog.txt attatched to it.
			file_reader = open(contact_chatlog, "r") # That variable holding then string is then opened as a text under read mode.
			for lines in file_reader.readlines(): # A for loop is created that iterates through the the lines of the chatlog text file.
				print(f"{lines}") # Then prints out each of the lines.
		except FileNotFoundError: # A file not found error is raised, if that file does not exist already.
			print(f"This is the beginning of your Direct Message History with {self.__name}") # A messege prints out.
		while True: # A True loop is created.
			message = input(f"Message {self.__name}:") # a variables stores an input of a user.
			end_convo = ["ttyl", "bye", "I'm done talking to you", "gtg"] # A list of strings is stored.
			if message not in end_convo: # Checks if the user input is not equal to a string inside the list.
				f = open(contact_chatlog, "a") # if not, then the text file is opened in append mode
				f.write(f"\t\t{message}\n") # Any of the users inputs will be written in there with tabs and a new line.
				f.close() # file is closed.
				print(f"\t\tYou:\n\t\t{message}") # the message is printed out in the terminal.
			else: # if it is in the list.
				print(message) # The message is printed out in the terminal.
				break # And then the while loop is broken.

	def search_contacts(self): # A search contacts method is created.
		contact_database = [] # an empty string is created.
		print("Contacts list:")# a header is printed out in the terminal

		contact_database = [] # An empty list is created to store these keys.
		f = open("contact_list.txt", "r")
		for contacts in f.readlines():
			print(contacts)
			point = contacts.find(",") # This is the same method, of checking for existing contacts in the file document.
			k = contacts[:point]
			contact_database.append(k)

		contact_input = input("Enter the name of the contact you are trying to text: >>>") # A variable stores a user input
		if contact_input in contact_database: # The code below is the copy of the text method.
			try: 
				inputed_contact = contact_input.replace(" ","_").lower() +"_chatlog.txt" # This variable catenates the name given by the user, after it is modified to be lowercased and had space replaced,
				file_reader = open(inputed_contact, "r") #It is now opened as a file in read mode.
				for lines in file_reader.readlines():
					print(f"{lines}")
			except FileNotFoundError: # given the chance that the file may not exist, And passes this exception statement.
				print(f"This is the beginning of your Direct Message History with {contact_input}")
			while True: #Everything below is the same as the text().
				message = input(f"Message {contact_input}:")
				end_convo = ["ttyl", "bye", "I'm done talking to you", "gtg"]
				if message not in end_convo:
					f = open(inputed_contact, "a")
					f.write(f"\t\t{message}\n")
					f.close()
					print(f"\t\tYou:\n\t\t{message}")
				else:
					print(message)
					break
		else: # However this else statement prints out a unique message for if your input does not match an existing contact.
			print("Sorry but the contact you just inputed does not exist, try saving it in the contact list first.")
	



def main():
	print("The Following is the Demonstration of the Contacts Class and its methods.")
	john = Contacts("John Doe", "545-435-4231") # A bunch of objects are created from the class Contacts.
	jill = Contacts("Jill Doe", "435-314-4213") # The first attribute is the name, and the second is the phone number.
	jack = Contacts("Jack Trade", "534-342-5321")
	melissa = Contacts("Melissa Lee", "530-452-4231")
	joao = Contacts("Joao Pedro", "543-414-5431")

	jack.open_contacts() #This is the jack object with a open contacts method attatched to it.
	#Note that this method relies on a certain file to exist in order to read from it, this method accounts for this error and will display a string stating that the contacts list is empty.
	jack.add_contact()#The add method is used here to the jack object, and creates a text file and writes the name and number attribute in.
	jill.add_contact() # The same are done for the Jill, Melissa, and Joao objects.
	melissa.add_contact()
	joao.add_contact()
	joao.open_contacts() # Finally the open_contacts() method is used, and all of the contacts are printed out

	jill.remove_contact() # The remove method is used here, to remove the jill contact
	jill.open_contacts() # All of the contacts are printed out, to show that the contact is actually gone.
	time.sleep(2)

	print("The Following is the Demonstration of the get-set Methods and the Class Variable.")
	joao.get_contact_bio() # This is executed before the set_contact_bio method is used, showing what happens if you don't set it before hand.
	time.sleep(1)
	joao.set_contact_bio() #Now it is actually set, the user may input anything they wish.
	joao.get_contact_bio() # Now this method is tried again, this time displaying the players input
	time.sleep(1)
	jack.get_contact_bio()# here it demonstrates how the data variables are different for other objects.
	# the bio for joao is set, but not for jack.
	time.sleep(1)
	jack.get_contact_nickname() # The get_contact_nickname() is executed before the set version, displaying what happens if you dont set your nicknames before.
	jack.set_contact_nickname()# now the user can set a nickname
	jack.get_contact_nickname()# and then call it.
	time.sleep(1)
	print(melissa.status) #This is calling the class variable, all objects made from this class will have access to this variable
	time.sleep(1)
	print(joao.status) # here it demonstrates another object of this class, having access to this variable
	time.sleep(1)
	print("The Following is the Demonstration of the Messenger Class, and its methods.")
	
	texting_joao = Messenger("Joao Pedro", "543-414-5431") # AN object is created from the Messenger Class.
	
	texting_joao.text() #Demonstrating the text Method, User may type in what every they want as messenges
	# But can only end this method using 1 of 4 key words and terms.
	texting_joao.search_contacts() # The user here has the ability to do the text() method's function with any contact, 
	# it will first prompt them to type in a valid contact name, it will display all available ones first.
	texting_joao.text() # THis demonstrates the methods ability to dispay old text messages from an existing chatlog file.
	#The first time, it only printed a string saying that it was the start of the chat history, here it prints out everything typed before
	#before allowing the user to enter more messages.

if __name__ == "__main__":
	main()




		

