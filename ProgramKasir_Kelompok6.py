from tkinter import *
from tkinter import messagebox

login = Tk()
login.title('kasir')
login.geometry("500x310+500+200")
login.config(bg='#FF7F50')
label = Label(login, text='LOGIN KASIR', font="Normal 24 bold", bg='#FF7F50', foreground='#fef5ac')
username = Label(login, text='Username :', font="arial 15 bold ", bg='#FF7F50', foreground='#fef5ac')
password = Label(login, text='Password :', font="arial 15 bold ", bg='#FF7F50', foreground='#fef5ac')
entry1 = Entry(login, bd=5,relief=RIDGE, font="arial 15 bold ")
entry2 = Entry(login,bd=5, relief=RIDGE, font="arial 15 bold ", show="*")

label.place(x=150, y=20)
username.place(x=40, y=100)
password.place(x=40, y=160)
entry1.place(x=165, y=90, height=50)
entry2.place(x=165, y=150, height=50)

def show_password():
    if entry2.cget('show') == '*':
        entry2.config(show="")
    else:
        entry2.config(show="*")

def windowlogin():
    username = entry1.get()
    password = entry2.get()
    if username == 'KLMPOK 6' and password == 'Telkom12345':
        messagebox.showinfo('Sukses', 'Login Berhasil Mas')
        login.destroy()
    else :
        messagebox.showerror('Salah Woi', 'Salah satu dari user dan pass salah')


eye_pass = Checkbutton(login,command=show_password, text="show password", bg='#FF7F50', activeforeground="#FF7F50",activebackground="#FF7F50",font="10" )
eye_pass.place(x=165, y=200)

tombol_button = Button(login, text='LOGIN', command=windowlogin)
tombol_button.place(x=200, y=240, height=50, width=90)
login.mainloop()



app = Tk()
app.title('ZStore')
app.geometry("+410+90")
# variabe
Figur_Animejh = StringVar()
Rubik = StringVar()
Bola_PingPong = StringVar()
Sepatu_Super = StringVar()
Kipas_Cosmos = StringVar()
tekstotal = StringVar()
teksuang = StringVar()
total = 0
# buat function
def totalbeli():
    global Figur_Animejh, Rubik, Bola_PingPong, Sepatu_Super, Kipas_Cosmos, tekstotal, total
    hFigur_Animejh = int(Figur_Animejh.get()) * 50000
    hRubik = int(Rubik.get()) * 25000
    hBola_PingPong = int(Bola_PingPong.get()) * 5000
    hSepatu_Super = int(Sepatu_Super.get()) * 200000
    hKipas_Cosmos = int(Kipas_Cosmos.get()) * 80000
    total = hFigur_Animejh + hRubik + hBola_PingPong + hSepatu_Super + hKipas_Cosmos
    tekstotal.set(str(total))
def kembalian():
    global total
    uang = int(teksuang.get())
    if uang == total:
        messagebox.showinfo(message='Terima Kasih, Uang Kamu Pas')
    elif uang >= total:
        kembalian = uang - total
        messagebox.showinfo(message='Kembalian Kamu Sebesar {}'.format(str(kembalian)))
    else:
        messagebox.showerror(message='maaf uang kamu kurang')
def clear():
        Figur_Animejh.set('0')  
        Rubik.set('0')
        Bola_PingPong.set('0')
        Sepatu_Super.set('0')
        Kipas_Cosmos.set('0')
        tekstotal.set('0')
        teksuang.set('0')
app.geometry('650x600') # membuat ukuran
app.configure(bg='#FF7F50') # membuat backgroung warna
# membuat properti tulisan title
Label(app, text='Selamat Datang di ZStore', bg='#FF7F50', foreground='#fef5ac', font='arial 18 bold').place(x=200,y=30)
# membuat label nama menu
Label(app, text='1. Figur Animejh', bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=100)
Label(app, text='2. Rubik', bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=140)
Label(app, text='3. Bola Ping Pong', bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=180)
Label(app, text='4. Sepatu Super', bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=100,y=220)
Label(app, text='5. Kipas Cosmos', bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=100, y=260)
# membuat label harga
Label(app, text='Rp. 50000', bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=100)
Label(app, text='Rp. 25000', bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=140)
Label(app, text='Rp. 5000', bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=180)
Label(app, text='Rp. 200000', bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=220)
Label(app, text='Rp. 80000', bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=260)
# membuat spinbox
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Figur_Animejh, command=totalbeli).place(x=550,y=100)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Rubik, command=totalbeli).place(x=550,y=140)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Bola_PingPong, command=totalbeli).place(x=550,y=180)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Sepatu_Super, command=totalbeli).place(x=550,y=220)
Spinbox(app, from_=0, to=100, width=4, font='arial 10', textvariable=Kipas_Cosmos, command=totalbeli).place(x=550, y=260)
# membuat label pembayaran
Label(app, text='Masukan uang anda', bg='#FF7F50', foreground='#fef5ac', font='arial 12 ').place(x=97,y=320)
# membuat entry jumlah uang
Entry(app, textvariable=teksuang).place(x=100,y=345)
# membuat label total
Label(app, text='Rp. ', bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=350,y=340)
Label(app, textvariable=tekstotal, bg='#FF7F50', foreground='#fef5ac', font='arial 12 bold').place(x=380,y=340)
Label(app, text='Total', bg='#FF7F50', foreground='#fef5ac', font='arial 12').place(x=350,y=320)
# membuat tombol
Button(app, text='Bayar', foreground='white', bg='#006400', width=10, command=kembalian).place(x=100,y=400)
Button(app, text='Clear', foreground='white', bg='#ff1e1e', width=10, command=clear).place(x=250,y=400)

Label(app, text='Created By Zaid Alfian Haridtsah', foreground='White', bg='#FF7F50', font='Times 10').place(x=245,y=520)
app.mainloop() # menampilkan aplikasi