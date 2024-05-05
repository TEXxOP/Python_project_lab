import random
import math
import time

def display_intro():
    """Display the intro message"""
    title = "** Welcome to the Math Challenge **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))

def display_menu():
    """Display the menu options"""
    print("\nChoose a topic:")
    print("1. Basic Arithmetic")
    print("2. Area and Volume")
    print("3. Trigonometry and Identities")
    print("4. Calculus")
    print("5. Exit")

def get_user_input():
    """Get user input and validate it"""
    while True:
        try:
            user_input = int(input("Enter your choice: "))
            if 1 <= user_input <= 5:
                return user_input
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_user_solution(problem, time_limit, player):
    """Get user solution and validate it"""
    print(f"Player {player}, enter your answer")
    print(problem, end="")
    start_time = time.time()
    result = float(input(" = "))
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time > time_limit:
        print("Time's up!")
        return None
    return result

def check_solution(user_solution, solution, count):
    """Check if the user solution is correct"""
    if user_solution == solution:
        count += 1
        print("Correct!")
    else:
        print("Incorrect.")
    return count

def basic_arithmetic():
    """Generate a basic arithmetic problem"""
    operations = ['+', '-', '*', '/']
    number_one = random.randrange(10, 1000) 
    number_two = random.randrange(10, 1000)
    operation = random.choice(operations)
    time_limit = 10

    if operation == '+':
        problem = f"{number_one} + {number_two} = "
        solution = number_one + number_two
    elif operation == '-':
        problem = f"{number_one} - {number_two} = "
        solution = number_one - number_two
    elif operation == '*':
        problem = f"{number_one} * {number_two} = "
        solution = number_one * number_two
    elif operation == '/':
        while number_two == 0 or number_one % number_two!= 0: 
            number_two = random.randrange(1, 10)
        problem = f"{number_one} / {number_two} = "
        solution = number_one / number_two  # Changed from integer division to floating-point division

    return problem, solution

def area_volume():
    """Generate an area and volume problem"""
    shapes = ['circle', 'square', 'rectangle', 'cube', 'sphere']
    shape = random.choice(shapes)
    time_limit = 15 

    if shape == 'circle':
       radius = random.randrange(5, 25)
       problem = f"Area of a circle with radius {radius} = "
       solution = round(math.pi * radius**2, 2)
    elif shape == 'square':
      side = random.randrange(5, 25)
      problem = f"Area of a square with side {side} = "
      solution = side ** 2
    elif shape == 'rectangle':
      length = random.randrange(5, 25)
      width = random.randrange(5, 25)
      problem = f"Area of a rectangle with length {length} and width {width} = "
      solution = length * width
    elif shape == 'cube':
      side = random.randrange(5, 25)
      problem = f"Volume of a cube with side {side} = "
      solution = side ** 3
    elif shape == 'sphere':
     radius = random.randrange(5, 25)
     problem = f"Volume of a sphere with radius {radius} = "
     solution = round((4/3) * math.pi * radius**3, 2)

    return problem, solution

def trigonometry_identities():
    """Generate a trigonometry and identities problem"""
    functions = ['sin', 'cos', 'tan']
    operation = random.choice(functions)
    angles = ['0', '30', '45', '60', '90', '120', '135', '150', '180']
    angle = random.choice(angles)
    time_limit = 15

    if operation == 'sin':
      problem = f"sin({angle}) = "
      solution = round(math.sin(math.radians(int(angle))), 2)
    elif operation == 'cos':
      problem = f"cos({angle}) = "
      solution = round(math.cos(math.radians(int(angle))), 2)
    elif operation == 'tan':
      if int(angle) == 0 or int(angle) == 180:
        print("Infinite. Please try again.")
        return None
      else:
        problem = f"tan({angle}) = "
        solution = round(math.tan(math.radians(int(angle))), 2)
    elif operation == 'cot':
      if int(angle) == 0 or int(angle) == 180:
        print("Infinite. Please try again.")
        return None
      else:
        problem = f"cot({angle}) = "
        solution = round(1/math.tan(math.radians(int(angle))), 2)
    elif operation == 'sec':
      problem = f"sec({angle}) = "
      solution = round(1/math.cos(math.radians(int(angle))), 2)
    elif operation == 'cosec':
      problem = f"cosec({angle}) = "
      solution = round(1/math.sin(math.radians(int(angle))), 2)

    return problem, solution

