# This is a sample Python script.
import tkinter.filedialog
from tkinter import *
from tkinter import messagebox
import sys
from time import sleep
import random
import pyautogui
import re


def ana_menu(ad):
    def basla_buton_tiklandi():
        metin_kutusu.config(text=str(ing_kelime1), bg="#514c6d")
        bitir.config( command=bitir_buton_tiklandi,cursor="hand2", bg="green", state="normal")
        basla.destroy()
    def bitir_buton_tiklandi():
        def inglizce_page_change_orta21_func():
            metin_kutusu.configure(text=str(ing_kelime_orta))
            btn_box_change_orta22.config(state="normal", cursor="hand2")
            btn_box_change_orta21.config(state=DISABLED, cursor="x_cursor")
            metin_kutusu.config(state="normal", cursor="hand2")
            metin_kutusu_pre.configure(text=f"{adim}) İngilizce Kelimeniz:")
        def turkce_page_change_orta22_func():
            metin_kutusu.configure(text=str(tr_kelime_orta))
            btn_box_change_orta21.config(state="normal", cursor="hand2")
            btn_box_change_orta22.config(state=DISABLED, cursor="x_cursor")
            metin_kutusu_pre.configure(text="Kelimenin Türkçe Anlamı:")

        global tr_kelime, adim, btn_box_change_orta21, btn_box_change_orta22, ing_kelime_orta, dogruluk_durumu
        btn_box_change1.destroy()
        btn_box_change2.destroy()
        btn_box_change_orta21 = Button(english_pencere, text="<", state=DISABLED, command=inglizce_page_change_orta21_func, bd=5,
                                bg="#27234c",
                                cursor="x_cursor", fg="turquoise", font="times 18 bold")
        btn_box_change_orta21.place(x=15, y=125, height=25, width=25)
        btn_box_change_orta22 = Button(english_pencere, text=">", command=turkce_page_change_orta22_func, bd=5, bg="#27234c",
                                 cursor="hand2", fg="turquoise", font="times 18 bold")
        btn_box_change_orta22.place(x=365, y=125, height=25, width=25)

        adim=2
        k_text = cevap_kutusu.get()
        k_text = k_text.lower()
        tr_kelimee = tr_kelime1.split("\n")
        cevap = k_text.split(" ")
        print(cevap)
        print(tr_kelimee)
        try:
            cevapp = cevap_kutusu.get()
        except Exception as cevapp:
            print("Hatalı tuşlama yapıldı...")
            messagebox.showerror("hata", "Hatalı tuşlama yapıldı...")
        if re.search("[ ]", cevapp):
            print("Cevap metinde boşluk var.... :(")
            messagebox.showerror("hata", "Lütfen cevabınızı boşluk kullanmadan, bitişik şekilde girin.... :(")
            return
        elif re.search("[.,£#${}|*+?<>!'^%&()=_/-]", cevapp):
            print("Saçma sapan isim yazıyosun doğru yaz şu adını.... :(")
            messagebox.showerror("hata", "Saçma sapan cevap yazıyosun! Lütfen doğru şekilde cevabını gir.... :(")
            return
        elif re.search("[0-9]", cevapp):
            print("Saçma sapan sayı yazıyosun doğru yaz şu adını.... :(")
            messagebox.showerror("hata", "Saçma sapan sayı yazıyosun! Lütfen doğru bir cevap metni gir.... :(")
            return
        elif tr_kelimee == cevap:
            dogruluk_durumu =1
            durum_kutusu.configure(text="Doğru Cevap Verdiniz...  (+1 Puan)", bg="#514c6d")
            puanim.config(text=f"Puanım: 1")
            bitir.destroy()
            devam_kontrol=1
        elif cevap == ['']:
            messagebox.showinfo('Bilgi','Cevap verilmedi!')
            return
        else :
            dogruluk_durumu = 0
            durum_kutusu.configure(text=f"Yanlış Cevap Verdiniz...  (-1 Puan)\n{tr_kelimee}", bg="#514c6d")
            with open("C:\\Users\\asus\\Desktop\\degerlendirme.txt", "a", encoding="utf-8") as yazma:
                yazma.write(str(ing_kelime1)+"\t\t"+str(tr_kelimee)+"\t\t"+str(cevap) + "\n")
            puanim.config(text=f"Puanım: -1")
            bitir.destroy()
            devam_kontrol = 1
        if devam_kontrol == 1:
            with open(dosyayolu, "r+", encoding="utf-8") as file:
                okuma = file.readlines()
            #rastgele = random.randint(0, (son_sayii - 1))
            print("rastgele=>", rastgele[1])
            for i in range(0, int(len(okuma))):

                if rastgele[1] == i:
                    kelimeler = okuma[i]
                    kelimeler = kelimeler.split(" ")
                    ing_kelime_ham = str(kelimeler[0])
                    tr_kelime_ham = str(kelimeler[1])
                    ing_kelime = ing_kelime_ham.strip()
                    tr_kelime = tr_kelime_ham.strip()
                    ing_kelime_orta = ing_kelime
                    tr_kelime_orta = tr_kelime
                    metin_kutusu.config(text=str(ing_kelime), bg="#514c6a")
                    metin_kutusu_pre.config(text="2) İnglizce Kelimeniz:")
    def cikis_buton_tiklandi():
        try:
            messagebox.showinfo("Uyarı",f"Toplam -{adim-1}- kelime cevapladınız. Puanınız: {sayac}'dır.\nYanlış cevap verdiğiniz kelimeler masaüstüne eklenmiştir.\nUygulamadan çıkış yapılıyor...")
            with open("C:\\Users\\asus\\Desktop\\degerlendirme.txt", "a", encoding="utf-8") as yazma:
                yazma.write("\nToplam " + str(adim-1) + "kelime cevapladınız...\n Doğru sayınız:"+ str(dogru) + "'dır."+ "\n Yanlış sayınız:"+ str(((adim-1)-dogru)) + "'dır."+ "\n\nLütfen yeni bir kelime çalışması yapmadan önce bu dosyayı temizleyin...\nBu uygulama Onur ÇAĞLAR tarafından hazırlanmıştır.")
        except NameError:
            messagebox.showinfo("Uyarı",f"Toplam '0' kelime cevapladınız. Doğru sayınız: '0'dır.\nUygulamadan çıkış yapılıyor...")
        sleep(0.5)
        sys.exit()
    def devam_buton_tiklandi():
        btn_box_change_orta21.destroy()
        btn_box_change_orta22.destroy()

        #ekranda konuma gidip otomatik tıklıyor...
        yatay_konum = (screen_width / 2) + 125
        dikey_konum = (screen_height / 2) -30
        pyautogui.click(x=yatay_konum, y=dikey_konum)
        pyautogui.click(x=yatay_konum, y=dikey_konum)
        pyautogui.click(x=yatay_konum, y=dikey_konum)
        if ilk==0:
            btn_box_change21.destroy()
            btn_box_change22.destroy()
        devam2_buton_tiklandi(tr_kelime)
    def devam2_buton_tiklandi(tr_kelime):
        def inglizce_page_change21_func():
            metin_kutusu.configure(text=str(ing_kelime_text))
            btn_box_change22.config(state="normal", cursor="hand2")
            btn_box_change21.config(state=DISABLED, cursor="x_cursor")
            metin_kutusu.config(state="normal", cursor="hand2")
            metin_kutusu_pre.configure(text=f"{adim}) İngilizce Kelimeniz:")
        def turkce_page_change22_func():
                metin_kutusu.configure(text=str(tr_kelime_text))
                btn_box_change21.config(state="normal", cursor="hand2")
                btn_box_change22.config(state=DISABLED, cursor="x_cursor")
                metin_kutusu_pre.configure(text="Kelimenin Türkçe Anlamı:")

        global adim, sayac, dogru, btn_box_change21, btn_box_change22
        btn_box_change21 = Button(english_pencere, text="<", state=DISABLED, command=inglizce_page_change21_func, bd=5,
                                bg="#27234c",
                                cursor="x_cursor", fg="turquoise", font="times 18 bold")
        btn_box_change21.place(x=15, y=125, height=25, width=25)
        btn_box_change22 = Button(english_pencere, text=">", command=turkce_page_change22_func, bd=5, bg="#27234c",
                                 cursor="hand2", fg="turquoise", font="times 18 bold")
        btn_box_change22.place(x=365, y=125, height=25, width=25)
        k_text = cevap_kutusu.get()
        k_text = k_text.lower()
        tr_kelimee = tr_kelime.split("\n")
        cevap = k_text.split(" ")
        print(cevap)
        print(tr_kelimee)
        try:
            cevapp = cevap_kutusu.get()
        except Exception as cevapp:
            print("Hatalı tuşlama yapıldı...")
            messagebox.showerror("hata", "Hatalı tuşlama yapıldı...")
        if re.search("[ ]", cevapp):
            print("Cevap metinde boşluk var.... :(")
            messagebox.showerror("hata", "Lütfen cevabınızı boşluk kullanmadan, bitişik şekilde girin.... :(")
        elif re.search("[.,£#${}|*+?<>!'^%&()=_/-]", cevapp):
            print("Saçma sapan isim yazıyosun doğru yaz şu adını.... :(")
            messagebox.showerror("hata", "Saçma sapan cevap yazıyosun! Lütfen doğru şekilde cevabını gir.... :(")
        elif re.search("[0-9]", cevapp):
            print("Saçma sapan sayı yazıyosun doğru yaz şu adını.... :(")
            messagebox.showerror("hata", "Saçma sapan sayı yazıyosun! Lütfen doğru bir cevap metni gir.... :(")
        elif tr_kelimee == cevap:
            if ilk == 1:
                if dogruluk_durumu==1:
                    sayac = 1
                    dogru = 1
                else:
                    sayac = -1
                    dogru = 0

                print("döngü kontrol")
            durum_kutusu.config(text="Doğru Cevap Verdiniz...  (+1 Puan)", bg="#514c6d")
            adim += 1
            dogru += 1
            sayac += 1
            print(sayac, "   " , adim)
            puanim.config(text=f"Puanım:{sayac}")
            tekrarla(adim)
        elif cevap==['']:
            messagebox.showinfo('Bilgi','Cevap Verilmedi...')
        else:
            if ilk == 1:
                if dogruluk_durumu==1:
                    sayac = 0
                    dogru = 1
                else:
                    sayac = -2
                    dogru = 0
                adim +=1

                with open("C:\\Users\\asus\\Desktop\\degerlendirme.txt", "a", encoding="utf-8") as yazma:
                    yazma.write(str(ing_kelime_orta) + "\t\t" + str(tr_kelimee) + "\t\t" + str(cevap) + "\n")
            durum_kutusu.config(text=f"Yanlış Cevap Verdiniz...  (-1 Puan)\n{tr_kelimee}",bg="#514c6d")
            if ilk==0:
                adim += 1
                sayac -= 1
                with open("C:\\Users\\asus\\Desktop\\degerlendirme.txt", "a", encoding="utf-8") as yazma:
                    yazma.write(str(ing_kelime_text)+"\t\t"+str(tr_kelimee)+"\t\t"+str(cevap) + "\n")
            print(sayac, "   ", adim)
            puanim.config(text=f"Puanım:{sayac}")
            tekrarla(adim)
    def inglizce_page_change1_func():
        metin_kutusu.configure(text=str(ing_kelime1))
        btn_box_change1.config(state="normal", cursor="hand2")
        btn_box_change2.config(state=DISABLED, cursor="x_cursor")
        metin_kutusu.config(state="normal", cursor="hand2")
        metin_kutusu_pre.configure(text=f"{adim}) İngilizce Kelimeniz:")
    def turkce_page_change1_func():
        try:
            metin_kutusu.configure(text=str(tr_kelime))
            btn_box_change1.config( state="normal",cursor="hand2")
            btn_box_change2.config(state=DISABLED, cursor="x_cursor")
            metin_kutusu_pre.configure(text="Kelimenin Türkçe Anlamı:")
        except NameError:
            isim_hatasi_verildi()
    def tekrarla (adim):
        global tr_kelime, ing_kelime, ilk, ing_kelime_text, tr_kelime_text
        ilk=0
        with open(dosyayolu, "r+", encoding="utf-8") as file:
            okuma = file.readlines()
        for i in range(0, int(len(okuma))):

            if adim== son_sayii+1:
                messagebox.showinfo('Bilgi','Listenizdeki tüm kelimeleri cevapladınız...')
                cikis_buton_tiklandi()

            if i == rastgele[adim-1]:
                kelimeler = okuma[i]
                kelimeler = kelimeler.split(" ")
                ing_kelime_ham = str(kelimeler[0])
                tr_kelime_ham = str(kelimeler[1])
                ing_kelime = ing_kelime_ham.strip()
                tr_kelime = tr_kelime_ham.strip()
                ing_kelime_text= ing_kelime
                tr_kelime_text = tr_kelime
                metin_kutusu.config(text=str(ing_kelime), bg="#514c6a")
                metin_kutusu_pre.config(text=str(adim)+") İnglizce Kelimeniz:")

                print("rastgele döngü içi tekrar=>", adim, i)
                break
    def isim_hatasi_verildi():
        messagebox.showinfo("Uyarı","İlk kelimede kullanıcının yardım almadan kendi cevaplaması beklenir...")




    global ilk
    with open("son.txt", "r+", encoding="utf-8") as file:
        son_sayi1 = file.readlines()
    print("son sayı değeri=>", son_sayi1[0])
    name= ad
    ilk = 1
    english_pencere = Tk()
    english_pencere.title("English Vocabulary")
    english_pencere.iconbitmap('icon.ico')
    screen_width = english_pencere.winfo_screenwidth()  # Width of the screen
    screen_height = english_pencere.winfo_screenheight()  # Height of the screen
    w = 400
    h = 400
    x = (screen_width / 2) - (w / 2)
    y = (screen_height / 2) - (h / 1.3)
    english_pencere.geometry('%dx%d+%d+%d' % (w, h, x, y))
    english_pencere.resizable(width=FALSE, height=FALSE)
    Canvas(english_pencere, bd=3, bg="#514c6d", height=400, width=400).place(width=400, height=400)
    baslik = Label(english_pencere, text="English Vocabulary", bg="orange", fg="white",
                   font="times 22 bold").place(x=10, y=10, height=35, width=380)
    baslik1 = Label(english_pencere, text="İnglizce Kelime Tekrar Uygulaması", bg="orange", fg="white",
                    font="times 14 bold").place(x=10, y=45, height=20, width=380)
    kullanici= Label(english_pencere, anchor=tkinter.W,text=f"Kullanıcı:{name}", bg="#514c6d", fg="black",
                    font="times 12 bold").place(x=10, y=70, height=20, width=280)
    puanim = Label(english_pencere, text="Puanım: 0",anchor=tkinter.E, bg="#514c6d", fg="black",
                      font="times 12 bold")
    puanim.place(x=300, y=70, height=20, width=90)
    devam = Button(english_pencere, command=devam_buton_tiklandi, text="Devam Et", fg="white", cursor="hand2",
                   bg="green", font="times 20 bold")
    devam.place(x=220, y=340, height=50, width=170)
    cikis= Button(english_pencere, command=cikis_buton_tiklandi, text="Çıkış Yap", fg="white", cursor="hand2",
                   bg="red", font="times 20 bold")
    cikis.place(x=10, y=340, height=50, width=170)
    Canvas(english_pencere, bd=3, bg="#514c6d", height=54, width=376).place(x=8, y=105)
    Canvas(english_pencere, bd=3, bg="#514c6d", height=86, width=376).place(x=8, y=178)
    metin_kutusu_pre = Label(english_pencere, text="1) İngilizce Kelimeniz:", bg="#514c6d", fg="black",
                         font="times 12 bold")
    metin_kutusu_pre.place(x=75, y=107, height=20, width=250)
    metin_kutusu = Label(english_pencere, bg="#514c6d", fg="white", font="times 15 bold")
    metin_kutusu.place(x=75, y=137, height=30, width=250)

    btn_box_change1 = Button(english_pencere, text="<",state=DISABLED, command=inglizce_page_change1_func, bd=5, bg="#27234c",
                           cursor="x_cursor", fg="turquoise", font="times 18 bold")
    btn_box_change1.place(x=15, y=125, height=25, width=25)
    btn_box_change2 = Button(english_pencere, text=">", command=turkce_page_change1_func, bd=5, bg="#27234c",
                           cursor="hand2", fg="turquoise", font="times 18 bold")
    btn_box_change2.place(x=365, y=125, height=25, width=25)
    durum_kutusu = Label(english_pencere, bg="#514c6d", fg="black",
                             font="times 12 bold")
    durum_kutusu.place(x=50, y=280, height=40, width=300)
    cevap_kutusu_pre = Label(english_pencere, text="Türkçe Cevabınız:", bd=5, bg="#514c6d", fg="black",
                             font="times 12 bold")
    cevap_kutusu_pre.place(x=10, y=180, height=20, width=380)
    cevap_kutusu = Entry(english_pencere, bg="white", bd=3, fg="black",
                         font="times 17 bold")
    cevap_kutusu.place(x=10, y=220, height=50, width=380)
    bitir= Button(english_pencere, text="Tamamla", bg="purple",state= DISABLED,fg="white",cursor="x_cursor", font="times 20 bold")
    bitir.place(x=220, y=340, height=50, width=170)

    basla = Button(english_pencere, command=basla_buton_tiklandi, text="Başla", fg="white", cursor="hand2",
                   bg="purple", font="times 20 bold")
    basla.place(x=10, y=340, height=50, width=170)




    son_sayii = int(son_sayi1[0])
    rastgele = random.sample(range(0, son_sayii),son_sayii)
    dosyayolu = tkinter.filedialog.askopenfilename(filetypes = (('Text files','*.txt'),))
    with open(dosyayolu, "r+", encoding="utf-8") as file:
        okuma = file.readlines()

    with open("C:\\Users\\asus\\Desktop\\degerlendirme.txt", "a", encoding="utf-8") as yazma:
        yazma.write("\nİnglizce\t\tTürkçe\t\tCevabınız\n\n")
    print("rastgele tüm sıra=>", rastgele)
    print("rastgele=>", rastgele[0])
    for i in range(0, int(len(okuma))):

        if rastgele[0] == i:
            kelimeler = okuma[i]
            kelimeler = kelimeler.split(" ")
            ing_kelime_ham = str(kelimeler[0])
            tr_kelime_ham = str(kelimeler[1])
            ing_kelime1 = ing_kelime_ham.strip()
            tr_kelime1 = tr_kelime_ham.strip()
            break
    english_pencere.mainloop()
