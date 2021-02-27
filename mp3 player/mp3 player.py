from tkinter import *
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root=Tk()

root.title("MP3 Player")
root.geometry("500x300")

#Initialize Pygame
pygame.mixer.init()

#Create Function to deal with time
def play_time():

    #Check if song is stopped
    if stopped:
        return

    #Grab current song time
    current_time=pygame.mixer.music.get_pos()/1000 #"get_pos"-->it is returning milliseconds.

    #Convert song time to time format
    converted_current_time=time.strftime('%M:%S',time.gmtime(current_time))

    # Add current time to status bar
    # status_bar.config(text=f'Time Elapsed :{converted_current_time} of {converted_song_length} ')
    

    #Create loop to check time every second
    status_bar.after(1000,play_time) #every second this function will run again.

    #Reconstruct song with directory structure stuff.
    song=playlist_box.get(ACTIVE)
    song=f"E:/Python Tutorials/programs/mp3 player/audio/{song}.mp3"

    #Find current song length
    song_mut=MP3(song)
    global song_length
    song_length=song_mut.info.length

    #Convert to time format
    converted_song_length =time.strftime('%M:%S',time.gmtime(song_length))
    # my_label.config(text=converted_song_length)

    if int(song_slider.get())==int(song_length): #we have converted them to integer so that they can easily sink up.
        stop()

    elif paused:#check to see if paused,is so-- end.
        pass

    else:
        #Move slider along 1 second at a time
        next_time=int(song_slider.get()) +1

        #Output new time value to slider,and to length of the song
        song_slider.config(to=song_length,value=next_time)

        #Convert slider position to time format
        converted_current_time=time.strftime('%M:%S',time.gmtime(int(song_slider.get())))

        #Output slider
        status_bar.config(text=f'Time Elapsed :{converted_current_time} of {converted_song_length} ')





    #Add current time and length to status bar
    if current_time>=1:
        status_bar.config(text=f'Time Elapsed :{converted_current_time} of {converted_song_length} ')
    


#Create function to add one song to playlist
def add_song():
    song=filedialog.askopenfilename(initialdir="audio/",title="Choose a Song",filetypes=(("mp3 Files","*.mp3"),))
    #the name of the song we selected will come into "song" variable.

    #strip out directory structure and .mp3 from song title
    song=song.replace("E:/Python Tutorials/programs/mp3 player/audio/", "")
    song=song.replace(".mp3", "")

    #Add to end of playlist.
    playlist_box.insert(END,song)

#Create function to add many songs in playlist

def  add_many_songs():
    songs=filedialog.askopenfilenames(initialdir="audio/",title="Choose a Song",filetypes=(("mp3 Files","*.mp3"),))
    #LOOP THROUGH SONG LIST AND REPLACE DIRECTORY STRUCTURE AND MP3 FROMFRROM SONG NAME
    for song in songs:
        song=song.replace("E:/Python Tutorials/programs/mp3 player/audio/", "")
        song=song.replace(".mp3", "")
        
        #Add to end of playlist.
        playlist_box.insert(END,song)


#CREATE FUNCTION TO DELETE ONE SONG FROM PLAYLIST
def delete_song():
    playlist_box.delete(ANCHOR)# ANCHOR ---> is basically what we have selectedor highlighted.

# CREATE FUNCTION TO DELETE ALL SONGS FROM PLAYLIST
def delete_all_songs():
    playlist_box.delete(0,END)  # delete all the songs.

#CREATE PLAY FUNCTION
def play():

    #Set stopped to False since  the song is now playing
    global stopped
    stopped=False

    #Reconstruct song with directory structure stuff.
    song=playlist_box.get(ACTIVE)
    song=f"E:/Python Tutorials/programs/mp3 player/audio/{song}.mp3"
    
    #Load song with pygame mixer
    pygame.mixer.music.load(song)

    #Play song with pygame mixer
    pygame.mixer.music.play(loops=0)  #loops=0  basically means play the song just one time .

    #Get song time
    play_time()

#Create stopped variable
global stopped
stopped= False  #by default

#Create stop function
def stop():
    #stop the song
    pygame.mixer.music.stop()

    #clear playlist bar
    playlist_box.selection_clear(ACTIVE)

    status_bar.config(text='')

    #Set our slider to zero
    song_slider.config(value=0)

    #Set stop variable to true
    global stopped
    stopped=True

# create "paused" variable
global paused
paused= False # by default value of paused is 'False'.

#Create pause function
def pause(is_paused):
    global paused
    paused=is_paused

    if paused:  # if paused is true i.e. the song is paused.
        #Unpause
        pygame.mixer.music.unpause()
        paused=False
    else:
        #Pause
        pygame.mixer.music.pause()
        paused=True

#Create function to play next song
def next_song():

    #Reset slider position in status bar
    status_bar.config(text='')
    song_slider.config(value=0) #so when the next song plays value is set to 0 at song slider again.

    #Get current song number
    next_one =playlist_box.curselection() #will tell our current selection
    # my_label.config(text=next_one)

    #playlist_box.curselection()--> basically returns a list thats why we have written 'next_one=next_one[0]+1'
   
    #Add one to the current Song number tuple/list.
    next_one=next_one[0]+1

    #Grab the song title from the playlist.
    song=playlist_box.get(next_one)

    # Add directory structure stuff to the song
    song=f"E:/Python Tutorials/programs/mp3 player/audio/{song}.mp3"

    #Load song with pygame mixer
    pygame.mixer.music.load(song)

    #Play song with pygame mixer
    pygame.mixer.music.play(loops=0)
    
    #Clear active bar in playlist
    playlist_box.selection_clear(0,END)

    #Move active bar to next song
    playlist_box.activate(next_one)

    #set active bar to next song
    playlist_box.selection_set(next_one,last=None)

    #Its working now because now the song is being selected and earlier it was not.

