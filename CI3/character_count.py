from mrjob.job import MRJob
import sys

class Character_count(MRJob):
    def mapper(self,_,line):
        for char in line:
            yield char,1
    def reducer(self,key,values):
        yield key,sum(values)

if __name__ == "__main__":
    if len(sys.argv)!=2:
        print("Use python character_count.py <filename>")
        sys.exit(1)
    Character_count.run()