# !/usr/bin/python
# -*- coding:utf-8 -*-
# author: huayang
# time: 2021.4.10

import json

import base64

import hashlib

import binascii

import webbrowser

import urllib.parse

import tkinter

from tkinter import *

from tkinter import ttk

from tkinter import scrolledtext

print('程序正在启动中请稍后\...')
print('程序正在启动中请稍后\......')
print('程序正在启动中请稍后\.........')
print('程序正在启动中请稍后\............')
print('程序正在启动中请稍后\...............')
print('程序正在启动中请稍后\.................')
print('程序正在启动中请稍后\...................')
print('程序正在启动中请稍后\......................')
print('程序正在启动中请稍后\........................')

window = Tk()

ttk.Style().configure(".", font=("仿宋", 15))

window.title('编码/解码工具 @hellohy.top V1.0')

window.geometry("1068x681")

window.wm_resizable(False,False)

#顶部菜单

tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='base编码/解码')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='MD5加密')

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='进制转换')

tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='url编码')

tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text='json格式化')

tab6 = ttk.Frame(tabControl)
tabControl.add(tab6, text='hex编码')

tab7 = ttk.Frame(tabControl)
tabControl.add(tab7, text='特殊的ascii')

tab8 = ttk.Frame(tabControl)
tabControl.add(tab8, text='骚操作')

tab9 = ttk.Frame(tabControl)
tabControl.add(tab9, text='关于&日志')

tabControl.pack(expand=1, fill="both")

#------------------------------

#base64编码/解码
book = tkinter.StringVar()

bookChosen = ttk.Combobox(tab1,width=8,textvariable=book,)

bookChosen['values'] = ('base64', 'base32', 'base16')

bookChosen.place(x = 475,y = 270)

bookChosen.current(0)

bookChosen.config(state='readonly')

def getValue():
    if bookChosen.get() == 'base64':
        def b64_en():

            txt = scr1.get('0.0', 'end')

            strip = txt.strip('\n')

            e = base64.b64encode(strip.encode('utf-8')).decode('ascii')

            scr2.insert(END, e)

            scr2.insert(END, '\n')

        def b64_de():

            txt = scr1.get('0.0', 'end')

            strip = txt.strip('\n')

            e = base64.b64decode(strip.encode('utf-8'))

            b = e.decode()

            scr2.insert(END, b)

            scr2.insert(END, '\n')

        def empty():

            scr1.delete('0.0', 'end')
            scr2.delete('0.0', 'end')

        scr1 = scrolledtext.ScrolledText(tab1,width=45, height=38, font=(1))

        scr2 = scrolledtext.ScrolledText(tab1,width=48, height=38, font=(1))

        scr1.place(x=0, y=0)

        scr2.place(x=573, y=0)

        button = Button(tab1,text="编 码-->", width=6, height=2, command=b64_en)

        button.place(x=495, y=150)

        button = Button(tab1,text="解 码-->", width=6, height=2, command=b64_de)

        button.place(x=495, y=410)

        button = Button(tab1,text="一清\n键空", width=6, height=3, command=empty)

        button.place(x=495, y=550)



    if bookChosen.get() == 'base32':
        def b32_en():

            txt = scr3.get('0.0', 'end')

            strip = txt.strip('\n')

            e = base64.b32encode(strip.encode('utf-8')).decode('ascii')

            scr4.insert(END, e)

            scr4.insert(END, '\n')

        def b32_de():

            txt = scr3.get('0.0', 'end')

            strip = txt.strip('\n')

            e = base64.b32decode(strip.encode('utf-8'))

            b = e.decode()

            scr4.insert(END, b)

            scr4.insert(END, '\n')

        def empty():

            scr3.delete('0.0', 'end')
            scr4.delete('0.0', 'end')

        button = Button(tab1,text="编 码-->", width=6, height=2, command=b32_en)

        button.place(x=495, y=150)

        button = Button(tab1,text="解 码-->", width=6, height=2, command=b32_de)

        button.place(x=495, y=410)

        button = Button(tab1,text="一清\n键空", width=6, height=3, command=empty)

        button.place(x=495, y=550)

        scr3 = scrolledtext.ScrolledText(tab1,width=45, height=38, font=(1))

        scr4 = scrolledtext.ScrolledText(tab1,width=48, height=38, font=(1))

        scr3.place(x=0, y=0)

        scr4.place(x=573, y=0)
    if bookChosen.get() == 'base16':
        def b16_en():

            txt = scr5.get('0.0', 'end')

            strip = txt.strip('\n')

            e = base64.b16encode(strip.encode('utf-8')).decode('ascii')

            scr6.insert(END, e)

            scr6.insert(END, '\n')

        def b16_de():

            txt = scr5.get('0.0', 'end')

            strip = txt.strip('\n')

            e = base64.b16decode(strip.encode('utf-8'))

            b = e.decode()

            scr6.insert(END, b)

            scr6.insert(END, '\n')

        def empty():

            scr5.delete('0.0', 'end')
            scr6.delete('0.0', 'end')

        button = Button(tab1,text="编 码-->", width=6, height=2, command=b16_en)

        button.place(x=495, y=150)

        button = Button(tab1,text="解 码-->", width=6, height=2, command=b16_de)

        button.place(x=495, y=410)

        button = Button(tab1,text="一清\n键空", width=6, height=3, command=empty)

        button.place(x=495, y=550)

        scr5 = scrolledtext.ScrolledText(tab1,width=45, height=38, font=(1))

        scr6 = scrolledtext.ScrolledText(tab1,width=48, height=38, font=(1))

        scr5.place(x=0, y=0)

        scr6.place(x=573, y=0)

