# This basic program is a seconds converter: you enter with integer number and receive its larger time magnitude
                                                                        #values as for example: decades, days, hours.


def main():
    try:
        start = int(input(f'Please, enter with integer number for conversion: '))

        century = start // 3155760000  # -> seconds in one day (as SID) multiplied per 36525 ((365 * 10) + 25)
        decade = (start % 3155760000) // 315352800  # -> SID  multiplied per 3652 ((365 * 10) + 2)
        year = ((start % 3155760000) % 315352800) // 31536000  # -> SID  multiplied per 365
        month = (((start % 3155760000) % 315352800) % 31536000) // 2626560  # -> SID multiplied per 30.4 (365/12)
        week = ((((start % 3155760000) % 315352800) % 31536000) % 2626560) // 604800  # ->  SID multiplied per 7
        day = (((((start % 3155760000) % 315352800) % 31536000) % 2626560) % 604800) // 86400  # -> seconds in one hour * 24
        hour = ((((((start % 3155760000) % 315352800) % 31536000) % 2626560) % 604800) % 86400) // 3600  # -> 60 * 60
        minute = (((((((start % 3155760000) % 315352800) % 31536000) % 2626560) % 604800) % 86400) // 3600) // 60
        second = (((((((start % 3155760000) % 315352800) % 31536000) % 2626560) % 604800) % 86400) // 3600) % 60

        print("\nYour entry corresponds to...\n")
        print(century, "century(s),", decade, "decade(s),", year, "year(s),", month, "month(s),", week, "week(s),", day,
              "day(s),", hour, "hour(s),", minute, "minute(s) e", second, "second(s).")

    except ValueError:
        print('Could not run the code correctly. Did you enter an integer?')
    
    except Exception as error:
        print("An error occurred, please contact the developer.", error)


if __name__ == "__main__":
    main()
