# 3SAT Problem

#using DPLL Algorithm

def simplify(clauses, assignment):
    new_clauses = []
    for clause in clauses:
        new_clause = []
        satisfied = False
        for lit in clause:
            var = abs(lit)
            if var in assignment:
                value = assignment[var]
                lit_value = value if lit > 0 else not value
                if lit_value:
                    satisfied = True
                    break
            else:
                new_clause.append(lit)
        if not satisfied:
            new_clauses.append(new_clause)
    return new_clauses


def dpll(clauses, assignment):
    clauses = simplify(clauses, assignment)

    if len(clauses) == 0:
        return True, assignment
    if [] in clauses:
        return False, {}

    # unit propagation
    for clause in clauses:
        if len(clause) == 1:
            lit = clause[0]
            var = abs(lit)
            value = lit > 0
            new_assignment = assignment.copy()
            new_assignment[var] = value
            return dpll(clauses, new_assignment)

    # pick the first unassigned variable and branch
    var = abs(clauses[0][0])
    for value in [True, False]:
        new_assignment = assignment.copy()
        new_assignment[var] = value
        result, final_assignment = dpll(clauses, new_assignment)
        if result:
            return True, final_assignment

    return False, {}


# Main Program
num_vars = int(input("Enter number of variables: "))
num_clauses = int(input("Enter number of clauses: "))

print("Enter each clause with exactly 3 literals.")
print("Use a positive number for a variable and a negative number for its negation.")
print("Example: 1 -2 3")

formula = []
for i in range(num_clauses):
    clause = list(map(int, input(f"Clause {i + 1}: ").split()))
    formula.append(clause)

print("\nFormula entered:", formula)

satisfiable, assignment = dpll(formula, {})

if satisfiable:
    print("\nSatisfiable")
    print("Assignment:")
    for var in range(1, num_vars + 1):
        value = assignment.get(var, "any")
        print(f"x{var} = {value}")
else:
    print("\nUnsatisfiable")