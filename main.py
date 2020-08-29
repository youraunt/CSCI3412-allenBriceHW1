#
# I don't know what happened to this problem.
# It was on canvas for a small amount of time.
# I did it, so here it is.
#
# def homework1() -> object:
#     for i in range(-10, 12, 2):
#         print("Num:", i, i ** 2)
#
#
# if __name__ == "__main__":
#     print('Hello CSCI 3412 !!')
#     homework1()


"""
 @param x the number of iterations
 @param number_of_bulbs default argument
 @brief This functions iterates over a list of boolean light bulbs
 @param n number of times.
"""


def light_bulb_problem(x, number_of_bulbs=100):
    light_bulbs = [False] * number_of_bulbs  # initialize list with all elements false or off or zero
    for index in range(x):
        for step in range(index, number_of_bulbs, index + 1):
            light_bulbs[step] = not light_bulbs[step]
    return light_bulbs


if __name__ == "__main__":
    for i in range(10, 101, 30):
        print('On pass', i, 'there are %d light bulbs are switched on.' % light_bulb_problem(i).count(True))