button = tkinter.Button(tab1,text="确认", width=6, pady=1, command=getValue)
button.place(x = 495,y = 305)

#------------------------------

#MD5加密
def MD5():

    txt = scr1_MD5.get('0.0', 'end')

    strip = txt.strip('\n')

    md5 = hashlib.md5()

    b = strip.encode(encoding='utf-8')

    md5.update(b)

    str_md5 = md5.hexdigest()

    scr2_MD5.insert(END, str_md5)

    scr2_MD5.insert(END, '\n')


def empty():  # 清除

    scr1_MD5.delete('0.0', 'end')
    scr2_MD5.delete('0.0', 'end')

scr1_MD5 = scrolledtext.ScrolledText(tab2, width=45, height=38, font=(1))

scr2_MD5 = scrolledtext.ScrolledText(tab2, width=48, height=38, font=(1))

scr1_MD5.place(x=0, y=0)

scr2_MD5.place(x=573, y=0)

button = Button(tab2, text="编 码-->", width=6, height=2, command=MD5)

button.place(x=495, y=220)

button = Button(tab2, text="一清\n键空", width=6, height=3, command=empty)

button.place(x=495, y=550)

#------------------------------
#进制转换

w = tkinter.Label(tab3, text="请在左边第一个方框输入：",font=("楷体", 12))
w.place(x=840, y=5)

book = tkinter.StringVar()

bookChosen2 = ttk.Combobox(tab3,width=8)

bookChosen2['values'] = ('二进制','八进制','十进制','十六进制')

bookChosen2.place(x = 880,y = 40)

bookChosen2.current(0)

bookChosen2.config(state='readonly')

scr1 = scrolledtext.ScrolledText(tab3, width=83, height=7, font=(1))
scr1.place(x=0, y=35)

scr2 = scrolledtext.ScrolledText(tab3, width=83, height=8, font=(1))
scr2.place(x=0, y=180)

scr3 = scrolledtext.ScrolledText(tab3, width=83, height=8, font=(1))
scr3.place(x=0, y=335)

scr4 = scrolledtext.ScrolledText(tab3, width=83, height=8, font=(1))
scr4.place(x=0, y=490)

#标题及窗口位置

