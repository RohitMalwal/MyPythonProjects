import time
from win32com.client import Dispatch

speak = Dispatch('SAPI.SpVoice')
voices = speak.getVoices()
speak.voice
speak.SetVoice(voices.item(1))

a = (time.strftime('%I:%M:%S'))
 
name = input("Enter Your Name: ")
Tell = int(input("0 for Miss / 1 for Mr. / 2 for Mrs. : "))
if Tell == 0:
    gender = 'Miss'
elif Tell == 1:
    gender = 'Mr.'
elif Tell == 2:
    gender = 'Mrs.'
else:
    exit
c = name.title()

b = int(time.strftime("%H"))

if (00 <= b < 6):
    print(f"Good Night {gender} {c} It is {a}")
    speak.speak(f"Good Night {gender} {c}.")
elif (6 <= b < 12):
    print(f"Good Morning {gender} {c} It is {a}")
    speak.speak(f"Good Morning {gender} {c}.")
elif (12 <= b < 16):
    print(f"Good Afternoon {gender} {c} It is {a}")
    speak.speak(f"Good Afternoon {gender} {c}.")
else:
    print(f"Good Evening {gender} {c} It is {a}")
    speak.speak(f"Good Evening {gender} {c}.")
