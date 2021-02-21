"""
Just a tester. Not relevant to the project.
"""

import tkinter as tk

from functions import *

import nltk

scary_words = ["at your own risk", 'we reserve the right to modify', 'replace the terms',
               'if your breach these terms', 'material breach', 'suspend the service',
               'sell your information', 'process your data', 'share your data', 'mercantile agent',
               'sole discretion', 'will be liable', 'distribute your data', 'automatically renewed',
               'excludes all liability', 'financial obligation']

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def analyze():
    """Analyze
    """
    terms = entry1.get()

    label3 = tk.Label(root, text='The Square Root of ' + terms + ' is:', font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)

    sentence_list = nltk.sent_tokenize(terms)

    freq_table = create_freq_table(terms)

    summary = ''
    summary += summary_generator(sentence_list, freq_table) + '\n' + '\n'

    summary += find_scary_phrases(sentence_list, scary_words)

    label4 = tk.Label(root, text=summary, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(text='Get the Square Root', command=analyze)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
