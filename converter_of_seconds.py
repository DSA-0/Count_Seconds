# This basic program is a converter of seconds: you enter with integer number and receive its larger time magnitude
# of values as for example: decades, days, hours, etc...

magnums = [[' century(s), ', 3155760000], [' decade(s), ', 315352800], [' year(s), ', 31536000],
           [' month(s), ', 2626560], [' week(s), ', 604800], [' day(s), ', 86400], [' hour(s), ', 3600],
           [' minute(s) and ', 60], [' second(s).']]  # -> List of time magnitude and yours respective seconds.


def total_mgm(num, list1):  # -> Function that calculates the magnitudes and constructs the answer.
    response = ''  # -> Here's the answer that will be constructed as per the calculations.
    mgm = num // list1[0][1]  # -> First calculation and your output, if there's.
    after = num % list1[0][1]
    if mgm > 0:
        response += str(mgm) + list1[0][1]
    for i in list1[1:8]:  # -> Others calculations and yours outputs, except the last.
        mgm = after // i[1]
        after = after % i[1]
        if mgm > 0:
            response += str(mgm) + i[0]
    response += str(after) + list1[8][0]  # -> Last output.
    print(f'Your enter corresponds to...\n{response}')


def main():
    try:
        start = int(input('Please, enter with integer number for conversion: '))
        total_mgm(start, magnums)
    except ValueError:  # -> Common error from entry.
        print('Could not run the code correctly. Did you enter an integer?')
    except Exception as error:  # -> Any others errors.
        print("An unexpected error occurred, please contact the developer.", error)


if __name__ == "__main__":
    main()
