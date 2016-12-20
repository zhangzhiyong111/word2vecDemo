#encoding="utf-8"
#!/usr/bin/env python

import sys
import time
from gensim.models import word2vec

reload( sys )
sys.setdefaultencoding( "utf-8" )

"""

#  This is the demo for get the chinese word embeding by means of word2vec algorithm 
#  the input the sentence that have been segment
#  tht output is the word and his embedding

"""
def getModel( inputFile ) :
	sentence = word2vec.Text8Corpus( inputFile )  # get the format of word2vec
	model = word2vec.Word2Vec( sentence , size = 200, window = 5, min_count=5, iter = 5 )  # set the parameters for the model
	model.save( "./word2vecModel", binary = 0)  # save the model in current dir


def main() :
	inputFile = "../processData/word2vecFormatPath"
	model = getModel( inputFile )


if __name__ == '__main__' :
	begin = time.clock()
	main()
	end = time.clock()
	print "The cost of time is : %f"%( end - begin )
