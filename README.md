# Random Playground

Random Playground is a repository for exercises of analysis and simulation of known problems on 
Randomness, Complexity, Dynamical Systems and Chaos Theory. Code is mainly written in Python. Algorithms may be original or "translated" from other sources/languages, when they were not already available in Python (at least for the best of my knowledge at the time). \
In the latter case, references to original sources are informed. \
Collaborations and discussions on the explored (and additional) topics are welcomed.

## General references

Complexity: A Guided Tour, from Melanie Mitchell \
https://www.amazon.com/Complexity-Guided-Tour-Melanie-Mitchell-dp-0199798109/dp/0199798109/ref=mt_other?_encoding=UTF8&me=&qid=1656600243

## Explored Topics

1. Monty Hall Problem \
The Monty Hall problem is a great example of how counter-intuitive Probability and Statistics may be. It is named after the presenter of a popular American TV show from the 60's, called "Let's Make a Deal". There was a regular sequence of the show where Monty Hall would present the participant to 3 closed doors, and give her/him the following challenge: \
"Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and I, the host, will open another door, say No. 3, which has a goat. After this you have the choice of continuing with door No. 1 or switch to the remaining door, in this example, No. 2. Is it to your advantage to switch your choice? Is it better to keep your initial pick? Is it indifferent?"\
The code here simulates a random door being chosen to hold the prize. Then a player who also randomly selects a door, and then the presenter selecting a door where he knows the prize is not placed. You can select the strategy of always switch the door picked by the player, or never switch from the initial pick. There is one test where you can compare the performance of the player for a large number of trials, both always switching and never switching. \
References: \
https://en.wikipedia.org/wiki/Monty_Hall_problem

2. Logistic Map \
References: \
https://en.wikipedia.org/wiki/Logistic_map

