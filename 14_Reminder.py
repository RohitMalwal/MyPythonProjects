from plyer import notification
from win32com.client import Dispatch

speak = Dispatch('SAPI.SpVoice') 
voice = speak.GetVoices()
speak.Voice 
speak.SetVoice(voice.Item(0)) 

notification.notify(
    title = 'Reminder: Stay Hydrated! 💧',
    message = "It's time to drink a glass of water. Keeping hydrated helps you stay focused and energized throughout the day. Cheers to good health!",
    app_icon = 'D:/7tsp/logo/favicon.ico',
    timeout = 4
    )
speak.speak("Hey Rohit, time to drink a glass of water")