def calculus():
    """Generate a calculus problem"""
    operations = ['integral', 'derivative']
    operation = random.choice(operations)
    functions = ['x^2', 'x^3', 'sin(x)', 'cos(x)', 'e^x', 'ln(x)']
    function = random.choice(functions)
    limits = ['0', '1', '2', '3', '4', '5', '10', '15', '20']
    limit = random.choice(limits)
    time_limit = 20

    if operation == 'integral':
      problem = f"Integral of {function} with respect to x from 0 to {limit} = "
      if function == 'x^2':
        solution = round((1/3) * (limit**3), 2)
      elif function == 'x^3':
        solution = round((1/4) * (limit**4), 2)
      elif function == 'sin(x)':
        solution = round(-math.cos(limit), 2)
      elif function == 'cos(x)':
        solution = round(math.sin(limit), 2)
      elif function == 'e^x':
        solution = round((1/2) * (math.e**(limit**2)), 2)
      elif function == 'ln(x)':
        solution = round((x * math.log(x) - x), 2)
    elif operation == 'derivative':
      problem = f"Derivative of {function} with respect to x = "
      if function == 'x^2':
        solution = 2 * x
      elif function == 'x^3':
        solution = 3 * x**2
      elif function == 'sin(x)':
        solution = math.cos(x)
      elif function == 'cos(x)':
        solution = -math.sin(x)
      elif function == 'e^x':
        solution = math.e**x
      elif function == 'ln(x)':
        solution = 1/x

    return problem, solution

def game():
    """Play the math game"""
    player_one_count = 0
    player_two_count = 0
    rounds = 0
    time_limit = 20

    while rounds < 10:
        problem_type = random.randrange(1, 5)

        if problem_type == 1:
            problem, solution = basic_arithmetic()
        elif problem_type == 2:
            problem, solution = area_volume()
        elif problem_type == 3:
            problem, solution = trigonometry_identities()
        elif problem_type == 4:
            problem, solution = calculus()

        # Use get_user_solution for player input and validation
        player_one_solution = get_user_solution(problem, time_limit, "1")
        player_two_solution = get_user_solution(problem, time_limit, "2")

        if problem_type!= 4:
            if abs(player_one_solution - solution) < 0.01:
                player_one_count += 1
            elif abs(player_two_solution - solution) < 0.01:
                player_two_count += 1
            else:
                print(f"Incorrect answer. The correct answer is {solution}.")
        else:
            if operation == 'integral':
                if abs(player_one_solution - solution) < 0.01:
                    player_one_count += 1
                elif abs(player_two_solution - solution) < 0.01:
                    player_two_count += 1
                else:
                    print(f"Incorrect answer. The correct answer is {solution}.")
            elif operation == 'derivative':
                if abs(player_one_solution - solution) < 0.01:
                    player_one_count += 1
                elif abs(player_two_solution - solution) < 0.01:
                    player_two_count += 1
                else:
                    print(f"Incorrect answer. The correct answer is {solution}.")

        rounds += 1

    print("\nGame over.")
    print(f"Player 1 score: {player_one_count}")
    print(f"Player 2 score: {player_two_count}")

    if player_one_count > player_two_count:
        print("Player 1 wins.")
    elif player_one_count < player_two_count:
        print("Player 2 wins.")
    else:
        print("It's a tie.")

display_intro()
while True:
    display_menu()
    user_choice = get_user_input()
    if user_choice == 5:
        break
    else:
        game()
