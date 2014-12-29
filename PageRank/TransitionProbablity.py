import numpy

__author__ = 'gk'

from PageRank.Iterator import MatrixInfo

# Implements matrix builder helper classes to build link, Teleport matrix used in Page rank calculation
# P = (1- α) * link matrix + α * teleport matrix , input α


from scipy import sparse



class LinkMatrix:
    matrix = sparse.csr_matrix([],dtype=float)

    def __init__(self,matrixInfo):
        super().__init__()
        self.matrix = sparse.coo_matrix((matrixInfo.value,(matrixInfo.row,matrixInfo.column)),shape=(matrixInfo.rowLength,matrixInfo.columnLength),dtype=float)

    def getTeleportMatrix(self):
        telePortMatrix = sparse.coo_matrix(self.matrix,dtype=float)
        telePortMatrixCSR = telePortMatrix.tocsr()
        # Get Average value of non zero elements in each arrow, assign the avg back to non zero elements positions
        for r in telePortMatrix.row:
            rowCount = telePortMatrix.getrow(r).nnz
            rowSum = telePortMatrix.getrow(r).sum()
            avg = rowSum/rowCount
            for c in telePortMatrix.col:
                if telePortMatrixCSR[r,c] != 0:
                    telePortMatrixCSR[r,c] = avg
        return telePortMatrixCSR.tocoo()



class InitialStateMatrix:
    matrix = sparse.coo_matrix([],dtype=float)

    def __init__(self,matrixInfo,randomSurferAlpha=0.1):
        super().__init__()
        matrixInfo.value*=randomSurferAlpha
        self.matrix = sparse.coo_matrix((matrixInfo.value,(matrixInfo.row,matrixInfo.column)),shape=(matrixInfo.rowLength,matrixInfo.columnLength),dtype=float)

class TransitionMatrix:
    initialStateMatrix = sparse.coo_matrix([],dtype=float)
    telePortMatrix = sparse.coo_matrix([],dtype=float)
    transitionMatrix = sparse.coo_matrix([],dtype=float)

    def __init__(self,initialStateMatrix,telePortMatrix):
        super().__init__()
        self.telePortMatrix = telePortMatrix
        self.initialStateMatrix = initialStateMatrix
        self.transitionMatrix = sparse.coo_matrix(self.initialStateMatrix.tocsr() + self.telePortMatrix.tocsr())

    def getTransitionMatrix(self):
        return self.transitionMatrix


def buildLinkMatrixInfo(screenNameIndex,TweetInfoList,value,rowSize,columnSize):
    row = list()
    column = list()
    values = list()
    for tweet in TweetInfoList:
        for user_mention in tweet.user_mentions:
            column.append(screenNameIndex.nameToIdMap[user_mention])
            row.append(screenNameIndex.nameToIdMap[tweet.screen_name])
            values.append(value)
    return MatrixInfo(numpy.array(row),numpy.array(column),numpy.array(values),rowSize,columnSize)


def buildInitialStateMatrixInfo(value,rowSize,columnSize):
    rows = numpy.empty(shape=((rowSize*columnSize)),dtype=int)
    columns = numpy.empty(shape=((rowSize*columnSize)),dtype=int)
    values = numpy.full(shape=((rowSize*columnSize)),fill_value=value,dtype=float)
    for i in range(0,rowSize):
        for j in range(0, columnSize):
            index = i*rowSize+j
            rows.flat[index]=i
            columns.flat[index]=j
    return MatrixInfo(rows,columns,values,rowSize,columnSize)

def buildStartMatrix(row,column,value,rowLength,columnLength):
    return  sparse.coo_matrix(([value],([row],[column])),shape=(rowLength,columnLength),dtype=float)
