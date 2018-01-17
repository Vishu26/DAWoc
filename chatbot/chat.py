import aiml
import warnings
from random import choice

warnings.filterwarnings("ignore")

kernel = aiml.Kernel()
kernel.learn("startup.xml")
kernel.respond("load aiml b")



while True:
    a = kernel.respond(input("Enter your message >> ").upper())
    if not a:
        print(''.join(choice(['Was that a typo?',
                              "I am afraid, I can't understand",
                              'Am I overfitted on data?, coz I can\'t get that one!',
                              'Correct your grammar probably?'])))
    print()