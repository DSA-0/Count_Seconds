# This basic program is a converter of seconds: you enter with integer number and receive its larger time magnitude
# of values as for example: decades, days, hours, etc...

magnums = [[' century(s), ', 3155760000], [' decade(s), ', 315352800], [' year(s), ', 31536000],
          [' month(s), ', 2626560], [' week(s), ', 604800], [' day(s), ', 86400], [' hour(s), ', 3600],
          [' minute(s) and ', 60], [' second(s).']]  # -> List of time magnitude and yours respective seconds.

response = ''  # -> Here is the answer that will be constructed as per the calculations.


def t_magnum(num, i_list0, i_list1):  # -> Function that calculates the magnitudes and constructs the answer.
    global response
    magnum = num // i_list1
    rest = num % i_list1
    if magnum > 0:
        response += str(magnum) + i_list0
    return rest


def multi_magnum(num):  # -> Function that structures previous function calls and outputs the response. 
    global response
    n = t_magnum(num, magnums[0][0], magnums[0][1])
    for i in magnums[1:8]:
        n = t_magnum(n, i[0], i[1])
    response += str(n) + magnums[8][0]
    print(f'Your enter corresponds to...\n{response}')


def main():
    try:
        start = int(input('Please, enter with integer number for conversion: '))
        multi_magnum(start)
    except ValueError:  # -> Common error from entry.
        print('Could not run the code correctly. Did you enter an integer?')
    except Exception as error:  # -> Any others errors.
        print("An unexpected error occurred, please contact the developer.", error)


if __name__ == "__main__":
    main()
