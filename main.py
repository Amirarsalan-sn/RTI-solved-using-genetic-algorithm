import numpy as np
from CnfResolver import CnfResolver
import math
import random

cn = CnfResolver("input.cnf")
# number of current generation
mu = 2 * cn.nv
# number of selected parent
lmda = int(math.sqrt(mu))
mutation_percent = 0.05
top_membership_percent = 0.75
bottom_membership_percent = 1 - top_membership_percent


def fitness(cnf_valuation):
    global cn

    return cn.count_number_of_satisfactions(cnf_valuation)


class Member:
    def __init__(self, gene):
        self.gene = gene
        self.fitness = fitness(gene)


def choose_parent(parent_list, generation_list):
    parent_list.clear()
    

generation = [Member(np.random.choice([0, 1], size=cn.nv)) for i in range(mu)]
generation.sort(key=lambda x: x.fitness)
parent = []
children = []