def position():
    if bookChosen2.get() == '二进制':
        w = tkinter.Label(tab3, text="二进制")
        w.place(x=350, y=150)

        w = tkinter.Label(tab3, text="八进制")
        w.place(x=350, y=305)

        w = tkinter.Label(tab3, text="十进制")
        w.place(x=350, y=460)

        w = tkinter.Label(tab3, text="十六进制")
        w.place(x=350, y=620)
    if bookChosen2.get() == '八进制':
        w = tkinter.Label(tab3, text="八进制")
        w.place(x=350, y=150)

        w = tkinter.Label(tab3, text="二进制")
        w.place(x=350, y=305)

        w = tkinter.Label(tab3, text="十进制")
        w.place(x=350, y=460)

        w = tkinter.Label(tab3, text="十六进制")
        w.place(x=350, y=620)
    if bookChosen2.get() == '十进制':
        w = tkinter.Label(tab3, text="十进制")
        w.place(x=350, y=150)

        w = tkinter.Label(tab3, text="八进制")
        w.place(x=350, y=305)

        w = tkinter.Label(tab3, text="二进制")
        w.place(x=350, y=460)

        w = tkinter.Label(tab3, text="十六进制")
        w.place(x=350, y=620)
    if bookChosen2.get() == '十六进制':
        w = tkinter.Label(tab3, text="十六进制")
        w.place(x=350, y=150)

        w = tkinter.Label(tab3, text="八进制")
        w.place(x=350, y=305)

        w = tkinter.Label(tab3, text="十进制")
        w.place(x=350, y=460)

        w = tkinter.Label(tab3, text="二进制")
        w.place(x=350, y=620)

button = tkinter.Button(tab3, text="确认", width=6, pady=1, command=position)
button.place(x=895, y=75)

#转码
def turn():
    if bookChosen2.get() == '二进制':

        # 2  ->  8

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = oct(int(strip, 2))[2:]

        scr2.insert(END, e)

        scr2.insert(END, '\n')

        # 2  ->  10

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = int(strip, 2)

        scr3.insert(END, e)

        scr3.insert(END, '\n')

        # 2  ->  16

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = hex(int(strip, 2))[2:]

        scr4.insert(END, e)

        scr4.insert(END, '\n')

    if bookChosen2.get() == '八进制':

        # 8  ->  2

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = bin(int(strip, 8))[2:]

        scr2.insert(END, e)

        scr2.insert(END, '\n')

        # 8  ->  10

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = int(strip, 8)

        scr3.insert(END, e)

        scr3.insert(END, '\n')

        # 8  ->  16

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = hex(int(strip, 8))[2:]

        scr4.insert(END, e)

        scr4.insert(END, '\n')

    if bookChosen2.get() == '十进制':

        # 10  ->  8

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = oct(int(strip, 10))[2:]

        scr2.insert(END, e)

        scr2.insert(END, '\n')

        # 10  ->  2

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = bin(int(strip, 10))[2:]

        scr3.insert(END, e)

        scr3.insert(END, '\n')

        # 10  ->  16

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = hex(int(strip))[2:]

        scr4.insert(END, e)

        scr4.insert(END, '\n')

    if bookChosen2.get() == '十六进制':

        # 16  ->  8

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = oct(int(strip, 16))[2:]

        scr2.insert(END, e)

        scr2.insert(END, '\n')

        # 16  ->  10

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = int(strip, 16)

        scr3.insert(END, e)

        scr3.insert(END, '\n')

        # 16  ->  2

        txt = scr1.get('0.0', 'end')

        strip = txt.strip('\n')

        e = bin(int(strip, 16))[2:]

        scr4.insert(END, e)

        scr4.insert(END, '\n')


def empty():  # 清除

    scr1.delete('0.0', 'end')
    scr2.delete('0.0', 'end')
    scr3.delete('0.0', 'end')
    scr4.delete('0.0', 'end')

button1 = Button(tab3, text="tm的\n给\n👴\n转!!!!", width=8, height=4, command=turn,font=('宋体', 20, 'bold', 'italic'))

button1.place(x=870, y=200)
#
button2 = Button(tab3, text="给\n👴🏻\n爬\n!", width=4, height=6, command=empty,font=('宋体', 20, 'bold', 'italic'))

button2.place(x=900, y=410)

# ------------------------------
# url编码

def url_en():

    txt = scr1_url.get('0.0', 'end')

    strip = txt.strip('\n')

    e = urllib.parse.quote(strip)

    scr2_url.insert(END, e)

    scr2_url.insert(END, '\n')

def url_de():

    txt = scr1_url.get('0.0', 'end')

    strip = txt.strip('\n')

    e = urllib.parse.unquote(strip)

    scr2_url.insert(END, e)

    scr2_url.insert(END, '\n')

