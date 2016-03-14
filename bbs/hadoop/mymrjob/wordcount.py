
from mrjob.job import MRJob
class MRWordCount(MRJob):
    """ Wordcount with MapReduce in a pythonic way"""

    def mapper(self, key, line):
        for word in line.split(' '):
             yield word.lower(), 1

    def reducer(self, word, occurrences):
        yield word, sum(occurrences)

if __name__ == '__main__':
    MRWordCount.run()