# Reinforcement Learning

In this problem, the goal is to train an AI that traverses an  n×n  grid to find paths that lead to the bottom right corner  (n−1,n−1) , from the top left corner, (0, 0). Assune  n=15 , and the terminal (end) states of the grid include the desired state  (14,14)  as well as areas with quicksand (death traps!). An agent gets a reward of 0 when it moves to a state that is not terminal, 1 when it moves to the desired state  (14,14) , and -1 when it moves into a quicksand. The game ends whenever the agent reaches a terminal state.

To run any RL, we need to specify a Markov Decision Process which is a tuple comprising of  S,A,P,R,γ . In this problem:

S  - denotes states, which are the grid coordinates, (x, y).
A  - denotes agent actions: will consider the following 1-step movement actions  (0−right,1−down,2−left,3−up) 
P  - denotes the transition matrix  P:S×A×S  which is the probability of going to state  s′ , from state  s , via action  a . We will consider a deterministic environment where  p(s,a,s′)=1  if it's possible to take action  a  from state  s  leading to state  s′ , otherwise its  0 
R  - the reward for the goal state,  (x=gridsize−1,y=gridsize−1)=1 . The reward for quicksand locations = -1, the reward for any other state = 0.
γ  - discount factor. Variable caters for preference of immediate rewards over long-term rewards. We will consider  γ=0.8 

Source: https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf

Source: https://en.wikipedia.org/wiki/Q-learning.
