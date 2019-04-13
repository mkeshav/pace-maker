# coding:utf-8

from pacemaker.pacemaker import PaceMaker
import time

def pace_me(data_gen, rate_per_second, **data_gen_kwargs):
    """
        Returns decorator for backoff and retry triggered by predicate.
        Args:
            data_gen: A generator yielding data that the target function needs
            rate_per_second: Rate.
            number_of_tokens_per_call: Number of tokens to consume per target function call
            data_gen_kwargs: Any additional keyword args specified will be
-            passed to data_gen function.
    """
    def decorate(target):
        p = PaceMaker()
        p.set_rate_per_second(rate_per_second)
        for d in data_gen(**data_gen_kwargs):
            target(d)
            # Do not import sleep directly as we want to monkey patch this during tests.
            time.sleep(p.consume(1))

    return decorate
