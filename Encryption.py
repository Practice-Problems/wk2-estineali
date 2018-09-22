s = "have a nice day"

def encrypt(message):
	stripped_message = message.replace(" ", "")

	rows = int(len(stripped_message)**0.5)
	collumns = int(len(stripped_message)**0.5) + 1

	encrypted_raw = ["" for i in range(rows)]

	for i in range(len(stripped_message)):
		encrypted_raw[i%rows] += stripped_message[i]
	encrypted = ""
	for i in range(rows):
		encrypted += encrypted_raw[i] 
		encrypted += " "
	return encrypted

print(encrypt(s))


