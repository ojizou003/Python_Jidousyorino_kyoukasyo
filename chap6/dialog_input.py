import tkinter as tk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd

tk.Tk().withdraw() # tkinterの窓を表示しない
name = sd.askstring(
    '名前入力', 'お名前は？',
    initialvalue='お名前を入力してください'
)
mb.showinfo('挨拶', f'こんにちは！ {name}さん！！')