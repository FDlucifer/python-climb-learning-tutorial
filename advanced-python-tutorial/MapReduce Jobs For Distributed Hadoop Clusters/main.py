# https://jmcauley.ucsd.edu/data/amazon
# pip install mrjob

import re
import json
from mrjob.job import MRJob
from mrjob.step import MRStep

class WordCounter(MRJob):
    def mapper(self, key, value):
        review = json.loads(value)
        review_text = review['reviewText']

        tokens = re.findall(r"\b\w+\b", review_text.lower())
        for token in tokens:
            yield token, 1

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield None, (sum(values), key)

    def reducer_sorter(self, key, values):
        for count, key in sorted(values):
            yield count, key

    def steps(self):
        return [
            MRStep(
                mapper = self.mapper,
                combiner = self.combiner,
                reducer = self.reducer
            ),
            MRStep(
                reducer = self.reducer_sorter
            )
        ]

if __name__ == "__main__":
    WordCounter.run()
