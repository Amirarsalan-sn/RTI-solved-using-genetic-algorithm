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
max_iteration = 10 * cn.clauses_size
max_answer = cn.clauses_size


def fitness(cnf_valuation):
    global cn

    return cn.count_number_of_satisfactions(cnf_valuation)


class Member:
    def __init__(self, gene):
        self.gene = gene
        self.fitness = fitness(gene)


def choose_parent(generation_list):
    global top_membership_percent
    global mu

    top_gen_num = int(lmda * top_membership_percent)
    bottom_gen_num = lmda - top_gen_num
    parent_list = [generation_list[i] for i in range(mu - top_gen_num, mu)]
    for i in range(bottom_gen_num):
        random_index = random.randint(0, mu - top_gen_num - 1)
        parent_list.append(generation_list[random_index])

    return parent_list


def mutate(child):
    global mutation_percent
    global cn

    possibility = random.random()
    if possibility <= mutation_percent:
        random_index = random.randint(0, cn.nv - 1)
        child[random_index] ^= 1


def cross_over(parent1, parent2):
    global cn

    random_index = random.randint(0, cn.nv)
    left_gene = [parent1[i] for i in range(random_index)]
    right_gene = [parent2[i] for i in range(random_index, cn.nv)]
    left_gene.append(right_gene)
    child = left_gene
    mutate(child)

    return child


def update_generation(parent_list, generation_list: list):
    global lmda
    global top_membership_percent
    global mu

    for i in range(lmda):
        parent1 = parent_list[i]
        for j in range(lmda):
            if i == j:
                continue
            parent2 = parent_list[j]
            child = cross_over(parent1, parent2)
            generation_list.append(child)

    generation_list.sort(key=lambda x: x.fitness)
    top_gen_num = int(mu * top_membership_percent)
    bottom_gen_num = mu - top_gen_num
    new_generation = [generation_list[i] for i in range(mu - top_gen_num, mu)]
    for i in range(bottom_gen_num):
        random_index = random.randint(0, mu - top_gen_num - 1)
        new_generation.append(generation_list[random_index])

    return new_generation


generation = [Member(np.random.choice([0, 1], size=cn.nv)) for i in range(mu)]
generation.sort(key=lambda x: x.fitness)
parent = []
children = []
