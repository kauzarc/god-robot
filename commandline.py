import random


def help_command(text):
    result = "HELP :\n"
    result += "\n"
    result += "help : --> show help\n"
    result += "\n"
    result += "test : --> a testing command\n"
    result += "\n"
    result += "random : @arg an integer --> pick a random number between 0 and @arg\n"
    result += "\n"
    result += "say : @arg any string --> reapeat @arg\n"
    return result

def log_command(text, file_name):
    f = open(file_name, "r")
    result = ""
    for line in f.readlines():
        result += line + "\n -------------------- \n"
    return result

def no_command(text):
    return "Message invalide mother fucker !"


def test_command(text):
    return "This command work !"


def random_command(text):
    string = text[7:]
    for letter in string:
        if not letter in "0123456789":
            return "non valid arg !"

    integer = int(string)
    return str(random.randint(0, integer))


def say_command(text):
    return text[4:]
