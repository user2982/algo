ALGORITHM: 
1. Randomized QuickSelect is an in-place algorithm that works by selecting a random pivot element from 
the list and partitioning the elements into two groups - those less than the pivot and those greater than 
the pivot. 
2. The algorithm then recursively focuses on the group containing the desired k-th element until the element 
is found.
--------------------------------------------------------------------------------------------------------------
PROGRAM:
import random
import math

def calculate_total_distance(order, distance_matrix):
    total_distance = 0
    num_cities = len(order)
    for i in range(num_cities - 1):
        total_distance += distance_matrix[order[i]][order[i + 1]]
    total_distance += distance_matrix[order[-1]][order[0]]
    return total_distance

def randomized_tsp(distance_matrix, max_iterations):
    num_cities = len(distance_matrix)
    
    current_solution = list(range(num_cities))
    random.shuffle(current_solution) 
    
    current_distance = calculate_total_distance(current_solution, distance_matrix)

    for iteration in range(max_iterations):
        new_solution = list(current_solution) 

        city1, city2 = random.sample(range(num_cities), 2)
        
        new_solution[city1], new_solution[city2] = new_solution[city2], new_solution[city1]
        
        new_distance = calculate_total_distance(new_solution, distance_matrix)
        
        if new_distance < current_distance:
            current_distance = new_distance
            current_solution = new_solution
        elif random.random() < math.exp((current_distance - new_distance) / (iteration + 1)):
            current_distance = new_distance
            current_solution = new_solution
            
    return current_solution, current_distance

if __name__ == "__main__":
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    max_iterations = 10000

    result_order, result_distance = randomized_tsp(distance_matrix, max_iterations)

    print("Optimal Tour Order:", result_order)
    print("Optimal Tour Distance:", result_distance)
