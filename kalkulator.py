import tkinter as tk

aktualne_rownanie = ""

def dodaj_znak(znak):
    global aktualne_rownanie
    aktualne_rownanie = aktualne_rownanie + znak
    ekran.delete(0, tk.END)
    ekran.insert(0, aktualne_rownanie)

def oblicz():
    global aktualne_rownanie
    try:
        wynik = str(eval(aktualne_rownanie))
        ekran.delete(0, tk.END)
        ekran.insert(0, wynik)
        aktualne_rownanie = wynik
    except:
        ekran.delete(0, tk.END)
        ekran.insert(0, "Błąd")
        aktualne_rownanie = ""
def wyczysc():
    global aktualne_rownanie
    aktualne_rownanie = ""
    ekran.delete(0, tk.END)

#okno
okno = tk.Tk()
okno.title("Kalkulator")
okno.geometry("540x410")
okno.configure(background="gray")
ekran = tk.Entry(okno, width=14, font=("Arial", 24), bg="#3F3F3F", fg="white")
ekran.grid(row=0, column=0, columnspan=4, sticky="ew")

#przycisk 0

btn = tk.Button(okno, text="0", font=("Arial",18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("0"))
btn.grid(row=5, column=1)

#przycisk 1

btn = tk.Button(okno, text="1", font=("Arial", 18), width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("1"))
btn.grid(row=4, column=0)

#przycisk 2

btn = tk.Button(okno, text="2", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("2"))
btn.grid(row=4, column=1)

#przycisk 3

btn = tk.Button(okno, text="3", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("3"))
btn.grid(row=4, column=2)

#przycisk 4

btn = tk.Button(okno, text="4", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("4"))
btn.grid(row=3, column=0)

#przycisk 5

btn = tk.Button(okno, text="5", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("5"))
btn.grid(row=3, column=1)

#przycisk 6

btn = tk.Button(okno, text="6", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("6"))
btn.grid(row=3, column=2)

#przycisk 7

btn = tk.Button(okno, text="7", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("7"))
btn.grid(row=2, column=0)

#przycisk 8

btn = tk.Button(okno, text="8", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("8"))
btn.grid(row=2, column=1)

#przycisk 9

btn = tk.Button(okno, text="9", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("9"))
btn.grid(row=2, column=2)

#przyick +
btn = tk.Button(okno, text="+", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("+"))
btn.grid(row=2, column=3)

#przycisk -

btn = tk.Button(okno, text="-", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("-"))
btn.grid(row=3, column=3)

# przycisk *
btn_mnoz = tk.Button(okno, text="*", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("*"))
btn_mnoz.grid(row=1, column=2)

# przycisk /
btn_dziel = tk.Button(okno, text="/", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("/"))
btn_dziel.grid(row=1, column=3)

# przycisk ^
btn_potega = tk.Button(okno, text="^", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("**"))
btn_potega.grid(row=1, column=1)

# przycisk sqrt
btn_potega = tk.Button(okno, text="√", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("**0.5"))
btn_potega.grid(row=1, column=0)

#przycisk =

btn = tk.Button(okno, text="=", font=("Arial", 18),width=9, height=2,bg="#FF8C00",fg="black", command=lambda: oblicz())
btn.grid(row=4, column=3)

#przycisk Clear

btn = tk.Button(okno, text="C", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: wyczysc())
btn.grid(row=5, column=2)

#przycisk .

btn = tk.Button(okno, text=".", font=("Arial", 18),width=9, height=2,bg="#6F6F6F",fg="white", command=lambda: dodaj_znak("."))
btn.grid(row=5, column=0)

okno.mainloop()