import random

def fitness(board):
    n = len(board)
    horizontal_collisions = sum([board.count(queen) - 1 for queen in board]) // 2
    diagonal_collisions = 0

    for i in range(n):
        for j in range(n):
            if i != j:
                dx = abs(i - j)
                dy = abs(board[i] - board[j])
                if dx == dy:
                    diagonal_collisions += 1

    return int(max_fitness - (horizontal_collisions + diagonal_collisions / 2))

def random_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def mutate(board):
    n = len(board)
    board[random.randint(0, n - 1)] = random.randint(0, n - 1)
    return board

def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(0, n - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

def genetic_algorithm(n, population_size=100, generations=1000):
    global max_fitness
    max_fitness = (n * (n - 1)) // 2
    population = [random_board(n) for _ in range(population_size)]

    for generation in range(generations):
        population = sorted(population, key=lambda board: fitness(board), reverse=True)
        if fitness(population[0]) == max_fitness:
            return population[0]

        next_generation = population[:2]
        for _ in range(population_size - 2):
            parent1, parent2 = random.choices(population[:50], k=2)
            child = crossover(parent1, parent2)
            if random.random() < 0.1:
                child = mutate(child)
            next_generation.append(child)

        population = next_generation

    return None

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    solution = genetic_algorithm(n)
    if solution:
        print("Solution found:", solution)
    else:
        print("No solution found.")