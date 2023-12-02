import tkinter as tk
import datetime as dt
import pyodbc
from winotify import Notification

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("PomoClock")
        self.root.geometry('400x280')
        self.root.resizable(width=False, height=False)
        self.root.configure(background="#fafcff")
        self.root.iconbitmap("icon.ico")
        
        self.work_time = dt.timedelta(minutes=1)
        self.break_time = dt.timedelta(minutes=5)
        self.is_working = True
        self.is_running = False
        
        self.label = tk.Label(root, text="", font=("Helvetica", 48), bg="#fafcff")
        self.label.pack(padx=20, pady=30)

        self.label_task = tk.Label(root, text="Digite a atividade:", font=("Helvetica", 10), bg="#fafcff")
        self.label_task.place(x=88, y=110)
        
        self.entry_task = tk.Entry(root, font=("Helvetica", 10), bd=2, width=30, justify="left")
        self.entry_task.place(x=88, y=140)

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_timer, width=10, height=2, bg='#0a0a0a', fg="#fafcff", font=('Ivy 8 bold'))
        self.pause_button = tk.Button(root, text="Reiniciar", command=self.pause_timer, width=10, height=2, bg='#0a0a0a', fg="#fafcff", font=('Ivy 8 bold'))
        
        self.start_button.pack(side=tk.LEFT, padx=80)
        self.pause_button.pack(side=tk.LEFT, padx=0)
        
        self.update_clock()

        self.notification1 = Notification(app_id="Pomoclock", title="Vamos lá!", msg="Relógio iniciado!", duration="short", icon=r"C:\Users\cesar\Documents\GitHub\PomoClock\venv\icon.ico")
        self.notification2 = Notification(app_id="Pomoclock", title="Atenção!", msg="Verifique seu Pomoclock!", duration="short", icon=r"C:\Users\cesar\Documents\GitHub\PomoClock\venv\icon.ico")

    def db_connect(self):
        self.SERVER = 'DESKTOP-3R9MF7L'
        self.DATABASE = 'POMOCLOCK'
        self.USERNAME = 'SA'
        self.PASSWORD = 'SuperPassword@182'

        self.connectionString = f'DRIVER={{SQL Server}};SERVER={self.SERVER};DATABASE={self.DATABASE};UID={self.USERNAME};PWD={self.PASSWORD}'
        self.conn = pyodbc.connect(self.connectionString)


    def update_clock(self):
        if not self.is_running:
            self.label.config(text=self.get_time_text(self.work_time if self.is_working else self.break_time))

        elif self.is_running:
            current_time = dt.datetime.now()
            time_difference = self.end_time - current_time

            if time_difference.total_seconds() <= 0:
                self.is_running = False
                self.toggle_timer()
            else:
                minutes = int(time_difference.total_seconds() // 60)
                seconds = int(time_difference.total_seconds() % 60)
                self.label.config(text=f"{minutes:02d}:{seconds:02d}")
        
        self.root.after(1000, self.update_clock)
        
    def start_timer(self):
        self.is_running = True
        self.end_time = dt.datetime.now() + (self.work_time if self.is_working else self.break_time)
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.task = self.entry_task.get()

        self.db_connect(    )
        self.hora_atual = dt.datetime.now()
        self.sql_query = f"""INSERT INTO ATIVIDADES(HORA_INICIO, FOCO_REINICIO, ATIVIDADE) VALUES ('{self.hora_atual}', 'FOCO', '{self.task}')"""
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.sql_query)
        self.cursor.commit()
        self.notification1.show()

        
    def pause_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.sql_query = f"""INSERT INTO ATIVIDADES(HORA_REINICIO, FOCO_REINICIO) VALUES ('{self.hora_atual}', 'REINICIO')"""
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.sql_query)
        self.cursor.commit()
        self.notification2.show()
        
    def toggle_timer(self):
        if self.is_working:
            self.is_working = False
        else:
            self.is_working = True
        
        self.start_timer()
        
    def get_time_text(self, time_delta):
        minutes = int(time_delta.total_seconds() // 60)
        seconds = int(time_delta.total_seconds() % 60)
        return f"{minutes:02d}:{seconds:02d}"

root = tk.Tk()
timer = PomodoroTimer(root)
root.mainloop()
