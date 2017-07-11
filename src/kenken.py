import csp
import re
import sys
import time


def kenken_constraint(A, a, B, b):
    if B in neighbors[A] and a == b:
        return False

    for n in neighbors[A]:
        if n in game_kenken.infer_assignment() and game_kenken.infer_assignment()[n] == a:
            return False

    for n in neighbors[B]:
        if n in game_kenken.infer_assignment() and game_kenken.infer_assignment()[n] == b:
            return False

    for i in range(len(blockVariables)):
        if A in blockVariables[i]:
            blockA = i
        if B in blockVariables[i]:
            blockB = i

    if blockA == blockB:
        blockNum = blockA
        if blockOp[blockNum] == "''":
            if A != B:
                return False
            elif a != b:
                return False
            elif a != blockValue[blockNum]:
                return False

            return True

        elif blockOp[blockNum] == 'add':
            sum = assigned = 0

            for v in blockVariables[blockNum]:
                if v == A:
                    sum += a
                    assigned += 1
                elif v == B:
                    sum += b
                    assigned += 1
                elif v in game_kenken.infer_assignment():
                    sum += game_kenken.infer_assignment()[v]
                    assigned += 1

            if sum == blockValue[blockNum] and assigned == len(blockVariables[blockNum]):
                return True
            elif sum < blockValue[blockNum] and assigned < len(blockVariables[blockNum]):
                return True
            else:
                return False

        elif blockOp[blockNum] == 'mult':
            sum = 1
            assigned = 0

            for v in blockVariables[blockNum]:
                if v == A:
                    sum *= a
                    assigned += 1
                elif v == B:
                    sum *= b
                    assigned += 1
                elif v in game_kenken.infer_assignment():
                    sum *= game_kenken.infer_assignment()[v]
                    assigned += 1

            if sum == blockValue[blockNum] and assigned == len(blockVariables[blockNum]):
                return True
            elif sum <= blockValue[blockNum] and assigned < len(blockVariables[blockNum]):
                return True
            else:
                return False

        elif blockOp[blockNum] == 'div':
            return max(a, b) / min(a, b) == blockValue[blockNum]

        elif blockOp[blockNum] == 'sub':
            return max(a, b) - min(a, b) == blockValue[blockNum]

    else:
        constraintA = kenken_constraint_op(A, a, blockA)
        constraintB = kenken_constraint_op(B, b, blockB)

        return constraintA and constraintB

		
def kenken_constraint_op(var, val, blockNum):
    if blockOp[blockNum] == "''":
        return val == blockValue[blockNum]

    elif blockOp[blockNum] == 'add':
        sum2 = 0
        assigned2 = 0

        for v in blockVariables[blockNum]:
            if v == var:
                sum2 += val
                assigned2 += 1
            elif v in game_kenken.infer_assignment():
                sum2 += game_kenken.infer_assignment()[v]
                assigned2 += 1

        if sum2 == blockValue[blockNum] and assigned2 == len(blockVariables[blockNum]):
            return True
        elif sum2 < blockValue[blockNum] and assigned2 < len(blockVariables[blockNum]):
            return True
        else:
            return False

    elif blockOp[blockNum] == 'mult':
        sum2 = 1
        assigned2 = 0

        for v in blockVariables[blockNum]:
            if v == var:
                sum2 *= val
                assigned2 += 1
            elif v in game_kenken.infer_assignment():
                sum2 *= game_kenken.infer_assignment()[v]
                assigned2 += 1

        if sum2 == blockValue[blockNum] and assigned2 == len(blockVariables[blockNum]):
            return True
        elif sum2 <= blockValue[blockNum] and assigned2 < len(blockVariables[blockNum]):
            return True
        else:
            return False

    elif blockOp[blockNum] == 'div':
        for v in blockVariables[blockNum]:
            if v != var:
                constraintVar2 = v

        if constraintVar2 in game_kenken.infer_assignment():
            constraintVal2 = game_kenken.infer_assignment()[constraintVar2]
            return max(constraintVal2, val) / min(constraintVal2, val) == blockValue[blockNum]
        else:
            for d in game_kenken.choices(constraintVar2):
                if max(d, val) / min(d, val) == blockValue[blockNum]:
                    return True

            return False

    elif blockOp[blockNum] == 'sub':
        for v in blockVariables[blockNum]:
            if v != var:
                constraintVar2 = v

        if constraintVar2 in game_kenken.infer_assignment():
            constraintVal2 = game_kenken.infer_assignment()[constraintVar2]
            return max(constraintVal2, val) - min(constraintVal2, val) == blockValue[blockNum]
        else:
            for d in game_kenken.choices(constraintVar2):
                if max(d, val) - min(d, val) == blockValue[blockNum]:
                    return True

            return False	


