# pip install click-shell

from click_shell import shell

@shell(prompt="luci-shell > ", intro="""
welcome to the luci shell! if you want to see a list of all available commands, enter "help"
""")
def luci_shell():
    pass

@luci_shell.command()
def help():
    print("""here is a list of all commands:

help: see this list
hello-world: prints a message
add: add two numbers
create-file: create new file and write into it
exit: exit the shell
""")

@luci_shell.command()
def hello_world():
    print("hello world!")

@luci_shell.command()
def add():
    n1 = float(input("enter the first number: "))
    n2 = float(input("enter the second number: "))
    print(n1 + n2)

@luci_shell.command()
def create_file():
    file_name = float(input("enter the file name: "))
    content = float(input("enter the file content: "))
    with open(file_name, "w") as f:
        f.write(content)



if __name__ == "__main__":
    luci_shell()

