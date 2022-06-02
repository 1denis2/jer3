import tkinter
from tkinter import *
import requests
from io import BytesIO
from PIL import Image,ImageTk

###def col_c():
    ##if col_c > 0:
         ###   lbl2.configure(fg='green')
   ## else:
  ##          lbl5.configure(fg='red')

def find(symbol):
    key = '56de8b33-426c-462a-8aab-a01fb8405164'
    api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
    api += key
    ans = requests.get(api).json()
    for item in ans['data']:
        if  symbol.lower() == item['symbol'].lower():
            r = requests.get(url=f'https://s2.coinmarketcap.com/static/img/coins/64x64/{item.get("id")}.png')
            pil_image = Image.open(BytesIO(r.content))
            pil_image.save(BytesIO(), format='PNG')
            pil_image.thumbnail((35, 35))

            img = ImageTk.PhotoImage(pil_image)
            Label1 = tkinter.Label(image=img)
            Label1.image = img
            Label1.place(x=45, y=150,)

    for i in ans['data']:
        if symbol.lower() == i['symbol'].lower():
            price =f"{round(i['quote']['USD']['price'],3)}$"
            s = i['symbol']
            price2 = f"{round(i['quote']['USD']['percent_change_30d'],4)}%"
            price3 = f"{round(i['quote']['USD']['percent_change_7d'],4)}%"

            lbl2.configure(text=f"{price}")
            lbl3.configure(text=f"{s}")
            lbl4.configure(text='Цена \n За 7 дней')
            lbl5.configure(text= f"{price2}")
            lbl6.configure(text= f"{price3}")
            lbl7.configure(text='Цена \n За 30 дней')
            lbl8.configure(text='Цена \n')


            if i['quote']['USD']['percent_change_7d'] < 0:
                lbl2.configure(fg='black') ## Цена вверх
                lbl6.configure(fg='red') ## за 7 дней низ
               ## lbl5.configure(fg='red') ## за 30 дней середина
            else:
                lbl6.configure(fg='green')
               ## lbl5.configure(fg='green')
                lbl2.configure(fg='black')
            if i['quote']['USD']['percent_change_30d'] < 0:
                        lbl5.configure(fg='red')## за 30 дней середина
            else:
                        lbl5.configure(fg='green')




window = Tk()
var = IntVar()
window.geometry("600x600")
window.resizable(width=False, height=False)
window.title("Парсинг криптовалюты")
window.iconphoto(True, PhotoImage(file='1.png'))
###indow.configure(background='w'
def clear():
    e1.delete(0,'end')
e1 = Entry(window)
e1.configure(borderwidth=5,)
e1.place(x=40,y=100,width=150)
b1 = Button(window,bg='red',fg='white',text='Найти',command=lambda: find(e1.get()))
b1.place(x=200,y=100,width=50)
b2 = Button(window,bg='black',fg='white', text='Очистить',command=clear)
b2.place(x=300,y=100,width=80)
lbl2 = Label(window, text=" ", font=("Comic Sans", 18)) ## Цена цифры
lbl2.place(x=200,y=205)
lbl3 = Label(window, text=" ", font=("Comic Sans", 18)) ## Символы (имя)
lbl3.place(x=200,y=150)
lbl4 = Label(window, text=" ", font=("Comic Sans", 15)) ## Цена за 7 дней text
lbl4.place(x=20,y=300)
lbl5 = Label(window, text=" ", font=("Comic Sans", 18)) ## Цена за 30 дней цифры
lbl5.place(x=200,y=400)
lbl6 = Label(window, text=" ", font=("Comic Sans", 18)) ## Цена за 7 дней цифры
lbl6.place(x=200,y=300)
lbl7 = Label(window, text=" ", font=("Comic Sans", 15)) ## Цена за 30 дней text
lbl7.place(x=20,y=400)
lbl8 = Label(window, text=" ", font=("Comic Sans", 15)) ## Цена текст
lbl8.place(x=40,y=200)
def night():
    ##lbl['bg'] = '#000000'
    lbl7['bg'] ='#ffb6c1'
    lbl4['bg'] ='#ffb6c1'
    lbl3['bg'] ='#ffb6c1'
    lbl8['bg'] ='#ffb6c1'
    lbl6['bg'] = '#ffb6c1'
    lbl5['bg'] = '#ffb6c1'
    lbl2['bg'] = '#ffb6c1'
    rad2['bg'] = '#ffb6c1'
    rad1['bg'] = '#ffb6c1'
    window.configure(bg='light pink')
def day():
    ##lbl['bg'] = '#000000'
    lbl7['bg'] = '#ffffff'
    lbl4['bg'] = '#ffffff'
    lbl3['bg'] = '#ffffff'
    lbl8['bg'] = '#ffffff'
    lbl6['bg'] = '#ffffff'
    lbl5['bg'] = '#ffffff'
    lbl2['bg'] = '#ffffff'
    rad2['bg'] = '#ffffff'
    rad1['bg'] = '#ffffff'
    window.configure(bg='white')
rad1 = Radiobutton(window,text='Розовый',value =1,command=night, variable = var)
rad2 = Radiobutton(window,text='Белый',value =2,command=day, variable = var)
rad1.place(x=320,y=180) ## розовый
rad2.place(x=320,y=150) ## белый
text = e1.get()
window.mainloop()
