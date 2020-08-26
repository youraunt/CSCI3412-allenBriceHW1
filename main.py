# for i in range(1, 101):
#     if i ** 0.5 % 1:
#         state = 'on'
#     else:
#         state = 'off'
#     print("Bulb {}:{}".format(i, state))

# for i in range(1, 11):
#     print("Bulb %s is on" % i ** 2)
#
# lightBulbs = [False] * 100
# for i in range(100):
#     for j in range(i, 10, i + 1):
#         lightBulbs[j] = not lightBulbs[j]
#     print("Bulb %d:" % (i + 1), 'open' if lightBulbs[i] else 'close')

# bulbs = [0] * 100
# for x in range(1, 101):
#     for y in range(x - 1, 100, x):
#         if bulbs[y] == 0:
#             bulbs[y] = 1
#         elif bulbs[y] == 1:
#             bulbs[y] = 0
# switchedOn = []
# for i, value in enumerate(bulbs):
#     if value == 1:
#         switchedOn.append(i + 1)
# print('these bulbs are on: ', switchedOn)


"""
 @param n the number of iterations
 @param number_of_bulbs default argument
 @brief This functions iterates over a list of boolean light bulbs
 @param n number of times.
"""


def light_bulb_problem(n, number_of_bulbs=100):
    bulbs = [False] * number_of_bulbs  # initialize list with all elements false or off
    for index in range(n):
        for step in range(index, number_of_bulbs, index + 1):
            bulbs[step] = not bulbs[step]
    return bulbs


if __name__ == "__main__":
    for i in range(10, 101, 30):
        print('On pass', i, 'there are %d light bulbs are switched on.' % light_bulb_problem(i).count(True))
