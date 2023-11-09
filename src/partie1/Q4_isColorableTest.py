from Q4_isColorable import isColorable

# Cas tirés de la page 1 de l'énoncé
assert isColorable(4, 1, [3])
assert isColorable(4, 0, [])
assert isColorable(4, 3, [1,1,1])
assert isColorable(4, 1, [3])
assert isColorable(3, 2, [1,1])
assert isColorable(3, 1, [1])
assert isColorable(3, 2, [1,2])
assert isColorable(3, 1, [1])
assert isColorable(3, 1, [2])


assert not isColorable(14, 2, [10,5])
assert isColorable(4, 1, [5])
assert not isColorable(5, 3, [1,2,3])
assert isColorable(15, 3, [1,2,11])

assert isColorable(14, 1, [10,5])
assert isColorable(5,2,[1,2,3])