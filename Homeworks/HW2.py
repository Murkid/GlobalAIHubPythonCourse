#A program that asks the login details and check if the username and password is correct

users = {"ExampleUserName":"ExamplePassword" , "AnotherUser":"AnotherPassword"}  #Registered users

uname = input("Username:") #Asks for username
pwd = input("Password:") # Asks for password

if uname in users:
	if pwd==users[uname]:
		print("Login successfull.")
	else:
		print("Your password is wrong.")
else:
	print("That username doesn't exists.")
