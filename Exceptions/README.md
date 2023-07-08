        EXCEPTIONS
        ----------

WHAT
---

- In Python Programming, exceptions are events that occur during the execution of a program.
- These events Usually disrupt the normal flow of instructions
- When such events occur, Python raises an exception allowing you to take appropriate actions thus handling the error gracefully

EXAMPLES
-------

Exception Handling
------------------

        try:
            # Code that may raise an exception
            result = 10 / 0  # This will raise a ZeroDivisionError
        except ZeroDivisionError:
            print("Error: Division by zero")
        except Exception as e:
            print("Error:", str(e))


Raising an Exception
--------------------

        def divide(a, b):
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return a / b

        try:
            result = divide(10, 0)  # This will raise a ValueError
        except ValueError as e:
            print("Error:", str(e))


Handling Multiple Exceptions
----------------------------

        try:
            # Code that may raise exceptions
            file = open("nonexistent_file.txt", "r")
            result = 10 / 0
        except FileNotFoundError:
            print("Error: File not found")
        except ZeroDivisionError:
            print("Error: Division by zero")
        except Exception as e:
            print("Error:", str(e))


Raising Custom Exceptions
-------------------------

        class MyCustomException(Exception):
            pass

        def check_value(value):
            if value < 0:
                raise MyCustomException("Value cannot be negative")

        try:
            check_value(-10)  # This will raise MyCustomException
        except MyCustomException as e:
            print("Error:", str(e))


------------------------------------

These examples demonstrate various aspects of exception handling, such as catching specific types of exceptions, handling multiple exceptions, and creating and raising custom exceptions.


