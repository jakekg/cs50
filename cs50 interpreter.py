def main():
    expression = input('What math equation would you like to solve? ').strip()
    x, y, z = expression.split()
    x = int(x)
    z = int(z)
    
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z
    else:
        print("Invalid operator")
        return
    
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()