import sys

def main():
	if len(sys.argv) != 3 or (not sys.argv[1].isdigit() or not sys.argv[2].isdigit()):
		print("Usage: python operations.py <number1> <number2>")	
		print("Example:")
		print("   python operations.py 10 3")
		return
	n1 = int(sys.argv[1])
	n2 = int(sys.argv[2])
	print("Sum: {}".format(n1 + n2))
	print("Difference: {}".format(n1 - n2))
	print("Product: {}".format(n1 * n2))
	if n2 == 0:
		print("Quotient ERROR (div by zero)")
		print("Remainder: ERROR(modulo by zero)")	
		return
	print("Quotient {}".format(float(n1) / float(n2)))
	print("Remainder: {}".format(float(n1) % float(n2)))

if __name__ == "__main__":
	main()