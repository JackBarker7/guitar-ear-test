from playsound import playsound
import random
from tkinter import *
import time
from sys import exit
#this is a test


root=Tk()
root.attributes('-fullscreen', True)
labels = []

CHORDS = {"I":"D",
          "ii":"Em",
          "iii":"F#m",
          "IV": "G",
          "V": "A",
          "V7": "A7",
          "vi":"Bm"}

NUMS = ["I","ii","iii","IV","V","V7","vi"]

def playChords():
    
    time.sleep(5)
    labels = []
    random.shuffle(NUMS)
    playsound("tonic.wav")
    playsound("metronome.wav")
    
    playsound(CHORDS[NUMS[0]]+".wav")
    playsound(CHORDS[NUMS[1]]+".wav")
    playsound(CHORDS[NUMS[2]]+".wav")
    playsound(CHORDS[NUMS[3]]+".wav")
    time.sleep(8/3)

    playsound("tonic.wav")
    playsound("metronome.wav")
    
    playsound(CHORDS[NUMS[0]]+".wav")
    playsound(CHORDS[NUMS[1]]+".wav")
    playsound(CHORDS[NUMS[2]]+".wav")
    playsound(CHORDS[NUMS[3]]+".wav")
    time.sleep(5)
    
    for i in range(0,4):
        labels.append(Label(root, text = NUMS[i], width = 4, font = ("Courier",300)))
        if i<=1:
            labels[i].grid(row = 2, column = i)
        else:
            labels[i].grid(row = 3, column = i-2)

    
    return NUMS[0:4]
    


tmp = playChords()
print(tmp)

again = Button(root, width = 15, text = "PLAY AGAIN", command = playChords, font = ("Courier",50))
again.grid(row = 4, column = 0)

finish = Button(root, width = 15, text = "EXIT", command = exit, font = ("Courier",50))
finish.grid(row = 4, column = 1)
root.mainloop()
