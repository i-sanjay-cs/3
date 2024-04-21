from mrjob.job import MRJob
import re
import sys

word_re = re.compile(r"[\w']+")

class Word_Count(MRJob):
    def mapper(self,_,line):
        for word in word_re.findall(line):
            yield word.lower(),1
    def reducer(self,key,values):
        yield key,sum(values)
        
if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("Use python word_count <filename>")
        sys.exit(1)
    Word_Count.run()
        