def empty():

    scr1_url.delete('0.0', 'end')
    scr2_url.delete('0.0', 'end')

scr1_url = scrolledtext.ScrolledText(tab4, width=45, height=38, font=(1))

scr2_url = scrolledtext.ScrolledText(tab4, width=48, height=38, font=(1))

scr1_url.place(x=0, y=0)

scr2_url.place(x=573, y=0)

button = Button(tab4, text="编 码-->", width=6, height=2, command=url_en)

button.place(x=495, y=220)

button = Button(tab4,text="解 码-->", width=6, height=2, command=url_de)

button.place(x=495, y=410)

button = Button(tab4, text="一清\n键空", width=6, height=3, command=empty)

button.place(x=495, y=550)

#---------------------------------------
#json格式

def json1():#注意这里函数名不能为json会和下面的函数冲突

    txt = scr1_json.get('0.0', 'end')

    a = json.loads(txt)

    b = json.dumps(a,sort_keys=True,indent=4,separators=(',','：'),ensure_ascii=False)

    scr2_json.insert(END,b)

    scr2_json.insert(END, '\n')


def empty():  # 清除

    scr1_json.delete('0.0', 'end')
    scr2_json.delete('0.0', 'end')

scr1_json = scrolledtext.ScrolledText(tab5,width=45, height=38, font=(1))

scr2_json = scrolledtext.ScrolledText(tab5, width=48, height=38, font=(1))

scr1_json.place(x=0, y=0)

scr2_json.place(x=573, y=0)

scr1_json.insert(END, '{"name":"huayang","url":"https://hellohy.top"}')

button = Button(tab5, text="转 换-->", width=6, height=2, command=json1)

button.place(x=495, y=220)

button = Button(tab5, text="一清\n键空", width=6, height=3, command=empty)

button.place(x=495, y=550)

# -----------------------
# hex编码
book3 = tkinter.StringVar()

bookChosen3 = ttk.Combobox(tab6,width=8,textvariable=book3,)

bookChosen3['values'] = ('基本型','加上0x', '加上%','加上\\x')

bookChosen3.place(x = 475,y = 270)

bookChosen3.current(0)

bookChosen3.config(state='readonly')


def hex1():
#基本型
    if bookChosen3.get() == '基本型':
        def hex1_en():

            txt = scr1_hex.get('0.0', 'end')

            strip = txt.strip('\n')

            e = base64.b16encode(strip.encode('utf-8')).decode('ascii')

            scr2_hex.insert(END, e)

            scr2_hex.insert(END, '\n')

        def hex1_de():

            txt = scr1_hex.get('0.0', 'end')

            strip = txt.strip('\n')

            e = binascii.a2b_hex(strip).decode()

            scr2_hex.insert(END, e)

            scr2_hex.insert(END, '\n')

        def empty():

            scr1_hex.delete('0.0', 'end')
            scr2_hex.delete('0.0', 'end')

        button = Button(tab6,text="编 码-->", width=6, height=2, command=hex1_en)

        button.place(x=495, y=150)

        button = Button(tab6,text="解 码-->", width=6, height=2, command=hex1_de)

        button.place(x=495, y=410)

        button = Button(tab6,text="一清\n键空", width=6, height=3, command=empty)

        button.place(x=495, y=550)

        scr1_hex = scrolledtext.ScrolledText(tab6,width=45, height=38, font=(1))

        scr2_hex = scrolledtext.ScrolledText(tab6,width=48, height=38, font=(1))

        scr1_hex.place(x=0, y=0)

        scr2_hex.place(x=573, y=0)

