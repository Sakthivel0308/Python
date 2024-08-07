import random
import time

OPERATORS = ['+', '-', '*','//']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    exp = str(left) +" "+ operator +" "+ str(right)
    answer = eval(exp)
    return exp, answer

input("Press Enter to Start....")
print("------------------------")

start_time = time.time()


for i in range(TOTAL_PROBLEMS):
    exp, answer = generate_problem()
    while True:
        guess = input("Problem # "+str(i+1)+": "+ exp+ "= ")
        if guess == str(answer):
            break
end_time = time.time()

total_time = round(end_time - start_time)
print("Well done.You finished in ", total_time,"seconds!")
