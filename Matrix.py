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

class UnValidMatrix(Exception):
    def __init__(self, message):
        super().__init__(message)



class Matrix:

    def __init__(self,m : int , n : int):
        # Initialize the matrix with dimensions m rows and n columns.
        self.m = m
        self.m = m
        self.n = n
        self.matrix = [[0 for j in range(self.n)] for i in range(self.m)]
        self.dimension = [self.m,self.n]

    def __str__(self):
        # Convert the matrix to a formatted string for printing.
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def getRow(self,lineIndex):
        # Get a specific row of the matrix by its index.
        return self.matrix[lineIndex]

    def getColumn(self,lineIndex):
        # Get a specific column of the matrix by its index.
        return [self.matrix[i][lineIndex] for i in range(self.m)]

    def getValue(self, whichRow, whichColumn):
        # Get the value at a specific row and column in the matrix.
        return self.matrix[whichRow][whichColumn]


    def verify(self):
        # Verify that the dimensions of the matrix are valid (positive integers).
        if(type(self.m) != int and type(self.n) != int):
            raise UnValidMatrix('Dimensions of matrix should always be given in integer.')


        if(self.m < 1 and self.n < 1):
            raise UnValidMatrix('UnValid Matrix, THe size of matrix could never be in the negative.')

        return True

    def constructMatrix(self):
        # Construct a matrix if the dimensions are valid
        if (self.verify()):
            setMatrix = [[0 for j in range(self.n)] for i in range(self.m)]

            return setMatrix
        raise UnValidMatrix(' Your given data to built the matrix is not valid.')

    def compareMatrixWithList(self,wholeList):
        # Compare the dimensions of the matrix with a 2D list to ensure they match.
        # just to protect the fundamental law of matrix.
        return (all(len(sublist) == self.n for sublist in wholeList) and len(wholeList) == self.m)

    def setEntireMatrix(self,wholeList):
        # Set the entire matrix using a 2D list if the dimensions match.
        if self.compareMatrixWithList(wholeList):

            for i in range(len(wholeList)):
                self.matrix[i] = wholeList[i]
            return

        raise ValueError(" Something went during the execution of setEntireMatrix. ")


    def setEntireRow(self, rowIndex : int, rowArray : list):
        # Set an entire row of the matrix at the specified index.
        if (rowIndex > self.m and rowIndex < 0):
            raise UnValidMatrix(f"The maximum number of rows is {self.m} with the maximum row index of {self.m - 1}")

        if (self.n != len(rowArray)):
            raise UnValidMatrix(f"The given row size is not equal to {self.m}")

        self.matrix[rowIndex] = rowArray

        return

    def setEntireColumn(self, columnIndex : int, columnArray ):
        # Set an entire column of the matrix at the specified index.
        if (columnIndex > self.n and columnIndex < 0):
            raise UnValidMatrix(f"The maximum number of columns is {self.n} with the maximum column index of {self.n - 1}")

        if (self.m != len(columnArray)):
            raise UnValidMatrix(f"The given column size is not equal to {self.n}")

        for e in range(self.m):
            self.matrix[e][columnIndex] = columnArray[e]

        return

    def setIndividualvalue(self, mIndex, nIndex, value):
        # Set an individual value in the matrix at the specified row and column.
        if (( 0 > mIndex > (self.m - 1)) and ( 0 > nIndex > {self.n - 1})):
            raise ValueError('The given index values are not valid according to the matrix dimension.')
        self.matrix[mIndex][nIndex] = value
        return

    def isSquareMatrix(self):
        # Check if the matrix is square (number of rows equals number of columns).
        return self.m == self.n


    def printMatrix(self):
        # Print the matrix in a readable format.
        for e in self.matrix:
            print(str(e))


if __name__ == "__main__":
    pass
    # m = Matrix(2, 3)
    # m.setEntireRow(1, [1, 2, 3])
    # m.setEntireColumn(2, [10, 10])
    # m.setIndividualvalue(0, 1, 9)
    #
    # m.printMatrix()
    #
    # print(m.getColumn(2))

