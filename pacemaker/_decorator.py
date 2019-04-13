# coding:utf-8

from pacemaker.pacemaker import PaceMaker
from time import sleep

def pace_me(data_gen, rate_per_second=1, number_of_tokens_per_call=1, **data_gen_kwargs):
    def decorate(target):
        p = PaceMaker()
        p.set_rate_per_second(rate_per_second)
        for d in data_gen(**data_gen_kwargs):
            target(d)
            sleep(p.consume(number_of_tokens_per_call))

    return decorate
