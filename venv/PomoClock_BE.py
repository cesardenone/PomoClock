import tkinter as tk
from datetime import datetime, timedelta

class CountdownApp:
    
    def __init__(self, root):

        self.start = False
        
        def start_clock():
            self.start = True
            self.update_clock()

        self.root = root
        self.root.title("PomoClock")
        self.root.geometry('400x280')
        self.root.resizable(width=False, height=False)
        self.root.configure(background="#fafcff")
        
        self.time_left = timedelta(minutes=25)  # Defina o tempo desejado
        self.end_time = datetime.now() + self.time_left
        
        self.label = tk.Label(root, text="", font=("Helvetica", 48))
        self.label.pack(padx=100, pady=80)

        self.button_start = tk.Button(root, command=start_clock, text="Iniciar", width=10, height=2, bg='#0a0a0a', fg="#fafcff", font=('Ivy 8 bold'))
        self.button_start.pack(padx=2, pady=10)
        
        

        self.update_clock()
        
    def update_clock(self):
        if self.start:
            current_time = datetime.now()
            time_difference = self.end_time - current_time
            
            if time_difference.total_seconds() <= 0:
                self.label.config(text="Tempo esgotado!")
            else:
                minutes = int(time_difference.total_seconds() // 60)
                seconds = int(time_difference.total_seconds() % 60)
                self.label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.after(1000, self.update_clock)

        
root = tk.Tk()
app = CountdownApp(root)
root.mainloop()