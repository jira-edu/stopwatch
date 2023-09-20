import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("โปรแกรมจับเวลา - © jiji 2023")  # Change the title bar
        self.root.geometry("800x400")  # Set the window size

        self.is_running = False
        self.start_time = 0
        self.timestamps = []

        # Create a frame to hold the clock label
        clock_frame = tk.Frame(root)
        clock_frame.pack(pady=20)

        self.label = tk.Label(clock_frame, text="0:00:00", font=("Arial", 200))
        self.label.pack()

        # Create a frame to hold the buttons
        button_frame = tk.Frame(root)
        button_frame.pack()

        # Use rounded buttons
        button_font = ("Arial", 14)  # Common font for buttons
        
        self.start_button = tk.Button(button_frame, text="เริ่ม / หยุด", width=15, font=button_font, command=self.start_stop, relief=tk.RAISED, borderwidth=4)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(button_frame, text="รีเซ็ต", width=15, font=button_font, command=self.reset_clock, relief=tk.RAISED, borderwidth=4)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.stamp_button = tk.Button(root, text="บันทึกเวลา", width=15, font=button_font, command=self.stamp_time)  # Use the same font as other buttons
        self.stamp_button.pack()

        self.clear_button = tk.Button(root, text="ล้างบันทึกเวลา", width=15, font=button_font, command=self.clear_timestamps)
        self.clear_button.pack()

        # Center-align the timestamp list
        timestamp_font = ("Arial", 22)  # Set the timestamp font size to 22
        self.timestamps_listbox = tk.Listbox(root, font=timestamp_font, justify="center")  # Center-align the text
        self.timestamps_listbox.pack(fill=tk.BOTH, expand=True)

        self.update_time()

    def start_stop(self):
        if self.is_running:
            self.stop()
        else:
            self.start()

    def start(self):
        self.is_running = True
        self.start_time = time.time() - self.start_time
        self.update()

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.start_time = time.time() - self.start_time
            self.update()

    def reset_clock(self):
        self.is_running = False
        self.start_time = 0
        self.update_time()

    def stamp_time(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
        else:
            elapsed_time = self.start_time

        self.timestamps.append(self.format_time(elapsed_time))
        # Center-align the text when inserting into the listbox
        self.timestamps_listbox.insert(tk.END, f"{len(self.timestamps)}: {self.format_time(elapsed_time)}")

    def clear_timestamps(self):
        self.timestamps = []
        self.timestamps_listbox.delete(0, tk.END)

    def update(self):
        if self.is_running:
            self.update_time()
            self.root.after(1000, self.update)

    def update_time(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
        else:
            elapsed_time = self.start_time

        self.label.config(text=self.format_time(elapsed_time))

    def format_time(self, elapsed_time):
        hours, remainder = divmod(int(elapsed_time), 3600)
        minutes, seconds = divmod(remainder, 60)

        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
