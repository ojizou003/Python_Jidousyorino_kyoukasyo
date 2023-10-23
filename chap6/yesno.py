import tkinter as tk
import tkinter.messagebox as mb

tk.Tk().withdraw()
yesno = mb.askyesno("質問", "処理を実行しますか？")
if yesno:
    mb.showinfo("はいを選択", "処理を実行しました")
else:
    mb.showinfo("いいえを選択", "実行しませんでした")