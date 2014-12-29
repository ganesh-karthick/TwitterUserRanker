import numpy

__author__ = 'gk'
from scipy.sparse import coo_matrix

# PowerMethod for PageRank
# Start with any distribution (say x=(10…0)).
# • After one step, we’re at xP;
# • after two steps at xP2 , then xP3 and so on.
# • “Eventually” means for “large” k, xPk = a.
# • Algorithm: multiply x by increasing powers of
# P until the product looks stable.

from scipy import sparse
from numpy import array

class MatrixInfo:
    row = numpy.array(list())
    column = numpy.array(list())
    value = numpy.array(list())
    rowLength = 0
    columnLength = 0

    def __init__(self,row,column,value,rowLength,columnLength):
        super().__init__()
        self.row = row
        self.column = column
        self.value = value
        self.rowLength = rowLength
        self.columnLength = columnLength


class Iterator:
    error_limit = 0.01
    iterationCount = 0
    xConverged = sparse.coo_matrix([],dtype=float)
    xMatrix = sparse.coo_matrix([],dtype=float)
    pMatrix = sparse.coo_matrix([],dtype=float)

    def __init__(self,xMatrix,pMatrix,error_limit = 0.001):
        super().__init__()
        self.xMatrix = xMatrix
        self.pMatrix = pMatrix
        self.error_limit = error_limit

    def buildPageRank(self):
        self.iterate(self.xMatrix.tocsr(),self.pMatrix.tocsr())

    def iterate(self,x,p):
        Iterator.iterationCount+=1
        print("Iteration count %d " % (Iterator.iterationCount))
        y = x*p
        diff = y-x
        x = y
        while not self.isConverged(diff):
            Iterator.iterationCount+=1
            print("Iteration count %d " % (Iterator.iterationCount))
            y = x*p
            diff = y-x
            x = y
        self.xConverged = x.tocoo()




    def isConverged(self,cx):
        for value in zip(cx.data):
            if abs(value[0]) > self.error_limit:
                return False
        return True

    def __str__(self, *args, **kwargs):
        desc = "Converged Matrix\n"
        for i,j,v in zip(self.xConverged.row, self.xConverged.col, self.xConverged.data):
             desc = desc + "Row: " + repr(i) + " Column: " + repr(j) + " Value: " + repr(format(v,".3f")) + "\n"
        return desc











