# get weight from user input
# ask if the weight is in lbs or kg (case insensitive input)
# return weight in other unit of measure

def main():
    weight = int(input('Weight: '))
    units = input('(K)g or (L)bs: ')
    if units.lower() == 'k':
        weight = round(weight * 2.20462, 1) 
        print(f'Weight in Lbs: {weight}')
    elif units.lower() == 'l':
        weight = round(weight * 0.453592, 1)
        print(f'Weight in kg: {weight}')


if __name__ == '__main__':
    main()