
import graphics as gr
import tkinter as tk

window = gr.GraphWin("Fractal Rectangle", 1000, 1000)

k = 0.1

def fractal_rectangle(A, B, C, D, depth=400):
	if (depth < 1):
		return
	for M, N in [(A, B), (B, C), (C, D), (D, A)]:
		gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
	A1 = (A[0] * (1 - k) + B[0] * k, A[1] * (1 - k) + B[1] * k)
	B1 = (B[0] * (1 - k) + C[0] * k, B[1] * (1 - k) + C[1] * k)
	C1 = (C[0] * (1 - k) + D[0] * k, C[1] * (1 - k) + D[1] * k)
	D1 = (D[0] * (1 - k) + A[0] * k, D[1] * (1 - k) + A[1] * k)
	fractal_rectangle(A1, B1, C1, D1, depth - 1)

fractal_rectangle((100, 100), (900, 100), (900, 900), (100, 900))
tk.mainloop()