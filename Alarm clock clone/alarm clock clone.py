from tkinter import * 
import datetime 
import winsound

root = Tk()
root.geometry("400x200")

def alarm() : 
  set_alarm_time = f"{hour.get()}:{min.get()}:{sec.get()}"
  def check_alarm() :
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time, set_alarm_time)
    if current_time == set_alarm_time :
      print('Time to wake up')
      winsound.PlaySound('sound.nav', winsound.SND_ASYNC)
    else : 
      root.after(1000, check_alarm)
  check_alarm()

Button(root, text="Set alarm", font=("Helvetica 15"), command=alarm).pack(pady=20)
Label(root, text="Alarm clock", font=("Helvica 20 bold"), fg="red").pack()
Label(root, text="Set time", font=("Helvica 15 bold")).pack()

frame = Frame(root)
frame.pack()




hour = StringVar(root)
hour.set("00")
OptionMenu(frame, hour, *map(lambda x : f"{x:02}", range(25))).pack(side=LEFT)

min = StringVar(root)
min.set("00")
OptionMenu(frame, min, *map(lambda x : f"{x:02}", range(60))).pack(side=LEFT)

sec = StringVar(root)
sec.set("00")
OptionMenu(frame, sec, *map(lambda x : f"{x : 02}", range(60))).pack(side=LEFT)

root.mainloop()

