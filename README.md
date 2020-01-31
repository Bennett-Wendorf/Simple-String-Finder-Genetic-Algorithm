# Simple String Finder Genetic Algorithm
This is a simple genetic algorithm that finds a randomly generated string.

#### Quick Note Before We Start
Please not that this repository is NOT designed to be a tutorial of any kind. Despite my efforts to make it easy to use, it does require a basic knowledge of how a genetic algorithm works to use this code.

## Getting Started
1. Open the Algorithm.py file in your favorite python IDE
2. Run the module
3. In the interpreter where the module was just run, use the Algorithm() function to run the genetic algorithm

## Algorithm()
The algorithm function has 2 required parameters and 4 additional optional parameters.
### Required Parameters
  #### popSize
  This is the first of the required parameters and represents how many individual chromosomes are in the population. It should be an
  integer greater than 0.
  #### chromSize
  The second of the required parameters, chromSize determines the length of each chromosome, or string, in the population. It also
  determines the length of the "answer." The chromSize parameter should be an integer greater than 0.
### Optional Parameters
  #### mutationRate
  mutationRate is the first of the optional parameters. It can be a float or an integer between 0 and 100 inclusive. The defualt value for
  this parameter is 100. The mutationRate parameter represents a percentage of each population that gets mutated each generation.
  #### GRADED_RETAIN_PERCENT
  This is the second optional parameter that determines a percentage of the previous population that is retained to the next generation. 
  GRADED_RETAIN_PERCENT takes its individuals from the highest scoring of the population. It should be float between 0 and 1 inclusive with 
  the default value being 0.3. 
  #### NONGRADED_RETAIN_PERCENT
  The third optional parameter, NONGRADED_RETAIN_PERCENT, also determines how much of the previous population is retained to the next
  generation. This parameter chooses a random set of indivuals from the ones not chosen by GRADED_RETAIN_PERCENT. Like
  GRADED_RETAIN_PERCENT, it should be a float between 0 and 1 inclusive. It defaults to 0.2.
  #### mutationAmount
  This is the fourth optional parameter. It determines how much variation is included with each mutation. For instance, given a
  mutationAmount of 1, each chromosome chosen to mutate will have 1 character changed to a random character. The value of mutationAmount
  should be an integer ranging from 1 to chromSize. The default value is 1.

## RunMultiple()
  RunMultiple is an alternative way to run the Algorithm() function. It purely runs the function a specified number of times. This amount
  is determined by the first parameter in RunMultiple(). All other parameters get directly passed to Algorithm(). The variable "times"
  should be an integer greater than 1.
