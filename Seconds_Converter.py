# This basic program is a converter of seconds: you enter with integer number and receive its larger time magnitude
# values as for example: decades, days, hours, etc...


def main():
    try:
        start = int(input('Please, enter with integer number for conversion: '))
        # -> SID = Seconds In a Day = 60 * 60 * 24 = 86400
        century = start // 3155760000  # -> SID * 36525 (result of: (365 * 100) + 25)
        aux1 = start % 3155760000  # -> all 'aux' saves the remaining value of the previous calculation
        decade = aux1 // 315352800  # -> SID * 3652 (result of: (365 * 10) + 2)
        aux2 = aux1 % 315352800
        year = aux2 // 31536000  # -> SID * 365
        aux3 = aux2 % 31536000
        month = aux3 // 2626560  # -> SID * 30.4 (rounding 365/12)
        aux4 = aux3 % 2626560
        week = aux4 // 604800  # ->  SID * 7
        aux5 = aux4 % 604800
        day = aux5 // 86400  # -> SID
        aux6 = aux5 % 86400
        hour = aux6 // 3600  # -> 60 * 60
        aux7 = aux6 % 3600
        minute = aux7 // 60
        second = aux7 % 60

        print("\nYour entry corresponds to...\n")
        print(century, "century(s),", decade, "decade(s),", year, "year(s),", month, "month(s),", week, "week(s),", day,
              "day(s),", hour, "hour(s),", minute, "minute(s) e", second, "second(s).")

    except ValueError:
        print('Could not run the code correctly. Did you enter an integer?')
    
    except Exception as error:
        print("An error occurred, please contact the developer.", error)


if __name__ == "__main__":
    main()
