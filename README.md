# Simple String Finder Genetic Algorithm
This is a simple genetic algorithm that finds a randomly generated string.

#### Quick Note Before We Start
Please not that this repository is NOT designed to be a tutorial of any kind. Despite my efforts to make it easy to use, it does require 
a basic knowledge of how a genetic algorithm works to use this code.

## Getting Started
1. Open the Algorithm.py file in your favorite python IDE
2. Run the module
3. In the interpreter where the module was just run, use the Algorithm() function to run the genetic algorithm

#### A Note On Variable Naming
Variable names adhere to common python practices of separating words by underscores. Method names start each word with a capital letter with 
the rest lower case and words are separated by underscores. Variable names are all lower case and words are separated by underscores.

## Algorithm()
The algorithm function has 2 required parameters and 4 additional optional parameters.
### Required Parameters
  #### pop_size
  This is the first of the required parameters and represents how many individual chromosomes are in the population. It should be an
  integer greater than 0.
  #### chrom_size
  The second of the required parameters, chrom_size determines the length of each chromosome, or string, in the population. It also
  determines the length of the "answer." The chrom_size parameter should be an integer greater than 0.
### Optional Parameters
  #### mutation_rate
  mutation_rate is the first of the optional parameters. It can be a float or an integer between 0 and 100 inclusive. The defualt value for
  this parameter is 100. The mutation_rate parameter represents a percentage of each population that gets mutated each generation.
  #### graded_retain_percent
  This is the second optional parameter that determines a percentage of the previous population that is retained to the next generation. 
  graded_retain_percent takes its individuals from the highest scoring of the population. It should be float between 0 and 1 inclusive with 
  the default value being 0.3. 
  #### nongraded_retain_percent
  The third optional parameter, nongraded_retain_percent, also determines how much of the previous population is retained to the next
  generation. This parameter chooses a random set of indivuals from the ones not chosen by graded_retain_percent. Like
  graded_retain_percent, it should be a float between 0 and 1 inclusive. It defaults to 0.2.
  #### mutation_amount
  This is the fourth optional parameter. It determines how much variation is included with each mutation. For instance, given a
  mutation_amount of 1, each chromosome chosen to mutate will have 1 character changed to a random character. The value of mutation_amount
  should be an integer ranging from 1 to chrom_size. The default value is 1.

## Run_Multiple()
  Run_Multiple() is an alternative way to run the Algorithm() function. It purely runs the function a specified number of times. This amount
  is determined by the first parameter in Run_Multiple(). All other parameters get directly passed to Algorithm(). The variable "times"
  should be an integer greater than 1.
