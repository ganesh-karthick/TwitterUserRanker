__author__ = 'gk'

import optparse
import os
from ParserUtils.Parser import Parser
from PageRank.TweetInfo import asTweetInfo,asPartialTweetInfo, TweetInfo
from PageRank.ScreenNameIndex import ScreenNameIndex,UserRank
from PageRank.TransitionProbablity import buildInitialStateMatrixInfo,buildLinkMatrixInfo,LinkMatrix,InitialStateMatrix,TransitionMatrix,buildStartMatrix
from PageRank.Iterator import Iterator
from GraphicsPlot import BarGraph



##### main ####


parser = optparse.OptionParser()
helpText = "Usage: \n python main.py  -f , --file=<InputJSONFile> \n[optional] -t , --topXUsers=<number>"

parser.add_option('-f', '--file',
    action="store", dest="file",type="string",
    help=helpText)
parser.add_option('-t', '--topX',
    action="store", dest="topX",type="int",
    help=helpText,default=15)

options, args = parser.parse_args()

if not options.file:   # if filename is not given
    print(helpText)
    parser.error("Filename not given")

inputFileName = options.file
topX = options.topX
if not os.path.isfile(inputFileName):
        print(helpText)
        parser.error("File does not exist")



print("Loading file " + inputFileName)
randomSurferAlpha = 0.1
tweetParse = Parser(inputFileName)
tweetInfoList = tweetParse.parseFile(asPartialTweetInfo)
TweetInfo.unique_screen_names = sorted(TweetInfo.unique_screen_names)


screenNameIndex = ScreenNameIndex(TweetInfo.unique_screen_names)
matrix_size = len(TweetInfo.unique_screen_names)
print("Found %d unique users who are connected to other users" % (matrix_size))
print(TweetInfo.unique_screen_names)
# for tweet in tweetInfoList:
#     print(tweet)
print("Built Screen Name with Index")
#print(screenNameIndex)

initialStateMatrix = InitialStateMatrix(buildInitialStateMatrixInfo(1/matrix_size,matrix_size,matrix_size),randomSurferAlpha)
print("Built Initial State Matrix")
linkMatrix = LinkMatrix(buildLinkMatrixInfo(screenNameIndex,tweetInfoList,1,matrix_size,matrix_size))
print("Built Link Matrix")
transitionMatrix = TransitionMatrix(initialStateMatrix.matrix,linkMatrix.getTeleportMatrix())
print("Built Transition Matrix")
iterator = Iterator(buildStartMatrix(0,0,1,1,matrix_size),transitionMatrix.getTransitionMatrix())
print("Starting Rank Calculation")
iterator.buildPageRank()
userRankList = UserRank.buildUserRankList(screenNameIndex,iterator.xConverged)
print("Twitter User Influence Rank:")
count = 0
for userRank in userRankList:
    count+=1
    print("Rank %d %s" % (count,userRank))

print("Generating Top X user Graph")

BarGraph.barPlot(userRankList)

###### End Main ######






