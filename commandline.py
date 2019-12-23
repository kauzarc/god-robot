import random
import multiprocessing as mp
import time
from math import *


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
    result += "\n"
    result += "eval : @arg a python line --> return the result of the python line\n"
    return result


def log_command(text, file_name):
    result = ""
    if text[4:] == "show":
        f = open(file_name, "r")
        for line in f.readlines():
            result += line + "\n -------------------- \n"
        f.close()
        if len(result) > 1000:
            result = result[-1000:]

    elif text[4:] == "clear":
        f = open(file_name, "w")
        f.write("")
        f.close()
        result += "done !"

    return result


def no_command(text):
    return "Message invalide mother fucker ! (try @bot help)"


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


def eval_command(text):
    try:
        return str(eval(text[5:]))
    except Exception as e:
        return str(e)
