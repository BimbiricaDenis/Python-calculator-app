import tkinter as tk

app = tk.Tk()
app.title("Calculatoru python")
app.resizable(False, False)

icon = tk.PhotoImage(file="calculator-icon.png")
app.iconphoto(True, icon)

color_somon="#FF91A4"
color_black="#000000"
color_white="#FFFFFF"
color_turqoise="#40E0D0"

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]
row_count = len(button_values)
column_count = len(button_values[0])

frame = tk.Frame(app)
label = tk.Label(frame, text="0", font=("Arial", 45), fg=color_white, bg=color_black, anchor="e",width=column_count)


label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for col in range(column_count):
        value=button_values[row][col]
        button=tk.Button(frame, text=value, font=("Arial", 30), width=column_count-1, height=1, 
                             command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.configure(fg=color_white, bg=color_turqoise)
        elif value in right_symbols:
            button.configure(fg=color_white, bg=color_somon)
        else:
            button.configure(fg=color_white, bg=color_black)
        button.grid(row=row+1, column=col)

frame.pack()

A = "0"
B = None
operator = None

def clear():
    global A, B, operator
    A = "0"
    B = None
    operator = None

def remove_zero(num):
    if num % 1 == 0:
        num = int(num)
    return num

def button_clicked(value):
    global A, B, operator, right_symbols, top_symbols, label

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = round(remove_zero(numA + numB),3)
                elif operator == "-":
                    label["text"] = round(remove_zero(numA - numB),3)
                elif operator == "×":
                    label["text"] = round(remove_zero(numA * numB),3)
                elif operator == "÷":
                    if numB == 0:
                        label["text"] = "Error"
                    else:
                     label["text"] = round(remove_zero(numA / numB),3)

                clear()
                

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

            operator = value

    elif value in top_symbols:
        if value == "AC":
            clear()
            label["text"] = "0"

        elif value == "+/-" and label["text"] != "0":
            result = float(label["text"]) * -1
            label["text"] = remove_zero(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero(result)
    else:        
     if value == ".":
        if "." not in label["text"]:
            label["text"] += "."
            
     elif value in "0123456789":
        if label["text"] == "0":
            label["text"] = value
        else: 
            label["text"] += value

     elif value == "√":
        if(float(label["text"]) < 0):
            label["text"] = "Error"
        result = float(label["text"]) ** 0.5
        label["text"] = round(remove_zero(result),7)
    

app.update()
app_width = app.winfo_width()
app_height = app.winfo_height()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 3) - (app_width // 2)
y = (app_height // 2)
app.geometry(f"{app_width}x{app_height}+{x}+{y}")


app.mainloop()