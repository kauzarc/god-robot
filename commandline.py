import random

def help_command(text):
    result = "HELP :\n"
    result += "\n"
    result += "test : a testing command\n"
    result += "random : @arg an integer\n"
    return result

def no_command(text):
    return "Message invalide mother fucker !"

def test_command(text):
    return "This command work !"

def random_command(text):
    return str(random.randint(0, int(text)))