# pip install cryptography

from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        # print(self.key)
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]

# pm = PasswordManager()
# # pm.create_key(None)
# pm.create_key("mykey.key")

def main():
    password = {
        "email": "1234567",
        "facebook": "myfbpassword",
        "email": "helloworld123",
        "email": "myfavoritepassword_123"
    }

    pm = PasswordManager()

    print("""what do you want to do?
    (1) create a new key
    (2) load an existing key
    (3) create new password file
    (4) load existing password file
    (5) add a new key
    (6) get a password
    (q) quit
    """)

    done = False

    while not done:
        choice = input("enter your choice: ")
        if choice == "1":
            path = input("enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("enter path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input("enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input("enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            site = input("enter the site: ")
            password = input("enter the password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input("what site do you want: ")
            print(f"password for {site} is {pm.get_password(site)}")
        elif choice == "q":
            done = True
            print("Bye")
        else:
            print("invalid choice!")

if __name__ == "__main__":
    main()