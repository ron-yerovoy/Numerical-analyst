#work by:
#Ron Yerovoy 205591142
#Doron Spitzer 313262594 Doron 
#Naor Waitzenberg 315875997
def is_diagonally_dominant(A):
    """
    Check if matrix A is diagonally dominant.
    """
    n = len(A)
    for i in range(n):
        if abs(A[i][i]) <= sum(abs(A[i][j]) for j in range(n) if i != j):
            return False
    return True

def jacobi_method(A, b, tolerance=0.001, max_iter=100):
    """
    Solve Ax = b using Jacobi method.
    """
    n = len(b)
    x = [0] * n

    for _ in range(max_iter):
        x_new = [0] * n
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum1) / A[i][i]

        if max(abs(x_new[i] - x[i]) for i in range(n)) < tolerance:
            return x_new

        x = x_new

    raise ValueError("Jacobi method did not converge")

def gauss_seidel(A, b, tolerance=0.001, max_iterations=1000):
    """
    Solve Ax = b using Gauss-Seidel method.
    """
    n = len(A)
    x = [0] * n

    # Check for diagonal dominance
    if not is_diagonally_dominant(A):
        print("The matrix not have a diagonally dominant.")
        return None
#check how many iteration needed
    for iteration in range(max_iterations):
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x[i] = (b[i] - s1 - s2) / A[i][i]

        # Check for convergence
        if all(abs(x[i] - s1 - s2) < tolerance for i in range(n)):
            return x
    return x

def solve_linear_system(A, b):
    if not is_diagonally_dominant(A):
        return "The matrix is not diagonally dominant. Solution cannot be guaranteed."
    jacobi_solution = jacobi_method(A, b)
    return jacobi_solution

# Main program
if __name__ == "__main__":
    if __name__ == "__main__":
        # Example 3x3 matrix
        A = [
            [10, -1, 4],
            [0, 7, -5],
            [-1, 0, 2]
        ]
        b = [1, 2, 3]

    solution = gauss_seidel(A, b)
    if solution is not None:
        print("Gauss-Seidel Solution:", solution)
        jacobi_solution = solve_linear_system(A, b)
        if jacobi_solution is not None:
            print("Jacobi Solution:", jacobi_solution)
