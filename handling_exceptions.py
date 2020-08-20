def handle_exception():
    while True:
        try:
            number = int(input("What's your favorite number?\n"))
            print(20/number)
            break
        except ValueError:
            print("Make sure and enter a number")
        except ZeroDivisionError:
            print("Don't pick Zero")
        finally:
            print("Executed no matter what exception happen, either error or no error")


handle_exception()
