# The keyword def introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters. 
# The statements that form the body of the function start at the next line, and must be indented.
def fib(n):
    """Print a fibonacci series up to n."""
    a,b =0,1
    while a < n:
        print(a,end=' ')
        a ,b =b,a+b
        print()
fib(2000)