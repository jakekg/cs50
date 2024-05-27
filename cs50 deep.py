Answer = input('What is the answer to the Great Question if Life, the Universe and Everything? ')

match Answer: 
    case '42' | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")