def display(dic, size):
    for i in range(size):
        for j in range(size):
            string = 'K' + str(i) + str(j)
            sys.stdout.write(str(dic[string]) + " ")
        print()
	
		
		
		
if __name__ == '__main__':
    """Read first line from file"""
    with open(sys.argv[1], 'r') as f:
        size = int(f.readline())

    """Create variables list"""
    variables = []

    for i in range(size):
        for j in range(size):
            variables.append('K' + str(i) + str(j))

    """Create domains dictionary"""
    dictDomainsValues = list(range(1, size+1))
    domains = dict((v, dictDomainsValues) for v in variables)

    """Create neighbors dictionary"""
    neighbors = {}

    for v in variables:
        dictNeighborValue = []
        coordinateX = int(list(v)[1])
        coordinateY = int(list(v)[2])

        for i in range(size):
            if i != coordinateY:
                string = 'K' + str(coordinateX) + str(i)
                dictNeighborValue.append(string)
            if i != coordinateX:
                string = 'K' + str(i) + str(coordinateY)
                dictNeighborValue.append(string)

        neighbors[v] = dictNeighborValue

    """Read rest lines from file"""
    with open('kenken5.txt', 'r') as f:
        lines = f.readlines()[1:]

    """Create constraint data lists"""
    blockVar = []
    blockOp = []
    blockValue = []

    for l in lines:
        var, op, val = l.split()

        blockVar.append(re.findall('\d+', var))
        blockOp.append(op)
        blockValue.append(int(val))

    blockVariables = []

    for i in range(len(blockVar)):
        blockList = []
        for j in range(0, len(blockVar[i]), 2):
            string = 'K' + str(blockVar[i][j]) + str(blockVar[i][j+1])
            blockList.append(string)

        blockVariables.append(blockList)

    game_kenken = csp.CSP(variables, domains, neighbors, kenken_constraint)

    start = time.time()

    if sys.argv[2] == "BT":
        print("Using BT algorithm to solve the puzzle")
        print()
        display(csp.backtracking_search(game_kenken), size)    		
    elif sys.argv[2] == "BT+MRV":
        print("Using BT and MRV algorithms to solve the puzzle")
        print()
        display(csp.backtracking_search(game_kenken, select_unassigned_variable=csp.mrv), size)
    elif sys.argv[2] == "FC":
        print("Using FC algorithm to solve the puzzle")
        print()
        display(csp.backtracking_search(game_kenken, inference=csp.forward_checking), size)
    elif sys.argv[2] == "FC+MRV":
        print()
        print("Using FC and MRV algorithms to solve the puzzle")
        display(csp.backtracking_search(game_kenken, select_unassigned_variable=csp.mrv, inference=csp.forward_checking), size)
    elif sys.argv[2] == "MAC":
        print()
        print("Using MAC algorithm to solve the puzzle")
        display(csp.backtracking_search(game_kenken, inference=csp.mac), size)
    else:
	    print("Error in selected algorithm!!!!")

    end = time.time()

    print()
    print("Execution time:", end - start, "seconds")
    print("Number of assignments perfomed:", csp.counterAssignments)