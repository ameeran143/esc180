import lab02_solutions



def sum_of_cubes(n):
    total = 0
    for i in range(n + 1):
        total += i ** 3

    return total


def check_sum(n):
    total = (n ** 2 * ((n + 1) ** 2)) / 4

    if total == sum_of_cubes(n):
        return True
    else:
        return False


def libniz_formula(n):
    total = 0
    for i in range(n):
        total += ((-1)**i)/(2*i + 1)

    print(4*total)



if __name__ == '__main__':
    lab02_solutions.initialize()
    lab02_solutions.add(42)

    if lab02_solutions.current_value == 42:
      print("Test 1 passed")
    else:
      print("Test 1 failed")