def replace_x_with_y(name,x,y):
    return name.replace(x, y)

def main():
    name = input()
    name = replace_x_with_y(name,":)","🙂")
    name = replace_x_with_y(name,":(","🙁")
    print(name)

main()