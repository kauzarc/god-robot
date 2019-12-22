import random

def no_command(text):
    return "Message invalide mother fucker !"

def test_command(text):
    return "This command work !"

def random_command(text):
    return str(random.randint(0, int(text)))