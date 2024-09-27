
# This is your unique solution file

from config import *
from lib204 import semantic_interface

# Assignment for 21SLR15

# Note: All of these answers are almost certainly wrong

a2q12 = [ [s1], [s2], [s3], [s4] ]

a2q13 = {
    P: True,
    Q: False,
    R: True,
    S: False,
    T: True
}

a2s5nnf = [
    [(~((Q&P)|R)>>(~Q|R)), 'starting formula'],
]

a2s6nnf = [
    [(~(R|Q)>>~(P|~R)), 'starting formula'],
]

a2s5cnf = [
    [(~((Q&P)|R)>>(~Q|R)), 'starting formula'],
]

a2s6cnf = [
    [(~(R|Q)>>~(P|~R)), 'starting formula'],
]

a2s5tseitin = semantic_interface.Encoding()
# Fill in the Tseitin steps and finalize
x1 = a2s5tseitin.tseitin(P | Q, 'x1') # just an example
a2s5tseitin.finalize(x1) # make sure you update the variable!

a2s6tseitin = semantic_interface.Encoding()
# Fill in the Tseitin steps and finalize
x1 = a2s6tseitin.tseitin(P | Q, 'x1') # just an example
a2s6tseitin.finalize(x1) # make sure you update the variable!
