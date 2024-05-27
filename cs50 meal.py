def main():
    time = input('What time is it? ').strip()
    hours = convert(time)
    
    if 7 <= hours <= 8:
        print('breakfast time')
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")
    # No need for an else block as we don't want to output anything if it's not meal time

def convert(time):
    if 'a.m.' in time or 'p.m.' in time:
        time, period = time.split()
        hours, minutes = map(int, time.split(':'))
        if period == 'p.m.' and hours != 12:
            hours += 12
        elif period == 'a.m.' and hours == 12:
            hours = 0
    else:
        hours, minutes = map(int, time.split(':'))
    
    return hours + minutes / 60

if __name__ == "__main__":
    main()