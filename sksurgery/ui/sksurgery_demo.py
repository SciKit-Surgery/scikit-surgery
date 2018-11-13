# coding=utf-8

"""Hello world demo module"""
import six


def run_demo(console, text):
    """Show message with or without console"""

    six.print_(text)

    if not console:
        from tkinter import Tk, Label

        root = Tk()

        label = Label(root, text=text)
        label.pack()

        root.mainloop()

    return True
