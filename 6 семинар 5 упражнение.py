import tkinter as tk
import random

def create_ball(event):
    x = event.x
    y = event.y
    radius = 20
    color = random.choice(['cyan', 'darkblue', 'darkcyan', 'darkgray', 'darkkhaki', 'darkolivegreen', 'darkorchid', 'darksalmon', 'darkslateblue', 'darkturqueise', 'deeppink', 'dimgray', 'firebrick', 'forestgreen', 'ghostwhite', 'gold', 'gray', 'greenyellow', 'hotpink', 'indigo', 'khaki', 'lavenderblush', 'lemonchiffon', 'lightcoral', 'lightgoldenrodyellow', 'lightgrey', 'lightsalmon', 'lightskyblue', 'lightsteelblue', 'lime', 'linen', 'maroon', 'mediumblue', 'mediumslateblue', 'mediumpurple', 'mediumturquose', 'midnightblue', 'mistyrose', 'navajowhite', 'oldlace', 'olivedrab', 'orangered', 'palegoldenrod', 'paleturquoise', 'papayawhip', 'peru', 'plum', 'purple', 'rosybrown', 'saddlebrown', 'sandybrown', 'seashell', 'silver', 'slateblue', 'snow', 'steelblue', 'teal', 'tomato', 'violet', 'white', 'yellow', 'aquamarine','red', 'green', 'blue', 'yellow', 'purple', 'orange','aliceblue', 'antiquewhite', 'aqua', 'chartreuse', 'azure', 'beige', 'bisque', 'cornsilk', 'blanchedalmond', 'blue', 'blueviolet', 'darkgoldenrod', 'darkgreen', 'darkmagenta', 'darkorange', 'darkred', 'darkseagreen', 'darkslategray', 'darkviolet', 'deepskyblue', 'dodgerblue', 'floralwhite', 'fuchsia', 'gainsboro', 'goldenrod', 'green', 'honeydew', 'indianred', 'ivory', 'lavender', 'lawngreen', 'lightblue', 'lightcyan', 'lightgreen', 'lightpink', 'lightseagreen', 'lightslategray', 'lightyellow', 'limegreen', 'mediumaquamarine', 'mediumseagreen', 'mediumorchid', 'mediumspringgreen', 'mediumvioletred', 'mintcream', 'moccasin', 'navy', 'olive', 'orange', 'orchid', 'palegreen', 'palevioletred', 'peachpuff', 'pink', 'powderblue', 'red', 'royalblue', 'salmon', 'seagreen', 'sienna', 'skyblue', 'slategray', 'springgreen', 'tan', 'thistle', 'turquoise', 'wheat', 'whitesmoke', 'yellowgreen', 'brown', 'burlywood', 'cadetblue', 'coral', 'chocolate', 'cornflowerblue', 'black', 'crimson'])

    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline='')

root = tk.Tk()
root.title("Создание шариков")

canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()

canvas.bind("<Button-1>", create_ball)

root.mainloop()