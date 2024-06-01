import tkinter
from tkinter import *
from tkinter import messagebox
from english import ana_menu
import re

def baslayin_buton_tiklandi():
    ad1 = isiim.get()
    ad1 = ad1.strip()
    ad1 = ad1.upper()
    print(ad1)
    try:
        ad = str(ad1)
    except Exception as ad:
        print("Hatalı tuşlama yapıldı...")
        messagebox.showerror("hata","Hatalı tuşlama yapıldı...")
    if len(ad)<3:
        print("İsim eksik yazıldı.... :(")
        isiim.config(fg="red")
        messagebox.showerror("hata", "İsim eksik yazıldı.... :(")
    elif re.search("[.,£#${}|*+?<>!'^%&()=_/-]", ad):
        print("Saçma sapan isim yazıyosun doğru yaz şu adını.... :(")
        isiim.config(fg="red")
        messagebox.showerror("hata", "Saçma sapan isim yazıyosun doğru yaz adını soydını.... :(")
    elif re.search("[0-9]", ad):
        print("Saçma sapan sayı yazıyosun doğru yaz şu adını.... :(")
        isiim.config(fg="red")
        messagebox.showerror("hata","Saçma sapan sayı yazıyosun doğru yaz adını.... :(")
    else:
        son_sayi = son_sayii.get()
        print("değer=>", son_sayi)
        print("tipi=>", type(son_sayi))
        try:
            int(son_sayi)
        except Exception as ex:
            messagebox.showerror("hata", "Sayı girilmedi... :(")
            son_sayii.config(fg="red")
            son_sayi = float(-5)
        son_sayi = int(son_sayi)
        if son_sayi <= 0:
            messagebox.showerror("hata", "Yanlış bir sayı girildi... :(")
            son_sayii.config(fg="red")
        else:
            f = open("son.txt", "w")
            f.write(str(son_sayi))
            f.close()
            klavye_pencere.destroy()
            ana_menu(ad)

klavye_pencere = Tk()
klavye_pencere.title("English Vocabulary")
klavye_pencere.iconbitmap('icon.ico')
screen_width = klavye_pencere.winfo_screenwidth()  # Width of the screen
screen_height = klavye_pencere.winfo_screenheight()  # Height of the screen
w = 400
h = 400
x = (screen_width / 2) - (w / 2)
y = (screen_height / 2) - (h / 1.3)
klavye_pencere.geometry('%dx%d+%d+%d' % (w, h, x, y))
klavye_pencere.resizable(width=FALSE, height=FALSE)
Cklavye = Canvas(klavye_pencere, bd=3, height=400, width=400, bg="#514c6d")
Cklavye.place(width=400, height=400)
baslik = Label(klavye_pencere, text="English Vocabulary", bg="orange", fg="white",
               font="times 22 bold").place(x=10, y=10, height=35, width=380)
baslik1 = Label(klavye_pencere, text="İnglizce Kelime Tekrar Uygulaması", bg="orange", fg="white",
                font="times 14 bold").place(x=10, y=45, height=20, width=380)
bilgi2 = Label(klavye_pencere,
               text="Bu uygulama, önceden hazırladığınız .txt uzantılı\nbir dosyaya girdiğiniz inglizce ve türkçe kelime\nlistesinden rastgele kelimeleri karşınıza çıkararak\nsize kelime ezberi yapma konusunda yardımcı olur.\nİyi çalışmalar dileriz...",
               bg="#514c6d", fg="white",
               font="times 14 ").place(x=10, y=70, height=200, width=380)
by = Label(klavye_pencere, text="Onur ÇAĞLAR tarafından hazırlanmıştır.", bg="#514c6d", fg="black",
           font="times 8 bold").place(x=10, y=380, height=15, width=220)
kim_oynuyor = Label(klavye_pencere, text="Lütfen kullanıcı adı girin =>", anchor=tkinter.W,bg="#514c6d", fg="white",
                         font="times 14").place(x=10, y=250, height=30, width=310)
deger_iste_bilgi = Label(klavye_pencere, text="Dosyanızda kaç kelime olduğunu girin =>", anchor=tkinter.W,bg="#514c6d", fg="white",
                         font="times 14").place(x=10, y=290, height=30, width=310),
isiim = Entry(klavye_pencere, cursor="xterm", bg="green", bd=3, fg="white", font="times 14 ")
isiim.place(x=230, y=250, height=30, width=130)
son_sayii = Entry(klavye_pencere, cursor="xterm", bg="green", bd=3, fg="white", font="times 14 ")
son_sayii.place(x=320, y=290, height=30, width=40)
baslayin = Button(klavye_pencere, command=baslayin_buton_tiklandi, text="Başlayın", fg="white", cursor="hand2",
                  bg="green", font="times 18 bold")
baslayin.place(x=250, y=350, height=40, width=130)



klavye_pencere.mainloop()





