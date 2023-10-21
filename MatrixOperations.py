from Matrix import Matrix
from SingleMatrixOperations import SingleMatrixOperations
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

class MatrixOperations():

    def __init__(self,M1,M2=None):
        # Initialize the MatrixOperations class with two matrices, M1 and optionally M2.
        self.M1 = M1
        self.M2 = M2
        self.canAddSubtract = (self.M1.dimension == self.M2.dimension) if M2 else False
        self.canBeMultiplied = self.M1.n == self.M2.m if M2 else False


    def addition(self):
        # Perform matrix addition if the dimensions of M1 and M2 allow.
        M = Matrix(self.M1.m,self.M1.n)

        if self.canAddSubtract:
            for i in range(self.M1.m):

                M.setEntireRow(i,list(map(lambda x,y: x+y,self.M1.getRow(i),self.M2.getRow(i))))

        return M

    def multiplication(self):
        # Perform matrix multiplication if the dimensions of M1 and M2 allow.
        if self.canBeMultiplied:
            M = Matrix(self.M1.m,self.M2.n)

            for row_index in range(M.m):
                for column_index in range(M.n):
                    # Calculate the element of the resulting matrix by dot-product of rows and columns.
                    M.setIndividualvalue(row_index,column_index,sum(list(map(lambda x,y : x * y,self.M1.getRow(row_index),self.M2.getColumn(column_index)))))

            return M
        else:
            return ValueError("The dimension of matrices does not allow to do multiplication")

    def scaleTheMatrix(self,multiplier):
        # Scale a matrix by multiplying each element by a multiplier.
        M = Matrix(self.M1.m,self.M1.n)

        for i in range(M.m):
            M.setEntireRow(i,list(map(lambda x: x * multiplier,self.M1.getRow(i))))

        return M


    def findTheValueOfXYZ(self):
        # Find the values of X, Y, and Z by solving linear equations using matrix operations.
        from SingleMatrixOperations import SingleMatrixOperations as singleOperation
        # Create a SingleMatrixOperations instance with no initial matrix (for inverse calculations).
        inverseM = singleOperation(None)
        # Calculate the values using the inverse of M1 and M2.
        values = MatrixOperations(inverseM.getInverse(self.M1), self.M2)
        return values.multiplication()


if __name__ == "__main__":
    pass

    # M = Matrix(2,2)
    # M2 = Matrix(2,2)
    #
    # M.setEntireMatrix([[3,0],[0,-1]])
    # M2.setEntireMatrix([[-4,-5],[-3,2]])
    #
    # operation = MatrixOperations(M,M2).multiplication().printMatrix()

