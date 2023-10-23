import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd

tk.Tk().withdraw() # tkinterの窓を表示しない
filepath = fd.askopenfilename(
    filetypes=[('Pythonファイル','*.py')],
    initialdir='./'
)
mb.showinfo('対象ファイル', filepath)