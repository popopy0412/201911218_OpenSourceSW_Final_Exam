def m(i):
	n,sum = 4,0
	for i in range(1,i+1):
		sum += (((-1)**(i+1)) / (2*i-1))
	n*=sum
	return n


print("i\tm(i)\n")
for i in range(1, 902, 100):
	print(f"{i}\t{m(i):.4f}")