from tkinter import (Tk, Entry, Button, Label, messagebox, FALSE, DISABLED)

window = Tk()
window.title('Calculadora de PGA')
window.geometry('600x800')
window.resizable(FALSE, FALSE)

label_1 = Label(window, text='Creditos')
label_1.place(relx=0.25, rely=0, anchor='nw')
label_2 = Label(window, text='Nota')
label_2.place(relx=0.75, rely=0, anchor='ne')

posx_1 = 0.303
posx_2 = 0.715
posy = 0.1
n_labels = 0

entries_creditos = []
entries_notas = []

def new_course(x_1, x_2, y):
    global n_labels
    if(n_labels <= 22):
        creditos = Entry(window)
        creditos.place(relx=x_1, rely=y, anchor='center')
        entries_creditos.append(creditos)
        
        nota = Entry(window)
        nota.place(relx=x_2, rely=y, anchor='center')
        entries_notas.append(nota)
        
        global posy
        posy += 0.035
        
        n_labels += 1
    else:
        messagebox.showerror('Error', 'No se puede agregar más cursos')

def calculate_pga():
    total_creditos = 0
    total_numerador = 0
    
    try:
        for i in range(len(entries_creditos)):
            total_creditos += float(entries_creditos[i].get())
            total_numerador += float(entries_notas[i].get())*float(entries_creditos[i].get())
            
        pga = total_numerador/total_creditos
        
        label_2['text'] = '{}'.format(pga)
    except:
        messagebox.showerror('Error', 'Las notas y los créditos deben ser números')

button_1 = Button(window, text='Nuevo Curso', command = lambda: new_course(posx_1, posx_2, posy))
button_1.place(relx=0.99, rely=0.99, anchor='se')

button_2 = Button(window, text='Calcular Promedio', command = lambda: calculate_pga())
button_2.place(relx=0.5, rely=0.97, anchor='center')

label_1 = Label(window, text='Su PGA es:')
label_1.place(relx=0.4, rely=0.92, anchor='center')

label_2 = Label(window, state=DISABLED)
label_2.place(relx=0.6, rely=0.92, anchor='center')

window.mainloop()
