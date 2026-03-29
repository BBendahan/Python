import threading
import time 

def walk_dog(name, surname):
    time.sleep(8) 
    print(f"Walking {name} {surname}")

def take_out_trash():
    time.sleep(5)
    print("Taking out the trash...")

def get_mail(name):
    time.sleep(3)
    print(f"Getting the mail for {name}")

# print('sin threading:')
# walk_dog()
# take_out_trash()
# get_mail()

print('con threading:')
thread1 = threading.Thread (target=walk_dog, args=('Apolo', 'Bendahan'))
thread2 = threading.Thread (target=take_out_trash)
thread3 = threading.Thread (target=get_mail, args=("Mauro"))

thread1.start()
thread2.start()
thread3.start()

print ('all tasks started.')
thread1.join()
thread2.join()
thread3.join()

print ('All tasks completed.')