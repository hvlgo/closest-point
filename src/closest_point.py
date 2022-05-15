from math import sqrt
import random
import time
import sys

points = []
INF = 1000_000_000
NUM = 5000
distance = lambda m, n : sqrt((m[0] - n[0]) ** 2 + (m[1] - n[1]) ** 2)
judge = lambda d, median, point : point[0] >= median - d and point[0]  <= median + d

def generate():
    global NUM, points
    for i in range(NUM):
        points.append((random.randint(0, NUM * 100), random.randint(0, NUM * 100)))

def qsort(array, l, r, flag):
    if r - l <= 20:
        for i in range(l + 1, r + 1):
            if array[i][flag] < array[i - 1][flag]:
                auxiliary = array[i]
                j = i - 1
                while j >= l and array[j][flag] > auxiliary[flag]:
                    array[j + 1] = array[j]
                    j -= 1
                array[j + 1] = auxiliary
        return 
    x = l
    y = r
    k = array[l]
    while True:
        while l < r and array[r][flag] > k[flag]:
            r -= 1
        if l < r:
            array[l] = array[r]
            l += 1
        while l < r and array[l][flag] <= k[flag]:
            l += 1
        if l < r:
            array[r] = array[l]
            r -= 1
        if l >= r:
            break
    array[l] = k
    qsort(array, x, l - 1, flag)
    qsort(array, l + 1, y, flag)
    return 


def naive_closest_point():
    global points
    if len(points) == 0:
        raise ValueError("the point array must not be empty")
    if len(points) == 1:
        return ValueError("the point array must not be just one element")
    min_val = distance(points[0], points[1])
    min_points = [0, 1]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            tmp = distance(points[i], points[j])
            if tmp < min_val:
                min_val = tmp
                min_points[0] = i
                min_points[1] = j
    return (min_val, points[min_points[0]], points[min_points[1]])

def closest_point(l, r):
    global points
    if r - l < 50:
        qsort(points, l, r, 1)
        min_val = distance(points[l], points[l + 1])
        min_points = [l, l + 1]
        for i in range(l, r + 1):
            for j in range(i + 1, r + 1):
                tmp = distance(points[i], points[j])
                if tmp < min_val:
                    min_val = tmp
                    min_points[0] = i
                    min_points[1] = j
        return (min_val, points[min_points[0]], points[min_points[1]])
    k = (l + r) // 2
    median = points[k][0]
    closest = ()
    closest_1 = closest_point(l, k)
    closest_2 = closest_point(k + 1, r)
    closest = closest_1 if closest_1[0] < closest_2[0] else closest_2

    points_y = []
    m = l
    n = k + 1
    while m <= k and n <= r:
        if points[m][1] <= points[n][1] and m <= k:
            points_y.append(points[m])
            m += 1
        elif points[m][1] > points[n][1] and n <= r:
            points_y.append(points[n])
            n += 1
    if m <= k:
        for i in range(m, k + 1):
            points_y.append(points[i])
    if n <= r:
        for i in range(n, r + 1):
                points_y.append(points[i])
        
    filter_points_y = []
    for i in range(l, r + 1):
        points[i] = points_y[i - l]
        if judge(closest[0], median, points[i]):
            filter_points_y.append(points[i])
    
    for i in range(len(filter_points_y)):
        for j in range(5):
            if i + j + 1 < len(filter_points_y):
                tmp = distance(filter_points_y[i], filter_points_y[i + j + 1])
                if tmp < closest[0]:
                    closest = (tmp, filter_points_y[i], filter_points_y[i + j + 1])
    return closest

def divide_closest_point():
    global points
    points = list(set(points))
    qsort(points, 0, len(points) - 1, 0)
    answer = closest_point(0, len(points) - 1)
    return answer

def main():
    global points, NUM
    if len(sys.argv) == 2:
        NUM = int(sys.argv[1])
    print(f"n = {NUM}")
    generate()
    answer_1 = naive_closest_point()
    answer_2 = divide_closest_point()
    print(answer_1)
    print(answer_2)

if __name__ == "__main__":
    main()
