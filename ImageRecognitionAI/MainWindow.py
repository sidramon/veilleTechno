import tkinter as tk
from PIL import Image, ImageTk
import cv2
from ImageRecognition import ImageRecognition
import time


# MainWindow Class #
class MainWindow:
    def __init__(self):
        self.last_iteration_time = time.time()  # Timer
        self.window = tk.Tk()                   # Window
        self.ir = ImageRecognition()            # Image recognition AI

        # Set up the window
        self.window.title("Image recognition tool")
        self.window.geometry("1080x720")
        self.window.resizable(False, False)

        # Set up the video stream
        self.video_label = tk.Label(self.window)
        self.video_label.pack()

        # Set up the text area
        self.text_area = tk.Text(self.window, height=5)
        self.text_area.pack()
        self.update_text_area("I see a human.")

        self.start_camera()

    def open(self):
        # Open the window
        self.window.mainloop()

    def update_text_area(self, content):
        self.text_area.configure(state="normal")
        self.text_area.delete("1.0", tk.END)  # Clear the existing content
        self.text_area.insert(tk.END, content)
        self.text_area.configure(state="disabled")

    def start_camera(self):
        global cap
        cap = cv2.VideoCapture(0)
        self.update_frame()

    def update_frame(self):
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=image)
            self.video_label.configure(image=photo)
            self.video_label.image = photo
            self.video_label.after(10, self.update_frame)  # Update the frame every 10 milliseconds

            elapsed_time = time.time() - self.last_iteration_time
            if elapsed_time >= 1:  # Each second recognize the image
                newText = self.ir.recognize_image(photo)
                print(newText)
                self.update_text_area(newText)
                self.last_iteration_time = time.time()
