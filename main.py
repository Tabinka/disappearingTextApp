from tkinter import *

main = Tk()
main.resizable(width=False, height=False)
main.config(bg="#2d3436")
main.title("Disappearing text App")

stop_writing_id = 'after'  # store id of the scheduled call to traduire
main_text = Label(main, text="Start typing and text will disappear after a few seconds...", fg="#dfe6e9", font=("Helvetica", 18), pady=20, padx=20, bg="#2d3436")
main_text.grid(row=0, column=0)
entry = Text(main, wrap=WORD, relief=FLAT, padx=14, pady=15, fg="#dfe6e9", font=("Helvetica", 14))
entry.grid(row=1, column=0)
entry.configure({"background": "#2d3436"})
entry.focus()


def wipe_text():
    entry.delete('1.0', END)


def stop_writing(event):
    global stop_writing_id
    main.after_cancel(stop_writing_id)  # cancel previous scheduling of traduire
    stop_writing_id = main.after(6000, wipe_text)  # wait 1s and execute traduire


entry.bind('<KeyRelease>', stop_writing)

main.mainloop()
