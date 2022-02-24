# automaton
### First LFA Lab
Exercise 1. Implement a library/program in a programming language of your
choosing to load and validate the following input file:
```
#
# comment lines ( skip them )
#
Sigma :
    word1
    word2
    ...
End
#
# comment lines ( skip them )
#
States :
    state1
    state2
    state3 ,F
    ...
    stateK , S
    ...
End
#
# comment lines ( skip them )
#
Transitions :
    stateX, wordY , stateZ
    stateX, wordY , stateZ
    ...
End
```

Sections can be in any order. By validation we ask to check that transition
section has valid states (first and third word) and valid words (word two). Note
that states can be succeeded by ”F”, ”S”, both or nothing. ”S” symbol can
succeed only one state.

Exercise 2. Familiarize yourself with Python Notebooks if python is your language of choice.

Exercise 3. Familiarize yourself with Latex (overleaf.com).
