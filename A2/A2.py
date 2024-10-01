
from config import *
from lib204 import semantic_interface

# Assignment for 21SLR15


a2q12 = [ [s1], [s2, s3], [s4] ]

a2q13 = {
    P: True,
    Q: False,
    R: True,
    S: False,
    T: True
}

a2s5nnf = [
    [(~((Q&P)|R)>>(~Q|R)), 'starting formula'],
    [(~(~((Q&P)|R))|(~Q|R)), 'material implication'],
    [(((Q&P)|R)|(~Q|R)), 'double negation'],
]

a2s6nnf = [
    [(~(R|Q)>>~(P|~R)), 'starting formula'],
    [((~R&~Q)>>(~P&~~R)), 'de Morgans'], 
    [((~R&~Q)>>(~P&R)), 'double negation'],
    [((~(~R&~Q))|(~P&R)), 'material implication'],
    [((~~R|~~Q)|(~P&R)), 'de Morgans'],
    [((R|Q)|(~P&R)), 'double negation']
]

a2s5cnf = [
    [(~((Q&P)|R)>>(~Q|R)), 'starting formula'],
     [(~(~((Q&P)|R))|(~Q|R)), 'material implication'],
    [(((Q&P)|R)|(~Q|R)), 'double negation'],
    [((Q|R)&(P|R)&(~Q|R)), 'distribution']
]


a2s6cnf = [
    [(~(R|Q)>>~(P|~R)), 'starting formula'],
    [((~R&~Q)>>(~P&~~R)), 'de Morgans'], 
    [((~R&~Q)>>(~P&R)), 'double negation'],
    [((~(~R&~Q))|(~P&R)), 'material implication'],
    [((~~R|~~Q)|(~P&R)), 'de Morgans'],
    [((R|Q)|(~P&R)), 'double negation']
]

a2s5tseitin = semantic_interface.Encoding()
x1 = a2s5tseitin.tseitin(Q & P, 'x1')
x2 = a2s5tseitin.tseitin(x1 | R, 'x2')
x3 = a2s5tseitin.tseitin(~x2, 'x3')
x4 = a2s5tseitin.tseitin(~Q | R, 'x4')
a2s5tseitin.finalize(x4) 

a2s6tseitin = semantic_interface.Encoding()
x1 = a2s6tseitin.tseitin(R | Q, 'x1') 
x2 = a2s6tseitin.tseitin(~x1, 'x2')
x3 = a2s6tseitin.tseitin(P | ~R, 'x3')
x4 = a2s6tseitin.tseitin(~x3, 'x4')
a2s6tseitin.finalize(x4) 