#加上0x
    if bookChosen3.get() == '加上0x':
        def hex2_en():

            txt = scr3_hex.get('0.0', 'end')

            strip = txt.strip('\n')

            total = ''

            for i in strip:

                e = base64.b16encode(i.encode('utf-8')).decode('ascii')

                total += '0x' + e

            scr4_hex.insert(END, total)

            scr4_hex.insert(END, '\n')

        def hex2_de():

            txt = scr3_hex.get('0.0', 'end')

            strip = txt.strip('\n')

            strip2 = strip.replace('0x','')

            e = binascii.a2b_hex(strip2).decode()

            scr4_hex.insert(END, e)

            scr4_hex.insert(END, '\n')

        def empty():

            scr3_hex.delete('0.0', 'end')
            scr4_hex.delete('0.0', 'end')

        button = Button(tab6,text="编 码-->", width=6, height=2, command=hex2_en)

        button.place(x=495, y=150)

        button = Button(tab6,text="解 码-->", width=6, height=2, command=hex2_de)

        button.place(x=495, y=410)

        button = Button(tab6,text="一清\n键空", width=6, height=3, command=empty)

        button.place(x=495, y=550)

        scr3_hex = scrolledtext.ScrolledText(tab6,width=45, height=38, font=(1))

        scr4_hex = scrolledtext.ScrolledText(tab6,width=48, height=38, font=(1))

        scr3_hex.place(x=0, y=0)

        scr4_hex.place(x=573, y=0)

#加上%编码
    if bookChosen3.get() == '加上%':
        def hex3_en():

            txt = scr5_hex.get('0.0', 'end')

            strip = txt.strip('\n')

            total = ''

            for i in strip:

                e = base64.b16encode(i.encode('utf-8')).decode('ascii')

                total += '%' + e

            scr6_hex.insert(END, total)

            scr6_hex.insert(END, '\n')

        def hex3_de():

            txt = scr5_hex.get('0.0', 'end')

            strip = txt.strip('\n')

            strip2 = strip.replace('%','')

            e = binascii.a2b_hex(strip2).decode()

            scr6_hex.insert(END, e)

            scr6_hex.insert(END, '\n')

        def empty():

            scr5_hex.delete('0.0', 'end')
            scr6_hex.delete('0.0', 'end')

        button = Button(tab6,text="编 码-->", width=6, height=2, command=hex3_en)

        button.place(x=495, y=150)

        button = Button(tab6,text="解 码-->", width=6, height=2, command=hex3_de)

        button.place(x=495, y=410)

        button = Button(tab6,text="一清\n键空", width=6, height=3, command=empty)

        button.place(x=495, y=550)

        scr5_hex = scrolledtext.ScrolledText(tab6,width=45, height=38, font=(1))

        scr6_hex = scrolledtext.ScrolledText(tab6,width=48, height=38, font=(1))

        scr5_hex.place(x=0, y=0)

        scr6_hex.place(x=573, y=0)

#加上\x编码
    if bookChosen3.get() == '加上\\x':
        def hex4_en():

            txt = scr7_hex.get('0.0', 'end')

            strip = txt.strip('\n')

            total = ''

            for i in strip:

                e = base64.b16encode(i.encode('utf-8')).decode('ascii')

                total += '\\x' + e

            scr8_hex.insert(END, total)

            scr8_hex.insert(END, '\n')

        def hex4_de():

            txt = scr7_hex.get('0.0', 'end')

            strip = txt.strip('\n')

            strip2 = strip.replace('\\x','')

            e = binascii.a2b_hex(strip2).decode()

            scr8_hex.insert(END, e)

            scr8_hex.insert(END, '\n')

        def empty():

            scr7_hex.delete('0.0', 'end')
            scr8_hex.delete('0.0', 'end')

        button = Button(tab6,text="编 码-->", width=6, height=2, command=hex4_en)

        button.place(x=495, y=150)

        button = Button(tab6,text="解 码-->", width=6, height=2, command=hex4_de)

        button.place(x=495, y=410)

        button = Button(tab6,text="一清\n键空", width=6, height=3, command=empty)

        button.place(x=495, y=550)

        scr7_hex = scrolledtext.ScrolledText(tab6,width=45, height=38, font=(1))

        scr8_hex = scrolledtext.ScrolledText(tab6,width=48, height=38, font=(1))

        scr7_hex.place(x=0, y=0)

        scr8_hex.place(x=573, y=0)

button = tkinter.Button(tab6,text="确认", width=6, pady=1, command=hex1)

button.place(x = 495,y = 305)
#
#
#---------------------------------
#特殊ascii编码

book4 = tkinter.StringVar()

bookChosen4 = ttk.Combobox(tab7,width=9,textvariable=book4,)

