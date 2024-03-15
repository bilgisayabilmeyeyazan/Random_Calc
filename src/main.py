import random
import itertools


def random_equation_generator():
    number_of_operators = random.randint(2,4)
    operators = ["*", "-", "/", "+"]

    x = random.choices(range(1,101), k= number_of_operators+1)
    y = random.choices(operators, k = number_of_operators)
    y.append("=")
    random_equation = list(itertools.chain.from_iterable(zip(x, y)))
    return random_equation


def equation_calculator(equation):
    while "*" in equation or "/" in equation:
        operator_location = 0
        if "*" in equation and "/" in equation:
            if equation.index("*") < equation.index("/"):
                operator_location = equation.index("*")
                mid_result = equation[operator_location-1]*equation[operator_location+1]
            else:
                operator_location = equation.index("/")
                mid_result = equation[operator_location-1]/equation[operator_location+1]
        elif "*" in equation:
            operator_location = equation.index("*")
            mid_result = equation[operator_location-1]*equation[operator_location+1]
        else:
            operator_location = equation.index("/")
            mid_result = equation[operator_location-1]/equation[operator_location+1]

        del equation[operator_location-1:operator_location+2]
        equation.insert(operator_location-1, mid_result)

    while len(equation) > 3:
        if equation[1] == "+":
            mid_result2 = equation[0]+equation[2]
        else:
            mid_result2 = equation[0]-equation[2]

        del equation[0:3]
        equation.insert(0, mid_result2)

    return round(equation[0], 2)


def main():

    n = int(input("How many equations do you want? "))
    equations = ["2256321"]
    while n > 0:
        the_equation = random_equation_generator()
        the_equation_copy = the_equation.copy()
        the_result = equation_calculator(the_equation)
        the_equation_copy.append(the_result)
        the_equation_copy = "".join(list(map(str, the_equation_copy)))
        equations.append(the_equation_copy)
        n -= 1
    try:
        f = open("../result.txt", "w")
        f.write("\n".join(equations))
        f.close()

    except Exception as exceptObj:
        print("Error:", str(exceptObj))


if __name__ == '__main__':
    main()
