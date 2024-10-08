print('Hello World!')


# Try/except with else block
try:
    val = 10/1
    str = 'Hello'
    num = int(input('Enter a number: '))
    print(str[num])
except ZeroDivisionError as e:
    print('Error:', e)
except IndexError:
    print('Error: Input index is out of range.')
else:
    print('No error occurred.')


# Try/except with finally block
try:
    val = 10/1
    str = 'Hello'
    num = int(input('Enter a number: '))
    print(str[num])
except ZeroDivisionError as e:
    print('Error:', e)
except IndexError:
    print('Error: Input index is out of range.')
else:
    print('No error occurred.')
finally:
    print('Finally block executed.')


# Try/except with raise block
try:
    val = 10/0
    if val == 0:
        raise ZeroDivisionError('Raise ZeroDivisionError')
except ZeroDivisionError as e:
    print('Error:', e)


# Try/except with assert block
try:
    val = 10/0
    assert val != 0, 'Value is zero'
except AssertionError as e:
    print('Error:', e)

# Try/except with custom exception
class MyException:
    def __init__(self, message):
        self.message = message

try:
    val = 10/0
    if val == 0:
        raise MyException('Value is zero')
except MyException as e:
    print('Error:', e.message)


print('Goodbye World!')