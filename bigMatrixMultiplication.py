import numpy as np

class bigmatmul():

    @staticmethod
    def large_matrix_multiplication(rows_matrix1, cols_matrix1, rows_matrix2, cols_matrix2):
        # Define a function to generate random matrices
        def random_matrix(rows, cols):
            return np.random.randint(1, 100, size=(rows, cols))

        # Create large random matrices
        matrix1 = random_matrix(rows_matrix1, cols_matrix1)
        matrix2 = random_matrix(rows_matrix2, cols_matrix2)

        # Perform matrix multiplication
        result_matrix = np.dot(matrix1, matrix2)

        return result_matrix

if __name__ == "__main__":
    # Define the size of the large matrices (adjust these values as needed)
    rows_matrix1 = 1000
    cols_matrix1 = 1000
    rows_matrix2 = 1000
    cols_matrix2 = 1000

    # Call the function to perform matrix multiplication
    result_matrix = bigmatmul.large_matrix_multiplication(rows_matrix1, cols_matrix1, rows_matrix2, cols_matrix2)

    # Print the result or do further processing with it
    print(result_matrix)
