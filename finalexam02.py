class Point:
	x = 0
	y = 0
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def distance(self, other):
		try:
			n = ((self.x - other.x)**2 + (self.y - other.y)**2)**(1/2)
			return n
		except:
			print("Error!")
		return None

	def __add__(self, other):
		try:
			p = Point(self.x+other.x, self.y+other.y)
			return p
		except:
			print("Error!")
		return None
	
	def __repr__(self):
		return f"({self.x}, {self.y})"

def main():
	p1 = Point(1, 1)
	p2 = Point(2, 2)
	print(f"distance : {p1.distance(p2)}")
	print(f"p1 + p2 = {p1+p2}")


if __name__ == "__main__":
	main()