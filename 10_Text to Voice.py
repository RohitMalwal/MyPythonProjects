import win32com.client as wincl

speak = wincl.Dispatch('SAPI.SpVoice') 
voice = speak.GetVoices()
speak.Voice 
speak.SetVoice(voice.Item(1))
print(voice.Item(2).GetAttribute('Name')) # to print the name of voice

with open(r'D:\sample.txt', encoding="utf-8") as file:
    for line in file.readlines():
        print(line)
        speak.speak(line)