from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as file_key:
        file_key.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter your Master Password: ")
key = load_key()
fer = Fernet(key)

def add():
    name = input("Account Name:  ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + " | "+ fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()

            user, password = data.split("|", 1)  # Limit to one split
            decrypted_password = fer.decrypt(password.encode()).decode()
            print("User:", user, "Password:", decrypted_password)

while True:
    mode = input("Would you like to add a new password or view existing password (view/add) or q to Quit: ").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid Mode.")
        continue