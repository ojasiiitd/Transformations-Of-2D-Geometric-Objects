# Ojasva Saxena 
# 2018352
# IP : HW - 4

import tkinter
import matplotlib.pyplot as plt
import math

def matrixMult(l1 , l2) :
	r1 = len(l1)
	c1 = len(l1[0])
	r2 = len(l2)
	c2 = len(l2[0])
	product = []
	for i in range (r1) :
		rows = []
		for j in range(c2) :
			elt = 0
			for k in range(r2) :
				elt += (l1[i][k] * l2[k][j] )
			rows.append(elt)
		product.append(rows)
	return (product)

def updateGraph(poly) :
	plt.clf()
	plt.fill(poly[0],poly[1])
	plt.axis('equal')
	plt.show()

def scale(t , sx , sy) :
	mult = [ [sx, 0] , [0, sy] ]
	scaled = matrixMult(mult , t)
	for i in scaled :
		for j in i :
			j = round(j)
	return (scaled)

def rotate(t , fai) :
	fai = math.radians(fai)
	a00 = round(math.cos(fai))
	a01 = round((-math.sin(fai)))
	a10 = round(math.sin(fai))
	a11 = round(math.cos(fai))
	mult = [ [a00,a01] , [a10,a11] ]
	rotated = matrixMult(mult , t)
	for i in rotated :
		for j in i :
			j = round(j)
	return (rotated)

def translate(t , dx , dy) :
	mult = [ [1,0,dx] , [0,1,dy] , [0,0,1] ]
	t.append([1]*len(t[0]))
	translated = matrixMult(mult , t)
	translated.remove(t[2])
	for i in translated :
		for j in i :
			j = round(j)
	return (translated)

if __name__ == '__main__':
	
	shape = input()
	if shape.lower() == 'disc' :
		abr = [ float(i) for i in input().strip().split() ]
		a = abr[0]
		b = abr[1]
		r = abr[2]
		xcoors = []
		ycoors = []
		for i in range(10) :
			angle = math.radians((i*360) / 10)
			elt = r * round(math.cos(angle))
			coor = a + elt
			xcoors.append(coor)
			ycoors.append(coor)
		disc = [ xcoors , ycoors ]
		print(disc)

		updateGraph(disc)
		choice = [ str(i) for i in input().strip().split() ]
		while choice[0] != 'quit' :
			if choice[0] == 'S' :
				sx = float(choice[1])
				sy = float(choice[2])
				disc = scale(disc,sx,sy)
			elif choice[0] == 'R' :
				fai = float(choice[1])
				disc = rotate(disc,fai)
			elif choice[0] == 'T' :
				dx = float(choice[1])
				dy = float(choice[2])
				disc = translate(disc,dx,dy)

			for i in disc :
				for j in i :
					if j == int(j) :
						print(int(j),end=" ")
					else :
						print(j,end=" ")
				print()
			updateGraph(disc)
			choice = [ str(i) for i in input().strip().split() ]

	elif shape.lower() == 'polygon' :
		xcoors = [ float(i) for i in input().strip().split() ]
		ycoors = [ float(i) for i in input().strip().split() ]
		poly = [ xcoors , ycoors ]

		updateGraph(poly)
		choice = [ str(i) for i in input().strip().split() ]
		while choice[0] != 'quit' :
			if choice[0] == 'S' :
				sx = float(choice[1])
				sy = float(choice[2])
				poly = scale(poly,sx,sy)
			elif choice[0] == 'R' :
				fai = float(choice[1])
				poly = rotate(poly,fai)
			elif choice[0] == 'T' :
				dx = float(choice[1])
				dy = float(choice[2])
				poly = translate(poly,dx,dy)

			for i in poly :
				for j in i :
					if j == int(j) :
						print(int(j),end=" ")
					else :
						print(j,end=" ")
				print()
			updateGraph(poly)
			choice = [ str(i) for i in input().strip().split() ]