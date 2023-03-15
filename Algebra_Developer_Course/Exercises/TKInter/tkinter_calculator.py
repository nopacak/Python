import tkinter as tk

def handle_btn_sum():
    txt_entry_result.delete(0, tk.END)

    first_number = int(txt_entry_first_number.get())
    second_number = int(txt_entry_second_number.get())

    result = first_number + second_number
    txt_entry_result.insert(tk.END, str(result))


def handle_btn_subtract(event):
    txt_entry_result.delete(0, tk.END)

    first_number = int(txt_entry_first_number.get())
    second_number = int(txt_entry_second_number.get())

    result = first_number - second_number
    txt_entry_result.insert(tk.END, str(result))

root = tk.Tk()
root.title("Algebra")
root.geometry("600x400")

lbl_first_number = tk.Label(root, text = "First number: ")
lbl_first_number.grid(row=0, column=0, padx=5, pady=5)
txt_entry_first_number = tk.Entry()
txt_entry_first_number.grid(row=0, column=1, padx=5, pady=5)

lbl_second_number = tk.Label(root, text = "Second number: ")
lbl_second_number.grid(row=1, column=0, padx=5, pady=5)
txt_entry_second_number = tk.Entry()
txt_entry_second_number.grid(row=1, column=1, padx=5, pady=5)

btn_sum = tk.Button(root, text = "Sum", command=handle_btn_sum)
btn_sum.grid(row=2, column=0, padx=5, pady=5)
btn_subtract = tk.Button(root, text = "Subtract")
btn_subtract.grid(row=2, column=1, padx=5, pady=5)
btn_subtract.bind("<Button-1>", handle_btn_subtract)

lbl_result = tk.Label(root, text = "Result: ")
lbl_result.grid(row=3, column=0, padx=5, pady=5)
txt_entry_result = tk.Entry()
txt_entry_result.grid(row=3, column=1, padx=5, pady=5)

root.mainloop() 
