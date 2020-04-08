# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:25:36 2020

@author: Shivamm
"""

import json
from logpy import Relation, facts, run, conde, var, eq

# Check if 'x' is the parent of 'y'
def parent(x, y):
    return conde([father(x, y)], [mother(x, y)])

# Check if 'x' is the grandparent of 'y'
def grandparent(x, y):
    temp = var()
    return conde((parent(x, temp), parent(temp, y)))

# Check for sibling relationship between 'a' and 'b'  
def sibling(x, y):
    temp = var()
    return conde((parent(temp, x), parent(temp, y)))

# Check if x is y's uncle
def uncle(x, y):
    temp = var()
    return conde((father(temp, x), grandparent(temp, y)))

if __name__=='__main__':
    father = Relation()
    mother = Relation()
    

    facts(father,('watson','Tom'),('watson','Harry'),('watson','Robert'),
         ('Tom','jakson'),('Tom','Amelia'),('Harry','Mia'),('Harry','Ava'),('Harry','Camila'),
	 ('Harry','Luna'),('Harry','Anna'),('Harry','Maya'))
    facts(mother,('Alexa','Tom'),('Alexa','Harry'),('Alexa','Robert'),
         ('Sadie','Amelia'),('Sadie','Jakson'),('Clara','Ava'),('Clara','Camila'),('Clara','Luna'),
	 ('Clara','Anna'),('Clara','Maya'))


    x = var()

    # Watson's children
    name = 'Watson'
    output = run(0, x, father(name, x))
    print("\nList of " + name + "'s children:")
    for item in output:
        print(item)

    # Tom's mother
    name = 'Tom'
    output = run(0, x, mother(x, name))[0]
    print("\n" + name + "'s mother:\n" + output)

    # Robert's parents 
    name = 'Robert'
    output = run(0, x, parent(x, name))
    print("\nList of " + name + "'s parents:")
    for item in output:
        print(item)

    # Mia's grandparents 
    name = 'Mia'
    output = run(0, x, grandparent(x, name))
    print("\nList of " + name + "'s grandparents:")
    for item in output:
        print(item)

    # Alexa's grandchildren 
    name = 'Alexa'
    output = run(0, x, grandparent(name, x))
    print("\nList of " + name + "'s grandchildren:")
    for item in output:
        print(item)

    # Harry's siblings 
    name = 'Harry'
    output = run(0, x, sibling(x, name))
    siblings = [x for x in output if x != name]
    print("\nList of " + name + "'s siblings:")
    for item in siblings:
        print(item)

    # Ava's uncles
    name = 'Ava'
    name_father = run(0, x, father(x, name))[0]
    output = run(0, x, uncle(x, name))
    output = [x for x in output if x != name_father]
    print("\nList of " + name + "'s uncles:")
    for item in output:
        print(item)

    # All spouses
    a, b, c = var(), var(), var()
    output = run(0, (a, b), (father, a, c), (mother, b, c))
    print("\nList of all spouses:")
    for item in output:
        print('Husband:', item[0], '<==> Wife:', item[1])
