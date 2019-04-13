from pacemaker.pacemaker import PaceMaker
from time import sleep, time
import pytest
from pacemaker._decorator import pace_me

from unittest.mock import patch, call

def test_set_rate():
    p = PaceMaker()
    p.set_rate_per_second(20)
    assert p.rate_per_second == 20
    assert p.tokens == 20

def test_consume():
    p = PaceMaker()
    p.set_rate_per_second(2)
    assert p.consume() == 0.5
    assert p.tokens == 1
    p.consume()
    assert p.tokens == 0
    assert p.consume() == 1
    
def test_consume_bucket_full():
    p = PaceMaker()
    p.set_rate_per_second(60)
    p.consume(tokens=30) # consume 30 tokens, 30 left after this
    assert p.tokens == 30
    sleep(1)
    p.consume() # After a second bucket should have 119 tokens, but still be set to 60 and then consume 1
    assert p.tokens == 59


def test_rate_not_set():
    p = PaceMaker()
    with pytest.raises(Exception) as e_info:
        p.consume()


def data_gen(n=3):
    for i in range(n):
        yield [x for x in range(n)]

def process(data):
    print('Processing....{0}'.format(data))

@patch('time.sleep', side_effect=lambda x: None)
@patch('test_pacemaker.process', side_effect=lambda x: None)
def test_pace_me(mock_process, mock_sleep):
    decorated_func = pace_me(data_gen, rate_per_second=3, number_of_tokens_per_call=1, n=6)
    decorated_func(mock_process)
    mock_process.assert_called_with([0, 1, 2, 3, 4, 5])
    calls = [
                call([0, 1, 2, 3, 4, 5]), call([0, 1, 2, 3, 4, 5]), 
                call([0, 1, 2, 3, 4, 5]), call([0, 1, 2, 3, 4, 5]),
                call([0, 1, 2, 3, 4, 5]), call([0, 1, 2, 3, 4, 5])
            ]
    mock_process.assert_has_calls(calls, any_order=False)