from time import time
from threading import Lock

class PaceMaker(object):
    '''
        Implementation of https://en.wikipedia.org/wiki/Token_bucket#Algorithm
    '''

    @classmethod
    def _epoch_in_seconds(self):
        return round(time())

    def __init__(self):
        self.tokens = 0
        self.rate_per_second = 0
        self.last = self._epoch_in_seconds() #Granularity of seconds is good enough
        self.lock = Lock() # for thread safety
        
    def set_rate_per_second(self, rate_per_second):
        with self.lock:
            self.rate_per_second = rate_per_second
            self.tokens = self.rate_per_second

    def consume(self, tokens=1):
        with self.lock: 
            # if the rate_per_second is set to 0, nothing to do here return 0
            if self.rate_per_second == 0:
                raise Exception('Cannot use the pace maker without setting the heart rate_per_second!!!')

            now = self._epoch_in_seconds()
            time_lapsed = now - self.last
            self.last = now
            # Add rate_per_second x seconds lapsed
            self.tokens += time_lapsed * self.rate_per_second
            # If the bucket is full, discard
            if self.tokens > self.rate_per_second:
                self.tokens = self.rate_per_second

            # subtract the number of tokens being consumed
            self.tokens -= tokens
            # If you make this a decorator, then run the callable here.
            if self.tokens > 0:
                # Calculate the pace based on the tokens left
                return self.tokens/self.rate_per_second
            else:
                return 1 

