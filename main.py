import tkinter as tk
import time

class Saat:
    def __init__(self):
        self.root = tk.Tk()
        
        self.root.overrideredirect(True)
        
        self.root.wm_attributes("-topmost", True)
        
        bg_color = "black"  
        self.root.config(bg=bg_color)
        self.root.wm_attributes("-transparentcolor", bg_color)

        self.label = tk.Label(self.root, font=('Consolas', 40, 'bold'), 
                              bg=bg_color, fg='#00ff41')
        self.label.pack()

        self.update_clock()

        self.root.bind('<Button-1>', self.start_move)
        self.root.bind('<B1-Motion>', self.do_move)
        
        self.root.bind('<Button-3>', lambda e: self.root.destroy())

        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.config(text=now)
        self.label.after(1000, self.update_clock)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = self.root.winfo_x() - self.x + event.x
        y = self.root.winfo_y() - self.y + event.y
        self.root.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    app = Saat()
