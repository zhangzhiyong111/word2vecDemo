#encoding="utf-8"
#!/usr/bin/env python

import sys
import jieba
import json
import re
import unicodedata

reload( sys )
sys.setdefaultencoding( "utf-8" )

"""

# This is the preproces for the word2vec training
# the input the format like this : {"content":"we just use the number","time":"2016-10-01","websiteId":"3254784"} and we get the \
#  "we just use the number " and we igore other information
# the output is sentence that have been segment

"""

def getdoc( filePath , content ) :    # get the content for the sql
	docSet = list()

	with open( filePath , 'r' ) as f :
		for line in f :
			postInfor = json.loads( line.strip() )
			if postInfor.has_key( content ) :
				docSet.append( postInfor[ content ] )

	return docSet

def writeFile( docSet , writeTofilePath ) :  # the data that have been handled to write to file
	fw = open( writeTofilePath , 'a' )

	for sentence in docSet :
		segList = list( jieba.cut( sentence , cut_all = False ) )   # segment the sentence 
		segListFilter = [ word.encode( "utf-8" ) for word in segList if ( not re.match( r'.*(\w|\d)+.*' , unicodedata.normalize('NFKD', word ).encode('ascii','ignore') ) ) ]
		segListFilter.append( "\n" )
		fw.write( "\t".join( segListFilter ) )

	fw.close()

def preProcess() :
	filePath = "../totalData/allData"    # the raw data source path
	writeTofilePath = "../processData/word2vecFormatPath"  # the path that handled data to write

	docSet = getdoc( filePath , "content".decode( "utf-8" ) )
	writeFile( docSet , writeTofilePath )

if __name__ == '__main__' :
	preProcess()