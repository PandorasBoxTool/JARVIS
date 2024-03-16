import psutil
import pyttsx3
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def system_stats():
    cpu_stats = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery().percent
    memory_in_use = convert_size(psutil.virtual_memory().used)
    total_memory = convert_size(psutil.virtual_memory().total)
    final_res = f"Aktuell werden {cpu_stats} Prozent der CPU verwendet, {memory_in_use} von RAM von insgesamt {total_memory}, und der Batteriestand beträgt {battery_percent} Prozent."
    return final_res

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

