import aiml
import warnings
from random import choice

warnings.filterwarnings("ignore")

kernel = aiml.Kernel()
#kernel.learn("startup.xml")
#kernel.respond("load aiml b")
kernel.bootstrap(brainFile='brain.brn')


if __name__ =='__main__':
    while True:
        a = kernel.respond(input("Srikumar >> ").upper())
        if not a:
            print(''.join(choice(['Was that a typo?',
                                  "I am afraid, I can't understand",
                                  'Am I overfitted on data?, coz I can\'t get that one!',
                                  'Correct your grammar probably?'])))
        print(a)