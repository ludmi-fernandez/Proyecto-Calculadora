from re import I
from sqlite3 import Row
from tkinter import*

ventana= Tk()
ventana. title("CALCULADORA")

i=0

#Entrada
e_texto=Entry(ventana, font=("Arial",20,"bold"))
e_texto.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

#Funciones
def click_boton(valor):
    global i
    e_texto.insert(i,valor)
    i+=1
def borrar():
    e_texto.delete(0, END)
    i=0
def realizar_operacion():
    ecuacion=e_texto.get()
    resultado=eval(ecuacion)
    e_texto.delete(0,END)
    e_texto.insert(0,resultado)
    i=0


#Botones
boton1= Button(ventana,text="1",width=5,height=2, command=lambda:click_boton(1),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))
boton2= Button(ventana,text="2",width=5,height=2,command=lambda:click_boton(2),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))
boton3= Button(ventana,text="3",width=5,height=2, command=lambda:click_boton(3),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))
boton4= Button(ventana,text="4",width=5,height=2, command=lambda:click_boton(4),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))
boton5= Button(ventana,text="5",width=5,height=2, command=lambda:click_boton(5),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))
boton6= Button(ventana,text="6",width=5,height=2, command=lambda:click_boton(6),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))
boton7= Button(ventana,text="7",width=5,height=2, command=lambda:click_boton(7),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))
boton8= Button(ventana,text="8",width=5,height=2, command=lambda:click_boton(8),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))
boton9= Button(ventana,text="9",width=5,height=2, command=lambda:click_boton(9),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))
boton0= Button(ventana,text="0",width=15,height=2, command=lambda:click_boton(0),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))


boton_borrar= Button(ventana,text="AC",width=5,height=2, command=lambda:borrar(),foreground="purple2",background="DarkOrange1",font=("Arial",14,"bold"))
boton_parentesis1= Button(ventana,text="(",width=5,height=2, command=lambda:click_boton("("),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))
boton_parentesis2= Button(ventana,text=")",width=5,height=2, command=lambda:click_boton(")"),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))
boton_punto= Button(ventana,text=".",width=5,height=2, command=lambda:click_boton("."),foreground="ghost white",background="purple2",font=("Arial",14,"bold"))

boton_div= Button(ventana,text="÷",width=5,height=2, command=lambda:click_boton("/"),foreground="purple2",background="ghost white",font=("Arial",14,"bold"))
boton_mult= Button(ventana,text="x",width=5,height=2, command=lambda:click_boton("*"),foreground="purple2",background="ghost white",font=("Arial",14,"bold"))
boton_sum= Button(ventana,text="+",width=5,height=2, command=lambda:click_boton("+"),foreground="purple2",background="ghost white",font=("Arial",14,"bold"))
boton_rest= Button(ventana,text="-",width=5,height=2, command=lambda:click_boton("-"),foreground="purple2",background="ghost white",font=("Arial",14,"bold"))
boton_igual= Button(ventana,text="=",width=5,height=2, command=lambda:realizar_operacion(),foreground="purple2",background="ghost white",font=("Arial",14,"bold"))

#Agregar botones a la pantalla
boton_borrar.grid(row=1,column=0,padx=5,pady=5)
boton_parentesis1.grid(row=1,column=1,padx=5,pady=5)
boton_parentesis2.grid(row=1,column=2,padx=5,pady=5)
boton_div.grid(row=1,column=3,padx=5,pady=5)

boton7.grid(row=2,column=0,padx=5,pady=5)
boton8.grid(row=2,column=1,padx=5,pady=5)
boton9.grid(row=2,column=2,padx=5,pady=5)
boton_mult.grid(row=2,column=3,padx=5,pady=5)

boton4.grid(row=3,column=0,padx=5,pady=5)
boton5.grid(row=3,column=1,padx=5,pady=5)
boton6.grid(row=3,column=2,padx=5,pady=5)
boton_sum.grid(row=3,column=3,padx=5,pady=5)

boton1.grid(row=4,column=0,padx=5,pady=5)
boton2.grid(row=4,column=1,padx=5,pady=5)
boton3.grid(row=4,column=2,padx=5,pady=5)
boton_rest.grid(row=4,column=3,padx=5,pady=5)

boton0.grid(row=5,column=0,columnspan=2,padx=5,pady=5)
boton_punto.grid(row=5,column=2,padx=5,pady=5)
boton_igual.grid(row=5,column=3,padx=5,pady=5)


ventana.mainloop()