#Create function to play previous song.
def previous_song():
    #Reset slider position in status bar
    status_bar.config(text='')
    song_slider.config(value=0) #so when the next song plays value is set to 0 at song slider again.

    #Get current song number
    next_one =playlist_box.curselection() #will tell our current selection
    # my_label.config(text=next_one)

    #playlist_box.curselection()--> basically returns a list thats why we have written 'next_one=next_one[0]+1'
   
    #Add one to the current Song number tuple/list.
    next_one=next_one[0]-1

    #Grab the song title from the playlist.
    song=playlist_box.get(next_one)

    # Add directory structure stuff to the song
    song=f"E:/Python Tutorials/programs/mp3 player/audio/{song}.mp3"

    #Load song with pygame mixer
    pygame.mixer.music.load(song)

    #Play song with pygame mixer
    pygame.mixer.music.play(loops=0)
    
    #Clear active bar in playlist
    playlist_box.selection_clear(0,END)

    #Move active bar to next song
    playlist_box.activate(next_one)

    #set active bar to next song
    playlist_box.selection_set(next_one,last=None)

#CREATE VOLUME FUNCTION
def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    # volume_slider.get()---> gives us the position of where our slider is .


#CREATE SLIDE FUNCTION FOR SONG POSITIONING
def slide(x):
    #Reconstruct song with directory structure stuff.
    song=playlist_box.get(ACTIVE)
    song=f"E:/Python Tutorials/programs/mp3 player/audio/{song}.mp3"
    
    #Load song with pygame mixer
    pygame.mixer.music.load(song)

    #Play song with pygame mixer
    pygame.mixer.music.play(loops=0,start=song_slider.get()) #will get the posn of the slider and run the song from there.



#CREATE MAIN FRAME
main_frame = Frame(root)
main_frame.pack(pady=20)

#Create Playlist Box
playlist_box =Listbox(main_frame,bg="black" ,fg="green",width=60,selectbackground="green",selectforeground="black")
playlist_box.grid(row=0,column=0)


#CREATE VOLUME SLIDER FRAME
volume_frame =LabelFrame(main_frame,text="Volume")
volume_frame.grid(row=0,column=1,padx=20)

# Create volume slider
volume_slider=ttk.Scale(volume_frame,from_=0 ,to =1,orient=VERTICAL,length=125,value=1,command=volume)
volume_slider.pack(pady=10)

# Create song slider
song_slider=ttk.Scale(main_frame,from_=0 ,to =100,orient=HORIZONTAL ,length=360 ,value=0,command=slide)
song_slider.grid(row=2,column=0,pady=20)

#DEFINE BUTTON IMAGES FOR CONTROLS
# back_btn_img=PhotoImage(file='images/back.jpg')
# forward_btn_img=PhotoImage(file='mp3 player/forward.jpg')
# play_btn_img=PhotoImage(file='mp3 player/play.jpg')
# pause_btn_img=PhotoImage(file='mp3 player/pause.jpg')
# stop_btn_image=PhotoImage(file='mp3 player/stop.jpg')

#CREATE BUTTON FRAME
control_frame=Frame(main_frame)
control_frame.grid(row=1,column=0)

#create play/stop etc buttons
back_button=Button(control_frame,text="Back",command=previous_song)
back_button.grid(row=0,column=0,padx=10)

forward_button=Button(control_frame,text="Forward",command=next_song)
forward_button.grid(row=0,column=1,padx=10)

play_button=Button(control_frame,text="Play",command=play)
play_button.grid(row=0,column=2,padx=10)

pause_button=Button(control_frame,text="Pause",command=lambda: pause(paused))
pause_button.grid(row=0,column=3,padx=10)

stop_button=Button(control_frame,text="Stop",command=stop)
stop_button.grid(row=0,column=4,padx=10)


#CREATE MAIN  MENU
my_menu=Menu(root)
root.config(menu=my_menu)


#CREATE ADD SONG MENU DROPDOWNS
add_song_menu= Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)

#Add one song to playlist
add_song_menu.add_command(label="Add one Song To Playlist",command=add_song)

#Add many songs to playlist
add_song_menu.add_command(label="Add many Songs To Playlist",command=add_many_songs)

# CREATE DELETE SONG MENU DROPDOWNS
remove_song_menu= Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Remove Songs",menu=remove_song_menu)

#Delete one song from playlist
remove_song_menu.add_command(label="Delete a song from Playlist",command=delete_song)

#Delete all songs from playlist
remove_song_menu.add_command(label="Delete all songs from Playlist",command=delete_all_songs)


#CREATE STATUS BAR
status_bar=Label(root,text="",bd=1,relief=GROOVE,anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)
#ipad-->gives internal padding

#TEMPORARY LABEL #is made to check what it is printing on the screen.
my_label=Label(root,text="")
my_label.pack(pady=20)


root.mainloop()
