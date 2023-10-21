'''
Byimann

Author - Subhpreet Singh
Date - 20 October, 2023


Backend Skills -  Django, Java, Django Rest Framework (API's), MySql, Object Orienting Programming
Frontend Skills - React, Html, Css, JavaScript, Landing Pages

"----- This is coded to help in Math Assignments and to implement the mathematical applications in programming -----"

"These classes, developed in Python, encapsulate a powerful set of tools for matrix manipulation and operations.
  The Matrix class provides a versatile framework for creating, setting, and modifying matrices of various dimensions,
    while the SingleMatrixOperations and MatrixOperations classes offer extensive functionality for performing mathematical
      operations on matrices, such as addition, multiplication, finding determinants, and solving linear equations.
       These classes are not only a testament to my proficiency in Python but also serve as a valuable resource for anyone
        working with matrices in programming. Feel free to explore and utilize these classes for your own projects,
         and I welcome any feedback or contributions to enhance their capabilities."

'''



from Matrix import Matrix

class SingleMatrixOperations:
    # Initialize the SingleMatrixOperations class with a matrix (M).
    def __init__(self,M : None or Matrix):

        self.matrix = M

    def isSquare(self):
        # Check if the matrix is square (number of rows equals number of columns).
        return self.matrix.m == self.matrix.n

    def scaleTheMatrix(self,multiplier,matrix:Matrix):
        # Scale a matrix by multiplying each element by a multiplier.
        M = Matrix(matrix.m,matrix.n)

        for i in range(M.m):
            M.setEntireRow(i,list(map(lambda x: x * multiplier,matrix.getRow(i))))

        return M

    def getSubMatrixForDeterminant(self,rIndex,cIndex):

        # Get a submatrix by excluding a specific row (rIndex) and column (cIndex).
        if ( 0 > rIndex > self.matrix.m and 0 > cIndex > self.matrix.n):
            raise ValueError(" Give valid inputs for the index of row and column describing the position of element in the matrix")

        if self.isSquare():
            M = Matrix(self.matrix.m - rIndex, self.matrix.n - cIndex)

            for i in range(M.m):
                M.setEntireRow(i,self.matrix.getRow((self.matrix.m - M.m) + i)[cIndex:])

            return M

        return ValueError("Something went wrong! during the execution.")

    def determinantOf2by2Matrix(self, matrix: None or Matrix):
        # Calculate the determinant of a 2x2 matrix.
        # this method will be the base case to find the determinant of bigger matrices.
        if matrix:
            return matrix.matrix[0][0] * matrix.matrix[1][1] - matrix.matrix[1][0] * matrix.matrix[0][1]

        if(matrix == None and self.matrix.m == self.matrix.n == 2):
            return self.matrix.matrix[0][0] * self.matrix.matrix[1][1] - self.matrix.matrix[1][0] * self.matrix.matrix[0][1]
        else:
            return None

    def skipColumnOnlyForDeterminant(self,lineColumnIndexToSkip,matrix):
        # Create a submatrix by skipping a specific column (lineColumnIndexToSkip).
        M = Matrix(matrix.m-1,matrix.n - 1)

        if 0 > lineColumnIndexToSkip > M.n:
            return ValueError(" You gave the wrong the index for the column")

        for i in range(0,M.m):
            M.setEntireRow(i,matrix.getRow(i+1)[:lineColumnIndexToSkip] + matrix.getRow(i+1)[lineColumnIndexToSkip+1:])

        return M

    def skipRowAndColumn(self,rowLineIndex,colLineIndex,matrix: Matrix):
        # Create a submatrix by excluding a specific row (rowLineIndex) and column (colLineIndex).
        M = Matrix(matrix.m - 1,matrix.n - 1)

        if 0 > colLineIndex > M.n:
            return ValueError(" You gave the wrong the index for the column line")

        if 0 > rowLineIndex > M.m:
            return ValueError(" You gave the wrong the index for the row line")

        fillingIndex = 0

        for i in range(matrix.m):
            if (i == rowLineIndex):
                continue
            else:
                M.setEntireRow(fillingIndex,matrix.getRow(i)[:colLineIndex] + matrix.getRow(i)[colLineIndex+1:])
                fillingIndex += 1

        return M



    def getDeterminant(self,matrix:Matrix):
        # Calculate the determinant of a matrix using recursive cofactor expansion.
        if [matrix.m,matrix.n] == [2,2]:

            return self.determinantOf2by2Matrix(matrix)


        value = sum([((-1)**i) * matrix.matrix[0][i] *( self.getDeterminant(self.skipColumnOnlyForDeterminant(i,matrix))) for i in range(matrix.n)])


        return value

    def getAdjacencyOf2By2Matrix(self,matrix: Matrix):
        # Calculate the adjugate of a 2x2 matrix.
        if matrix.dimension != [2,2]:
            raise ValueError(" This method can be only be used for the matrices of size 2 x 2.")

        matrix.matrix[0][0] , matrix.matrix[1][1] = matrix.matrix[1][1] , matrix.matrix[0][0]

        matrix.matrix[0][1], matrix.matrix[1][0] = -matrix.matrix[1][0], -matrix.matrix[0][1]

        return matrix

    def getAdjacenyMatrix(self,matrix : Matrix):
        # Calculate the adjugate (adjacency) matrix for any square matrix.
        M = Matrix(matrix.m,matrix.n)
        if matrix.dimension == [2, 2]:
            return self.getAdjacencyOf2By2Matrix(matrix)

        if matrix.isSquareMatrix():

            for row in range(matrix.m):
                for col in range(matrix.n):
                    M.setIndividualvalue(row,col,(-1)**(row+col)*self.getDeterminant(self.skipRowAndColumn(row,col,matrix)))

            return M

        raise ValueError('Something went wrong!')

    def getTransposeMatrix(self,matrix: Matrix):
        # Calculate the transpose of a matrix.
        M = Matrix(matrix.n,matrix.m)
        for i in range(M.m):
            M.setEntireRow(i,matrix.getColumn(i))
        return M

    def getAdjointMatrix(self,matrix: Matrix):
        M = self.getAdjacenyMatrix(matrix)
        return self.getTransposeMatrix(M)


    def getInverse(self,M : Matrix):
        # Calculate the adjoint matrix for a square matrix.
        # inverse = adjoint(M) / det(M)

        deter = self.getDeterminant(M)

        adjointMatrix = self.getAdjointMatrix(M)

        return self.scaleTheMatrix(1/deter,adjointMatrix)


if __name__ == "__main__":
    M = Matrix(4, 4)

    M.setEntireMatrix([[2, 4, 6, 8], [1, 6, 4, 10], [2, 4, 9, 33], [8, 9, 1, 7]])

    operation = SingleMatrixOperations(M).getDeterminant(M)

    print(operation)
    pass
    # M = Matrix(4,4)
    #
    # M.setEntireMatrix([[2,4,6,8],[1,6,4,10],[2,4,9,33],[8,9,1,7]])

    # M = Matrix(2,2)
    # M.setEntireMatrix([[8,1],[8,6]])
    # M.printMatrix()

    #
    # M = Matrix(3,3)
    # M.setEntireMatrix([[1,1,-2],[0,1,1],[2,6,1]])
    #
    # M.printMatrix()
    #
    # operation = SingleMatrixOperations(M)
    # operation.getTransposeMatrix(M).printMatrix()





