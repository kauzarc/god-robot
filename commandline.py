import random


def help_command(text):
    result = "HELP :\n"
    result += "\n"
    result += "help : --> show help\n"
    result += "\n"
    result += "test : --> a testing command\n"
    result += "\n"
    result += "random : @arg an integer --> pick a random number between 0 and @arg\n"
    return result


def no_command(text):
    return "Message invalide mother fucker !"


def test_command(text):
    return "This command work !"


def random_command(text):
    return "nique sa mere"