bookChosen4['values'] = ('八进制','unicode中文','unicode英文数字')

bookChosen4.place(x = 475,y = 270)

bookChosen4.current(0)

bookChosen4.config(state='readonly')


def ascii1():
#八进制
    if bookChosen4.get() == '八进制':

        def ascii8_en():

            txt = scr1_hex.get('0.0', 'end')

            strip = txt.strip('\n')

            total = ''

            for i in strip:
                b = oct(ord(i))
                b = '\\' + str(b[2:])
                total += b

            scr2_hex.insert(END, total)

            scr2_hex.insert(END, '\n')

        def ascii8_de():

            txt = scr1_hex.get('0.0','end')

            strip = txt.strip('\n')

            scr2_hex.insert(END, strip.encode('ascii').decode('unicode_escape'))

            scr2_hex.insert(END, '\n')

        def empty():

            scr1_hex.delete('0.0', 'end')
            scr2_hex.delete('0.0', 'end')

        button = Button(tab7,text="编 码-->", width=6, height=2, command=ascii8_en)

        button.place(x=495, y=150)

        button = Button(tab7,text="解 码-->", width=6, height=2, command=ascii8_de)

        button.place(x=495, y=410)

        button = Button(tab7,text="一清\n键空", width=6, height=3, command=empty)

        button.place(x=495, y=550)

        scr1_hex = scrolledtext.ScrolledText(tab7,width=45, height=38, font=(1))

        scr2_hex = scrolledtext.ScrolledText(tab7,width=48, height=38, font=(1))

        scr1_hex.place(x=0, y=0)

        scr2_hex.place(x=573, y=0)

    if bookChosen4.get() == 'unicode中文':

        def asciiu_Z_en():

            txt = scr1_hex.get('0.0', 'end')

            strip = txt.strip('\n')

            scr2_hex.insert(END, strip.encode('unicode-escape').decode())

            scr2_hex.insert(END, '\n')

        def asciiu_Z_de():

            txt = scr1_hex.get('0.0','end')

            strip = txt.strip('\n')

            scr2_hex.insert(END, strip.encode('ascii').decode('unicode_escape'))

            scr2_hex.insert(END, '\n')

        def empty():

            scr1_hex.delete('0.0', 'end')
            scr2_hex.delete('0.0', 'end')

        button = Button(tab7,text="编 码-->", width=6, height=2, command=asciiu_Z_en)

        button.place(x=495, y=150)

        button = Button(tab7,text="解 码-->", width=6, height=2, command=asciiu_Z_de)

        button.place(x=495, y=410)

        button = Button(tab7,text="一清\n键空", width=6, height=3, command=empty)

        button.place(x=495, y=550)

        scr1_hex = scrolledtext.ScrolledText(tab7,width=45, height=38, font=(1))

        scr2_hex = scrolledtext.ScrolledText(tab7,width=48, height=38, font=(1))

        scr1_hex.place(x=0, y=0)

        scr2_hex.place(x=573, y=0)
    if bookChosen4.get() == 'unicode英文数字':

        def asciiu_E_en():

            txt = scr1_hex.get('0.0', 'end')

            strip = txt.strip('\n')

            total = ''

            for i in strip:

                e = base64.b16encode(i.encode('utf-8')).decode('ascii')

                total += '\\u00' + e

            scr2_hex.insert(END, total)

            scr2_hex.insert(END, '\n')

        def asciiu_E_de():

            txt = scr1_hex.get('0.0','end')

            strip = txt.strip('\n')

            scr2_hex.insert(END, strip.encode().decode('unicode_escape'))

            scr2_hex.insert(END, '\n')

        def empty():

            scr1_hex.delete('0.0', 'end')
            scr2_hex.delete('0.0', 'end')

        button = Button(tab7,text="编 码-->", width=6, height=2, command=asciiu_E_en)

        button.place(x=495, y=150)

        button = Button(tab7,text="解 码-->", width=6, height=2, command=asciiu_E_de)

        button.place(x=495, y=410)

        button = Button(tab7,text="一清\n键空", width=6, height=3, command=empty)

        button.place(x=495, y=550)

        scr1_hex = scrolledtext.ScrolledText(tab7,width=45, height=38, font=(1))

        scr2_hex = scrolledtext.ScrolledText(tab7,width=48, height=38, font=(1))

        scr1_hex.place(x=0, y=0)

        scr2_hex.place(x=573, y=0)


