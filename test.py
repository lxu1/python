print(1)
import sys

def print_testcase(expected_value, actual_value):
    print('expected_value:{}, actual value: {}'.format(expected_value,actual_value))

return_value = print_testcase(42,32)

def readable_timedelta(days):
    return '{} week(s) and {} day(s).'.format(days//7, days%7)
    # print('{} week(s) and {} days.'.format(days/7, days%7))

print(readable_timedelta(10))
print(readable_timedelta(5062))


how_many_snakes = 2
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Philip and Charlie
"""


print(snake_string * how_many_snakes)
