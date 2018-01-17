import aiml
import warnings

warnings.filterwarnings("ignore")

kernel = aiml.Kernel()
kernel.learn("startup.xml")
kernel.respond("load aiml b")



while True:
    a = kernel.respond(input("Enter your message >> ").upper())
    print(a)