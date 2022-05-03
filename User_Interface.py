from tkinter import *
from PIL import Image, ImageTk
import threading
import imageio
# create instance for window
root = Tk()
# set window title
root.title('Video Player')
# read video
video = imageio.get_reader('Atoms - 13232.mp4')
def display_video(label):
   # iterate through video data
   for image in video.iter_data():
      # convert array into image
      img = Image.fromarray(image)
      # Convert image to PhotoImage
      image_frame = ImageTk.PhotoImage(image = img)
      # configure video to the lable
      label.config(image=image_frame)
      label.image = image_frame
# create label for video
video_label = Label(root)
video_label.pack()
# create and start thread
thread = threading.Thread(target=display_video, args=(video_label,))
thread.start()
root.mainloop()


# from tkinter import *
# from tkvideo import tkvideo
# # create instance fo window
# root = Tk()
# # set window title
# root.title('Video Player')
# # create label
# video_label = Label(root)
# video_label.pack()
# # read video to display on label
# player = tkvideo("Atoms - 13232.mp4", video_label,
#                  loop = 1, size = (700, 500))
# player.play()
# root.mainloop()