button = tkinter.Button(tab7,text="确认", width=6, pady=1, command=ascii1)
button.place(x = 495,y = 305)

# ---------------------
# 骚操作

ttk.Label(tab8, text="\n各种骚操作转换，鼠标点击可以直接打开哦。下面的位置是通随机数算出来的哦，有没有惊艳到（呕）",font=("宋体", 17)).pack()

def open_url1(event):
    webbrowser.open_new(r"https://www.toolmao.com/tool/juhuawen.htm")

def open_url2(event):
    webbrowser.open_new(r"http://huoxingwen.17ziti.com/")

def open_url3(event):
    webbrowser.open_new(r"http://www.keyfc.net/bbs/tools/tudoucode.aspx")

def open_url4(event):
    webbrowser.open_new(r"https://www.qqxiuzi.cn/bianma/wenbenjiami.php?s=huaduo")

def open_url5(event):
    webbrowser.open_new(r"https://www.qqxiuzi.cn/bianma/wenbenjiami.php?s=yinbiao")

def open_url6(event):
    webbrowser.open_new(r"https://www.qqxiuzi.cn/bianma/wenbenjiami.php?s=yiwen")

def open_url7(event):
    webbrowser.open_new(r"https://www.qqxiuzi.cn/bianma/wenbenjiami.php?s=yinyue")

def open_url8(event):
    webbrowser.open_new(r"https://www.qqxiuzi.cn/bianma/wenbenjiami.php?s=jiantou")

def open_url9(event):
    webbrowser.open_new(r"https://www.qqxiuzi.cn/bianma/wenbenjiami.php?s=mangwen")

link1 = Label(tab8, text="菊花文", fg="Cyan", cursor="hand2", font=('Arial', 40))
link1.place(x= 760, y= 222)

link2 = Label(tab8, text="火星文", fg="Cyan", cursor="hand2", font=('Arial', 40))
link2.place(x= 533, y= 185)

link3 = Label(tab8, text="与佛论禅", fg="Cyan", cursor="hand2", font=('Arial', 40))
link3.place(x= 783 ,y= 80)

link4 = Label(tab8, text="花朵符号", fg="Cyan", cursor="hand2", font=('Arial', 40))
link4.place(x= 509, y= 54)

link5 = Label(tab8, text="国际音标", fg="Cyan", cursor="hand2", font=('Arial', 40))
link5.place(x= 201, y= 87)

link6 = Label(tab8, text="彝文", fg="Cyan", cursor="hand2", font=('Arial', 40))
link6.place(x= 488, y= 120)

link7 = Label(tab8, text="音乐符号", fg="Cyan", cursor="hand2", font=('Arial', 40))
link7.place(x= 303 ,y= 230)

link8 = Label(tab8, text="箭头符号", fg="Cyan", cursor="hand2", font=('Arial', 40))
link8.place(x= 68, y= 225)

link9 = Label(tab8, text="盲文", fg="Cyan", cursor="hand2", font=('Arial', 40))
link9.place(x= 44 ,y= 64)

link1.bind("<Button-1>", open_url1)
link2.bind("<Button-1>", open_url2)
link3.bind("<Button-1>", open_url3)
link4.bind("<Button-1>", open_url4)
link5.bind("<Button-1>", open_url5)
link6.bind("<Button-1>", open_url6)
link7.bind("<Button-1>", open_url7)
link8.bind("<Button-1>", open_url8)
link9.bind("<Button-1>", open_url9)

ttk.Label(tab8, text="----------------------------------------------------------------------------------------------------------------------------------------------------").place(x=0,y=300)#刚好够一个不差
ttk.Label(tab8,text='编码/解码网站',font=("楷体", 17)).place(x=450,y=320)

# ---------------------
# 骚操作_编码/解码网站

def open_url10(event):
    webbrowser.open_new(r"http://ctf.ssleye.com/")

def open_url11(event):
    webbrowser.open_new(r"https://www.somd5.com/")

def open_url12(event):
    webbrowser.open_new(r"https://www.cmd5.com/")

