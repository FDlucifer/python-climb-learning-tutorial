# pip install opencv-python pillow

import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import cv2
from PIL import Image, ImageTk


class GIFMaker(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("GIF Maker")
        self.geometry("800x850")

        self.video_path = ""
        self.output_path = ""
        self.frames = []
        self.preview_frame_index = 0

        self.select_video_button = tk.Button(
            self, text="Select Video", command=self.select_video
        )
        self.select_video_button.pack(pady=10)

        self.preview_label = tk.Label(self, text="Video Preview")
        self.preview_label.pack(pady=10)

        self.canvas = tk.Canvas(self, width=640, height=480, background="#eeeeee")
        self.canvas.pack(pady=10)

        self.speed_label = tk.Label(self, text="Speed (fps):")
        self.speed_label.pack(pady=10)

        self.speed_entry = tk.Entry(self)
        self.speed_entry.pack()
        self.speed_entry.insert(0, "10")

        self.scale_label = tk.Label(self, text="Scale (1.0 = 100%):")
        self.scale_label.pack(pady=10)

        self.scale_entry = tk.Entry(self)
        self.scale_entry.pack()
        self.scale_entry.insert(0, "0.5")

        self.export_button = tk.Button(self, text="Export GIF", command=self.export_gif)
        self.export_button.pack(pady=20)

        self.progress = ttk.Progressbar(
            self, orient=tk.HORIZONTAL, length=100, mode="indeterminate"
        )
        self.progress.pack(pady=20)

    def select_video(self):
        self.video_path = filedialog.askopenfilename(
            title="Select Video",
            filetypes=(("MP4 Files", "*.mp4"), ("ALL Files", "*.*")),
        )
        if self.video_path:
            self.process_video()

    def process_video(self):
        if not self.video_path:
            return

        cap = cv2.VideoCapture(self.video_path)
        self.frames = []

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.frames.append(frame)

        cap.release()

        self.preview_frame_index = 0
        self.animate_preview()

    def animate_preview(self):
        if not self.frames:
            return

        frame = self.frames[self.preview_frame_index]
        frame_image = Image.fromarray(frame)
        frame_image = frame_image.resize((640, 480), Image.ANTIALIAS)
        frame_photo = ImageTk.PhotoImage(frame_image)

        self.canvas.create_image(0, 0, anchor=tk.NW, image=frame_photo)
        self.canvas.image = frame_photo

        self.preview_frame_index = (self.preview_frame_index + 1) % len(self.frames)
        self.after(100, self.animate_preview)

    def export_gif(self):
        fps = int(self.speed_entry.get())
        scale = float(self.scale_entry.get())

        if not self.frames or fps <= 0 or scale <= 0:
            messagebox.showerror("Error", "Invalid options")

        self.output_path = filedialog.asksaveasfilename(
            defaultextension=".git",
            filetypes=(("GIF Files", "*.gif"), ("All Files", "*.*")),
        )

        if not self.output_path:
            return

        self.progress.start(10)
        threading.Thread(target=self.create_gif, args=(fps, scale), daemon=True).start()

    def create_gif(self, fps, scale):
        output_frames = []

        for frame in self.frames:
            img = Image.fromarray(frame)
            img = img.resize(
                (int(img.width * scale), int(img.height * scale)), Image.ANTIALIAS
            )
            output_frames.append(img)

        output_frames[0].save(
            self.output_path,
            save_all=True,
            append_images=output_frames[1:],
            optimize=False,
            duration=1000 // fps,
            loop=0,
        )

        self.after(0, self.progress.stop)
        messagebox.showinfo("Success", "GIF Successfully Exported!")


if __name__ == "__main__":
    app = GIFMaker()
    app.mainloop()
