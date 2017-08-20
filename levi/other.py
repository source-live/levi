print("Levi AI started")
from Tkinter import *
from pyttsx import *
from midiutil.MidiFile import MIDIFile
import turtle
import random
import winsound

def say(text):
  levi = init()
  levi.say(text)

# Define moving functions
def go_right(step):
     turtle.setheading(0)
     turtle.forward(step)

def go_up(step):
     turtle.setheading(90)
     turtle.forward(step)


def go_left(step):
     turtle.setheading(180)
     turtle.forward(step)

def go_down(step):
     turtle.setheading(270)
     turtle.forward(step)

def levi_draw(step_size, step_number):
    move_dict = {1: go_up,
                 2: go_right,
                 3: go_left,
                 4: go_down
                 }
    for _ in range(step_number):
        move_in_a_direction = move_dict[random.randint(1, 4)]
        move_in_a_direction(step_size)

def midiwrite():
    # Define variables
    pitches = [60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
    beats = [1,2,3,4,5,6,7]
    times = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,21,22,23,24,25,26,27,28,29,30]
    
    mf = MIDIFile(1)
    mf.addTrackName(1, 0, "Track1")
    mf.addTempo(1, 0, 120)
    
    
    channel = 0
    volume = 100
    duration = random.choice(beats)
    pitch = random.choice(pitches)
    time = random.choice(times)
    mf.addNote(track, channel, pitch, time, duration, volume)

class Levi:
  bgcolors = ['blue','white','orange','red','black','green','gray']
  def __init__():
    # Start window
    root = Tk()
    root.Title("Levi")
    
    # Say intro.
    say('Levi AI started.')
    say('I am an advanced artifficial intelligence that draws art.')
    
    # Run pen tests.
    turtle.penup()
    turtle.pendown()
    turtle.penup()
    turtle.forward()
    say('Ran pen tests.  I am ready to go!')
    
    # Choose background color.
    bgc = random.choice(bgcolors)
    turtle.bgcolor(bgc)
    say('Changed background color to ' + bgc)
    
    if bgc == 'blue':
      turtle.pencolor('white')
    elif bgc == 'white':
      turtle.pencolor('black')
    elif bgc == 'orange':
      turtle.pencolor('white')
    elif bgc == 'red':
      turtle.pencolor('white')
    elif bgc == 'black':
      turtle.pencolor('white')
    elif bgc == 'green':
      turtle.pencolor('white')
    elif bgc == 'gray':
      turtle.pencolor('white')
      
    turtle.clear()
    say('I have changed the pen color to match the background.  I have also cleared the screen in case of marks.')
    
    # Start drawing
    say('I will now start drawing.')
    turtle.hideturtle()
    turtle.speed("fastest")
    levi_draw(15, 1000)
    
    # Make a song
    say('I will now make a song.')
    
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    midiwrite()
    with open('levi.mid', 'a+') as outf:
      mf.writeFile(outf)
      
    say('I have now drawn something and made a song.')
    winsound.PlaySound('levi.mid', winsound.SND_FILENAME)
    say('That is my song.')
    
    say('I will now generate another art.')
