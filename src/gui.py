## 
# @file gui.py
# @brief GUI pre kalkulačku
# @author Kristián Pribila


from pathlib import Path
from tkinter import *
import tkinter as tk
from tkinter import Tk, Canvas, Button, PhotoImage
import parse as parse


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("500x700")
window.configure(bg = "#808080")
window.title("LPH Kalkulačka")


canvas = Canvas(
    window,
    bg = "#808080",
    height = 700,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    500.0,
    69.0,
    fill="#808080",
    outline="")


canvas.create_rectangle(
    15.0,
    116.0,
    481.0,
    242.0,
    fill="#D9D9D9",
    outline="")


custom_font = ("Inter", 22, "bold") 

##
# @brief Zaznamenanie inputu z klávesnice
# @param event Stlačené tlačidlo
def handle_key(event):
    if event.char.isdigit() or event.char in "+-*/.!^(),epilogn":
        button_click(event.char)
    elif event.keysym == "Return":
        button_answer()
    elif event.keysym == "BackSpace":
        button_delete()
    return "break"

e = tk.Entry(canvas, font=custom_font)
e.place(x=15, y=116, width=466, height=126)
e.focus_set()
e.bind("<Key>", handle_key)

 
ans = "" 
cond = 0
cond2 = 0
comma = ""

##
# @brief Stlačenie tlačidla 
#
# Pri každom stlačení niektorého z tlačidiel sa pomocu funkcie button_click pošle danný string a ten sa následne vytlačí 
# po každom pridaní daľšieho znaku
#
# @param number číslo 

def button_click(number):
    global cond2
    global comma
    current = e.get()
    e.delete(0, END)
    e.insert(0,current + number)
    global ans
    ans = str(current + number)
    if cond2==1:
        comma=str(",")
        e.delete(0, END)
        e.insert(0,current + number + comma)
    cond2=0

##
# @brief Stlačenie tlačidla logaritmus 
#
# Po stlační logaritmu sa vytlačí log( a nastavý sa podmienka vypísania čiarky "cond2" je to kvoli parseru ten berie logaritmus 
# ako log(a,b) kde a je zaklad a b je argument
#
# @param number základ logaritmu 

def button_logaritm(number):
    global cond2
    cond2 = 1
    current = e.get()
    e.delete(0, END)
    e.insert(0,current + number )

##    
# @brief Stlačenie tlačidla answer
#
# Po stlační tlačidla answer sa vytlačí odpoveď s predošlého výpočtu. Riadiaca podmienka sa vyhodnocuje v funkcii button_equal 
# pretože na žiatku je výsledok prázdny string
#
# @param ans funkcia dostáva string 

def button_answer(ans):
    new_ans=""
    global cond
    if cond==1:
        try:
            result = parse.evaluate(ans)
        except (SyntaxError) as error:
            result = error
        e.delete(0, END)
        e.insert(0,result)
        cond = 0
        new_ans=ans
    else:
        e.insert(0,new_ans)


##        
# @brief Stlačenie tlačidla delete
#
# Po stlační tlačidla delete odstráni posledný znak z pola a vymaže ho z okna. 
# 
def button_delete():
    global ans
    ans = ans[:-1]
    e.delete(0, END)
    e.insert(0,ans)

##
# @brief Stlačenie tlačidla rovná sa
#
# Po stlační tlačidla rovná sa , to posiela string parseru ktorý ho vyhodnotí a pošle string späť.
#
# @param ans predošlý výraz
# @return funkcia evaluate vracia string
def button_equal(ans):
    try:
        result = parse.evaluate(ans)
    except (SyntaxError) as error:
        result = error
    global cond
    cond=1
    e.delete(0, END)
    e.insert(0,str(result))

##
# @brief Stlačenie tlačidla clear all
#
# Po stlačení tlačidla ac sa vymaže obsah celého okna
#
def button_clear():
    e.delete(0, END)