def open_url13(event):
    webbrowser.open_new(r"https://www.sojson.com/")

def open_url14(event):
    webbrowser.open_new(r"http://tool.chinaz.com/map.aspx")

def open_url15(event):
    webbrowser.open_new(r"https://www.fujieace.com/jingyan/ascii.html")

def open_url16(event):
    webbrowser.open_new(r"https://regex101.com/")

def open_url17(event):
    webbrowser.open_new(r"https://www.box3.cn/tools/jwt.html")

def open_url18(event):
    webbrowser.open_new(r"https://jwt.io/")



link10 = Label(tab8, text="CTF在线工具", fg="Cyan", cursor="hand2", font=('Arial', 30))
link10.place(x= 111 ,y= 473)

link11 = Label(tab8, text="MD5免费在线解密", fg="Cyan", cursor="hand2", font=('Arial', 30))
link11.place(x= 700 ,y= 360)

link12 = Label(tab8, text="md5在线解密", fg="Cyan", cursor="hand2", font=('Arial', 30))
link12.place(x= 700, y= 585)

link13 = Label(tab8, text="JSON解析格式化", fg="Cyan", cursor="hand2", font=('Arial', 30))
link13.place(x= 600 ,y= 530)

link14 = Label(tab8, text="日常实用工具", fg="Cyan", cursor="hand2", font=('Arial', 30))
link14.place(x= 163 ,y= 554)

link15 = Label(tab8, text="ASCII码对照表", fg="Cyan", cursor="hand2", font=('Arial', 30))
link15.place(x= 382 ,y= 457)

link16 = Label(tab8, text="regex101", fg="Cyan", cursor="hand2", font=('Arial', 30))
link16.place(x= 143 ,y= 426)

link17 = Label(tab8, text="JWT 在线解密", fg="Cyan", cursor="hand2", font=('Arial', 30))
link17.place(x= 387 ,y= 376)

link18 = Label(tab8, text="JSON Web Tokens", fg="Cyan", cursor="hand2", font=('Arial', 30))
link18.place(x= 660, y= 454)


link10.bind("<Button-1>", open_url10)
link11.bind("<Button-1>", open_url11)
link12.bind("<Button-1>", open_url12)
link13.bind("<Button-1>", open_url13)
link14.bind("<Button-1>", open_url14)
link15.bind("<Button-1>", open_url15)
link16.bind("<Button-1>", open_url16)
link17.bind("<Button-1>", open_url17)
link18.bind("<Button-1>", open_url18)

# ---------------------
# 关于&日志
ttk.Label(tab9,text='作者：huayang',font=("楷体", 30)).pack()
ttk.Label(tab9,text='师傅们还有什么需要添加的编码或是建议记得在Github或是博客给我里留言哦\n',font=("楷体", 20)).pack()
ttk.Label(tab9,text='师傅们看我这么用心个Star✩不过分吧*ଘ(੭*ˊᵕˋ)੭* ੈ✩‧₊˚\n',font=("楷体", 20)).pack()
ttk.Label(tab9,text='本工具未来还会持续更新美化的，比如外观，功能，面向对象手法上\n',font=("楷体", 20)).pack()
ttk.Label(tab9,text='这只是我毕业设计项目的一个分类，未来还会有更多工具项目，请大家多多关照',font=("楷体", 20)).pack()

#event不能去掉
def open_url19(event):
    webbrowser.open_new(r"https://hellohy.top/")
link19 = Label(tab9, text="博客", fg="Cyan", cursor="hand2", font=('Arial', 30))
link19.place(x= 550 , y= 255)
link19.bind("<Button-1>", open_url19)
def open_url20(event):
    webbrowser.open_new(r"https://github.com/light-Life")
link20 = Label(tab9, text="Github", fg="Cyan", cursor="hand2", font=('Arial', 30))
link20.place(x= 380 , y= 255)
link20.bind("<Button-1>", open_url20)

ttk.Label(tab9, text="----------------------------------------------------------------------------------------------------------------------------------------------------").place(x=0,y=300)#刚好够一个不差
ttk.Label(tab9,text='更新日志',font=("楷体", 17)).place(x=470,y=320)

window.mainloop()#打开窗口并维持