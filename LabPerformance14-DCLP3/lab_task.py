import random

class Individual:
    def __init__(self,k,T):
        self.k=k
        self.T=T
        self.genes=[random.randint(0, 9) for _ in range(k)]
        self.fitness=self.calc_fitness()

    def calc_fitness(self):
        return abs(sum(self.genes)-self.T)

    def mutate(self):
        index = random.randint(0,self.k - 1)
        if random.random()<0.5:
            self.genes[index]=max(0,self.genes[index]-1)
        else:
            self.genes[index]=min(9,self.genes[index]+1)
        self.fitness=self.calc_fitness()

class Population:
    def __init__(self,size,k,T):
        self.individuals=[Individual(k,T) for _ in range(size)]
        self.k=k
        self.T=T

    def get_fittest(self):
        return min(self.individuals,key=lambda ind: ind.fitness)

    def select_parents(self):
        sorted_individuals=sorted(self.individuals, key=lambda ind: ind.fitness)
        return sorted_individuals[0],sorted_individuals[1]

    def crossover(self, parent1, parent2):
        child=Individual(self.k, self.T)
        midpoint=random.randint(1, self.k - 1)
        child.genes=parent1.genes[:midpoint] + parent2.genes[midpoint:]
        child.fitness=child.calc_fitness()
        return child

    def evolve(self):
        parent1, parent2=self.select_parents()
        child=self.crossover(parent1, parent2)
        if random.random() < 0.7:
            child.mutate()
            
        worst=max(self.individuals, key=lambda ind: ind.fitness)
        self.individuals.remove(worst)
        self.individuals.append(child)

def solve(T,k):
    population=Population(size=50,k=k,T=T)
    generation =0
    while population.get_fittest().fitness != 0:
        generation += 1
        if generation%50 ==0:
            print(f"Generation {generation} best sum: {sum(population.get_fittest().genes)} genes: {population.get_fittest().genes}")
        population.evolve()

    result = population.get_fittest().genes
    print(f"✅ Solution found:")
    print(' '.join(map(str, result)))



print("Case#1")
solve(7, 2)  

print("\nCase#2")
solve(10, 3) 
