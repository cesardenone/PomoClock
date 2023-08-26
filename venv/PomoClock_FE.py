from tkinter import *
import time

global tempo
tempo = '00:00:00'

count = -5
run = True


# Funcao iniciar
def iniciar():
   def valor():
      if run:
         global count
         global tempo
         # antes de comecar
         if count <= -1:
            inicio = "começando em " + str(abs(count))
            label_tempo['text'] = inicio
            label_tempo['font'] =  'ivy 20 '
         else:
             label_tempo['font'] =  'Times 50 bold'
             d = str(tempo)
             h,m,s = map(int,d.split(":")) 
             h = int(h)
             m=int(m)
             s= int(count)

             if(s>=5):
                 count = 0
                 m+=1

             s=str(0)+str(s)
             m=str(0)+str(m)
             h=str(0)+str(h)

             d=str(h[-2:])+":"+str(m[-2:])+":"+str(s[-2:])
             label_tempo['text'] = d
             tempo = d

             s= int(count)
             m= int(m)
             h= int(h)             

         label_tempo.after(1000, valor)
         count += 1
   valor()


# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#3a323d"  # red / vermelha - fonte
cor5 = "#f4efeb"  # gray / Cizenta - bg
cor6 = "#3080f0"  # blue / azul

#janela principal
janela = Tk()
janela.title("PomoClock")
janela.geometry('400x300')
janela.configure(bg=cor5)
janela.resizable(width=FALSE, height=FALSE)
janela.iconbitmap('venv\icon.ico')



#criando labels
label_titulo = Label(janela, text='PomoClock', fon=('Arial 20 bold'), bg=cor5, fg=cor4)
label_titulo.place(x=120, y=5)

label_tempo = Label(janela, text=tempo, fon=('Consolas 60 bold'), bg=cor5, fg=cor4)
label_tempo.place(x=20, y=50)

#criando botões
botao_iniciar = Button(janela, text='Iniciar', width=10, height=2, bg=cor4, fg=cor2, font=('Arial 10 bold'), relief='raised', overrelief='ridg')
botao_iniciar.place(x=20, y=180)

botao_pausar = Button(janela, text='Pausar', width=10, height=2, bg=cor4, fg=cor2, font=('Arial 10 bold'), relief='raised', overrelief='ridg')
botao_pausar.place(x=155, y=180)

botao_reiniciar = Button(janela, text='Reiniciar', width=10, height=2, bg=cor4, fg=cor2, font=('Arial 10 bold'), relief='raised', overrelief='ridg')
botao_reiniciar.place(x=290, y=180)

janela.mainloop()

