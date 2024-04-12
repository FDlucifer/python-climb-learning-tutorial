import random

POPULATION_SIZE = 100
GENOME_LENGHTH = 20
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7
GENERATIONS = 200


def random_genome(length):
    return [random.randint(0, 1) for _ in range(length)]


def init_population(population_size, genome_length):
    return [random_genome(genome_length) for _ in range(population_size)]


def fitness(genome):
    return sum(genome)


def select_parent(population, fitness_values):
    total_fitness = sum(fitness_values)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fitness_value in zip(population, fitness_values):
        current += fitness_value
        if current > pick:
            return individual


def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, len(parent1))
        return (
            parent1[:crossover_point] + parent2[crossover_point:],
            parent2[:crossover_point] + parent1[crossover_point:],
        )
    else:
        return parent1, parent2


def mutate(genome):
    for i in range(len(genome)):
        if random.random() < MUTATION_RATE:
            genome[i] = abs(genome[i] - 1)
    return genome


def genetic_algorithm():
    population = init_population(POPULATION_SIZE, GENOME_LENGHTH)

    for generation in range(GENERATIONS):
        fitness_values = [fitness(genome) for genome in population]

        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1 = select_parent(population, fitness_values)
            parent2 = select_parent(population, fitness_values)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutate(offspring1), mutate(offspring2)])

        population = new_population

        fitness_values = [fitness(genome) for genome in population]
        best_fitness = max(fitness_values)
        print(f"generation {generation}: best fitness = {best_fitness}")

    best_index = fitness_values.index(max(fitness_values))
    best_solution = population[best_index]
    print(f"best solution: {best_solution}")
    print(f"best fitness: {fitness(best_solution)}")


if __name__ == "__main__":
    genetic_algorithm()
