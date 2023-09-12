# from math import *
import random
import funcion
# isMale = True


# text = {"text": "Hola"}

# text1 = dict(text)

# print(text1)
# print(not isMale)

# number = -3
# print(type(str(number)))

# print(sqrt(4))

# print(f"{isMale} your momo haha" f"{isMale}")

lucky_numbers = [42, 833, 135, 1111, 11112, 16, 1, 23, 42]
friend = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "TuVieja"]
# friend.extend(lucky_numbers)
# friend.append("Creed")
# friend.insert(1, "Perro")
# friend.remove("Kevin")
# friend.clear()
# friend.pop()


# print(friend.index("Kevin"))
# print(friend.count("Jim"))
# friend.sort()
# lucky_numbers.sort()
# lucky_numbers.reverse()

# lucky_numbers2 = lucky_numbers.copy()
# print(lucky_numbers2, lucky_numbers, lucky_numbers == lucky_numbers2)


# coordinates = (4, 5) #tuplas
# coordinates = 10
# print(coordinates[0])


# def sayHi():
#     print("hello world!")
#     print("perro humano!")


# sayHi()


# for index in range(4, 11):
#     print(index)
# print([i for i in range(20) if i % 2 == 0])


# employee = open("employees.txt", "a")

# employee.write("amazing\n")

# print(employee.read())
# employee.close()

# print(random.randint(0, 10))
# print(funcion.amazing_tools(2))

def run(question):
    score = 0
    answer = input("Your answer: ")
    if answer == question:
        score += 1
        return print(f"tu score es {score}")


run("perro")