def button_help():
    root = Tk()

    root.geometry("500x700")
    root.configure(bg = "#808080")
    root.title("Help")



    canvas = Canvas(
        root,
        bg = "#808080",
        height = 700,
        width = 500,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )
    
    canvas.place(x = 0, y = 0)
    
    canvas.create_rectangle(
        0.0,
        0.0,
        500.0,
        69.0,
        fill="#808080",
        outline="")

    help_font = ("Inter", 12, "bold") 
    log_text = "Logaritmus sa zapisuje v našej kalkulačke ako log(a,b) kde a je základ logaritmu a b je aurgument"
    del_text = "Tlačidlo DEL vymazáva posledný pridaný znak tak ako backspace"
    ans_text = "Tlačidlo ANS vracia posledný zapísaný príkald"
    ac_text = "Tlačidlo AC vymaže celý obsah displeja kalkulačky"
    sqrt_text = "Odmocnina sa zapisuje v tvare 5√125"
    celoc_text = "Celočíselné delenie sa zapisuje v našej kalkulačke ako 3//2 "
    fac_text = "Faktoriál zapisujeme v tvare 5!"
    

    delete = tk.Label(root, text=del_text,font=help_font, bg="#808080",wraplength=490)
    delete.place(x=10,y=40)

    ans = tk.Label(root, text=ans_text,font=help_font, bg="#808080",wraplength=490)
    ans.place(x=10,y=90)

    ac = tk.Label(root, text=ac_text,font=help_font, bg="#808080",wraplength=490)
    ac.place(x=10,y=140)
    
    sqrt = tk.Label(root, text=sqrt_text,font=help_font, bg="#808080",wraplength=490)
    sqrt.place(x=10,y=190)

    celoc = tk.Label(root, text=celoc_text,font=help_font, bg="#808080",wraplength=490)
    celoc.place(x=10,y=240)

    fac = tk.Label(root, text=fac_text,font=help_font, bg="#808080",wraplength=490)
    fac.place(x=10,y=300)

    log = tk.Label(root, text=log_text,font=help_font, bg="#808080",wraplength=490)
    log.place(x=10,y=340)
    
    
    
    root.resizable(False, False)
    root.mainloop()


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_0 = Button(window,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("0"),
    relief="flat"
)
button_0.place(
    x=22.0,
    y=603.0,
    width=70.0,
    height=41.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_1 = Button(window,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("1"),
    relief="flat"
)
button_1.place(
    x=21.0,
    y=543.0,
    width=70.0,
    height=41.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_4 = Button(window,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("4"),
    relief="flat"
)
button_4.place(
    x=21.0,
    y=484.0,
    width=70.0,
    height=41.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_7 = Button(window,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("7"),
    relief="flat"
)
button_7.place(
    x=22.0,
    y=426.0,
    width=70.0,
    height=41.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_com = Button(window,
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("."),
    relief="flat"
)
button_com.place(
    x=118.0,
    y=603.0,
    width=70.0,
    height=41.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_2 = Button(window,
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("2"),
    relief="flat"
)
button_2.place(
    x=117.0,
    y=543.0,
    width=70.0,
    height=41.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_5 = Button(window,
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("5"),
    relief="flat"
)
button_5.place(
    x=117.0,
    y=484.0,
    width=70.0,
    height=41.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_8 = Button(window,
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("8"),
    relief="flat"
)
button_8.place(
    x=118.0,
    y=426.0,
    width=70.0,
    height=41.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_pi = Button(window,
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("π"),
    relief="flat"
)
button_pi.place(
    x=213.0,
    y=603.0,
    width=70.0,
    height=41.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_3 = Button(window,
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("3"),
    relief="flat"
)
button_3.place(
    x=212.0,
    y=543.0,
    width=70.0,
    height=41.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_eq = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_equal(str(ans)),
    relief="flat"
)
button_eq.place(
    x=411.0,
    y=603.0,
    width=70.0,
    height=41.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_6 = Button(window,
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("6"),
    relief="flat"
)
button_6.place(
    x=212.0,
    y=484.0,
    width=70.0,
    height=41.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_9 = Button(window,
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("9"),
    relief="flat"
)
button_9.place(
    x=213.0,
    y=426.0,
    width=70.0,
    height=41.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_plus = Button(window,
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("+"),
    relief="flat"
)
button_plus.place(
    x=312.0,
    y=543.0,
    width=70.0,
    height=41.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_mul = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("*"),
    relief="flat"
)
button_mul.place(
    x=312.0,
    y=484.0,
    width=70.0,
    height=41.0
)


button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_min = Button(window,
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("-"),
    relief="flat"
)
button_min.place(
    x=411.0,
    y=543.0,
    width=70.0,
    height=41.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_div = Button(window,
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("/"),
    relief="flat"
)
button_div.place(
    x=411.0,
    y=484.0,
    width=70.0,
    height=41.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_del = Button(window,
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=button_delete,
    relief="flat"
)
button_del.place(
    x=312.0,
    y=426.0,
    width=70.0,
    height=41.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_pow = Button(window,
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("^("),
    relief="flat"
)
button_pow.place(
    x=22.0,
    y=281.0,
    width=70.0,
    height=41.0
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_fac = Button(window,
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("!"),
    relief="flat"
)
button_fac.place(
    x=22.0,
    y=336.0,
    width=70.0,
    height=41.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_r2 = Button(window,
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("^(2)"),
    relief="flat"
)
button_r2.place(
    x=117.0,
    y=281.0,
    width=70.0,
    height=41.0
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
button_lb = Button(window,
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("("),
    relief="flat"
)
button_lb.place(
    x=117.0,
    y=336.0,
    width=70.0,
    height=41.0
)

button_image_28 = PhotoImage(
    file=relative_to_assets("button_28.png"))
button_rb = Button(window,
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click(")"),
    relief="flat"
)
button_rb.place(
    x=212.0,
    y=337.0,
    width=70.0,
    height=41.0
)

button_image_29 = PhotoImage(
    file=relative_to_assets("button_29.png"))
button_ln = Button(window,
    image=button_image_29,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("ln("),
    relief="flat"
)
button_ln.place(
    x=312.0,
    y=281.0,
    width=70.0,
    height=41.0
)

button_image_30 = PhotoImage(
    file=relative_to_assets("button_30.png"))
button_e = Button(window,
    image=button_image_30,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("e^("),
    relief="flat"
)
button_e.place(
    x=213.0,
    y=281.0,
    width=70.0,
    height=41.0
)

button_image_31 = PhotoImage(
    file=relative_to_assets("button_31.png"))
button_ac = Button(window,
    image=button_image_31,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_clear(),
    relief="flat"
)
button_ac.place(
    x=411.0,
    y=426.0,
    width=70.0,
    height=41.0
)

button_image_32 = PhotoImage(
    file=relative_to_assets("button_32.png"))
button_ans = Button(
    image=button_image_32,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_answer(ans),
    relief="flat"
)
button_ans.place(
    x=312.0,
    y=603.0,
    width=70.0,
    height=41.0
)

button_image_33 = PhotoImage(
    file=relative_to_assets("button_33.png"))
button_sqrt2 = Button(window,
    image=button_image_33,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("2√("),
    relief="flat"
)
button_sqrt2.place(
    x=312.0,
    y=337.0,
    width=70.0,
    height=41.0
)

button_image_34 = PhotoImage(
    file=relative_to_assets("button_34.png"))
button_log = Button(window,
    image=button_image_34,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_logaritm("log("),
    relief="flat"
)
button_log.place(
    x=394.0,
    y=278.0,
    width=91.0,
    height=47.0 
)

button_image_35 = PhotoImage(
    file=relative_to_assets("button_35.png"))
button_sqrtx = Button(window,
    image=button_image_35,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_click("√("),
    relief="flat"
)
button_sqrtx.place(
    x=393.0,
    y=335.0,
    width=89.0,
    height=43.0
)

button_image_36 = PhotoImage(
    file=relative_to_assets("button_36.png"))
button_h = Button(window,
    image=button_image_36,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button_help(),
    relief="flat"
)
button_h.place(
    x=21.0,
    y=18.0,
    width=42.0,
    height=32.0
)


window.resizable(False, False)
window.mainloop()
