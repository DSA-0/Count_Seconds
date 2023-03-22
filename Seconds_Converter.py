# This basic program is a converter of seconds: you enter with integer number and receive its larger time magnitude
# of values as for example: decades, days, hours, etc...


def main():
    try:
        start = int(input('Please, enter with integer number for conversion: '))
        response = ''
        # -> SID = Seconds In a Day = 60 * 60 * 24 = 86400
        century = start // 3155760000  # -> SID * 36525 (result of: (365 * 100) + 25)
        if century > 0:
            response += str(century) + ' century(s), '
        aux1 = start % 3155760000  # -> all 'aux' saves the remaining value of the previous calculation
        decade = aux1 // 315352800  # -> SID * 3652 (result of: (365 * 10) + 2)
        if decade > 0:
            response += str(decade) + ' decade(s), '
        aux2 = aux1 % 315352800
        year = aux2 // 31536000  # -> SID * 365
        if year > 0:
            response += str(year) + ' year(s), '
        aux3 = aux2 % 31536000
        month = aux3 // 2626560  # -> SID * 30.4 (rounding 365/12)
        if month > 0:
            response += str(month) + ' month(s), '
        aux4 = aux3 % 2626560
        week = aux4 // 604800  # ->  SID * 7
        if week > 0:
            response += str(week) + ' week(s), '
        aux5 = aux4 % 604800
        day = aux5 // 86400  # -> SID
        if day > 0:
            response += str(day) + ' day(s), '
        aux6 = aux5 % 86400
        hour = aux6 // 3600  # -> 60 * 60
        if hour > 0:
            response += str(hour) + ' hour(s), '
        aux7 = aux6 % 3600
        minute = aux7 // 60
        response += str(minute) + ' minute(s) and '
        second = aux7 % 60
        response += str(second) + ' second(s).'
        print(f'Your entry corresponds to...\n{response}')

    except ValueError:
        print('Could not run the code correctly. Did you enter an integer?')
    
    except Exception as error:
        print("An error occurred, please contact the developer.", error)


if __name__ == "__main__":
    main()
