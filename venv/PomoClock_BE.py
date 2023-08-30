from tkinter import *
import tkinter
import time

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

janela = Tk()
janela.title("")
janela.geometry('310x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=cor1)

global timer
timer = '25:00'
global run
run = False

def contador(): 
   global timer
   global run
   tempo = 25 * 60
   if timer != '00:00':
      m, s = divmod(tempo, 60) 
      timer = '{:02d}:{:02d}'.format(m, s)
      label_time['font'] = 'Times 20 bold '
      label_time['text'] = timer

      m=int(m)
      s=int(s)

      if s>=59:
         m -=1

      time.sleep (1)
      s -= 1

      s=str(0)+str(s)
      m=str(0)+str(m)

# Funcao para iniciar
def start():
   global run
   run = True
   contador()

# Funacao para pausar
def stop():
   global run
   run = False

# funcao para reiniciar
def reset():
   global count
   count = -5

   # Se estiver pausado ira reiniciar do zero
   if run == False:
       global timer
       tempo = '00:00:00'
       label_time['text'] = timer

   # Se nao estiver pausado ira continuar onde parou antes 
   else:
      label_time['font'] =  'ivy 20 '
      label_time['text'] = 'Iniciando...'


label_app = Label(janela, text='cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20,y=5)

label_time = Label(janela, text=timer, font=('Times 50 bold'), bg=cor1, fg=cor6)
label_time.grid(row=0, column=0, sticky=NSEW, padx=15, pady=20)

label_app.lift()

frameBaixo = Frame(janela,width=310, height=350,bg=cor1, relief="flat")
frameBaixo.grid(row=1, column=0,pady=0, padx=30, sticky=NSEW)

botao_start = Button(frameBaixo,command=start, text="Iniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_start.grid(row=0, column=0, sticky=NSEW, padx=2, pady=10)

botao_stop = Button(frameBaixo,command=stop, text="Pausar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_stop.grid(row=0, column=1, sticky=NSEW, padx=2, pady=10)

botao_reset = Button(frameBaixo, command=reset, text="Reiniciar", width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_reset.grid(row=0, column=2, sticky=NSEW, padx=2, pady=10)


janela.mainloop()