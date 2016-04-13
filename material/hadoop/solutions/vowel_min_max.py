# -*- coding: utf-8 -*-

from mrjob.job import MRJob
from mrjob.step import MRStep


class job(MRJob):

    def mapper(self, _, line):
        for char in line.strip().lower():
            if char in 'aeiou':
                yield char, 1

    def reducer(self, key, values):
        mysum = sum(values)
        self.increment_counter("vowels", key, mysum)
        # Move sum and key as values
        yield None, [mysum, key]

    def find_min_max(self, _, values):
        # Avoid consuming the generator more than once
        data = list(values)
        # Use available data to make different computations
        yield "vowel_min_counter", min(data)
        yield "vowel_max_counter", max(data)

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.find_min_max),
        ]

if __name__ == "__main__":
    job.run()
