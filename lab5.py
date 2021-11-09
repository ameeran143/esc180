# Problem 1
def list1_starts_with_list2(list1, list2):
    if len(list1) >= len(list2):
        for i in range(len(list2)):
            if list2[i] != list1[i]:
                return False
                break

        return True

    if len(list2) >= len(list1):
        return False


# Question 2
def match_pattern(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    if set1.issubset(set2) or set2.issubset(set1):
        return True
    else:
        return False


# Question 3
def repeats(list):
    start = 1
    end = len(list) - 2
    for i in range(len(list)-1):
        if list[i+1] == list[i]:
            return True

    return False


# Question 4 a
def print_matrix_dim(m):
    rows = len(m)
    columns = len(m[0])
    print("[", rows, ", ", columns, "]")


# Question 4 b
def mult_M_v(M, v):
    resultant = [[0],[0]]
    for i in range(len(M) - 1):
        for x in range(len(M[0]) - 1):
            resultant[i] += M[i][x] * v[i]

    print_matrix_dim(resultant)
    return resultant



if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [1, 2, 3, 4]
    list0 = [1,2,3,4,5,5,6,7,8]
    list4 = [1,2,2,3,4]

    if list1_starts_with_list2(list1, list2):
        print("problem 2 works")

    if repeats(list4):
        print("problem 3 works")

    else:
        print("no")

    mat = [[1, 2], [3, 4], [5, 6]]
    print_matrix_dim(mat)

    mult = [[2], [2]]

    mult_M_v(mat, mult)
