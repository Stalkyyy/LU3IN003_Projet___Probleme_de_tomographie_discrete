GRAY = 0
BLACK = 1
WHITE = 2

def creationMemo(M : int, k : int) :
    return [[None for _ in range(k + 1)] for _ in range(M)]