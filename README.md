# evalution_algorithm_222
• Problem: Find the number in the range {0,1,...,255} with the maximum number of 2’s in it. • Obvious solution: 222

This is begginer problem to test genetics algorithm on practice 

• Population: Set of solutions
• Fitness: Quality of a solution
• Chromosome: Representation for a solution (e.g., set of
parameters)
• Gene:Part of the representation of a solution (e.g.,
parameter or degree of freedom)
• Growth: Decoding of the representation of solutions
• Crossover and mutation: Search operators
• Natural selection: Reuse of good (sub-)solutions

Algorithm:

1. Initialise and evaluate fitness of population
Repeat until quality of solution “sufficiently good”:
2. Select sub-population for reproduction (Selection)
3. Recombine the “genes” of selected parents
(Recombination or Crossover, XO)
4. Mutate the mated population randomly (Mutation)
5. Evaluate the fitness of the new population
6. Select the survivors from the actual fitness
