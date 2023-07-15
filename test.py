""" Sine Cosine OPtimization Algorithm """

import random
import numpy
import math
from solution import solution
import time

SearchAgents_no=3
i=1
ub,lb =-5,5
dim =2

if not isinstance(lb, list):
    lb = [lb] * dim
if not isinstance(ub, list):
    ub = [ub] * dim
Positions = numpy.zeros((SearchAgents_no, dim))
print(Positions)

Positions[:,i]=numpy.random.uniform(0, 1, SearchAgents_no) * (ub[i] - lb[i]) + lb[i]

print(Positions)