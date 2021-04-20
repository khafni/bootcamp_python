def fib(limit):
      
    # Initialize first two Fibonacci Numbers 
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b

for n in fib(5):
    print(n)

def generator(text, sep=" ", option=None):
    