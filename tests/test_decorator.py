import pytest
from pacemaker import pace_me

from unittest.mock import patch, call

def data_gen(n=3):
    for i in range(n):
        yield [x for x in range(n)]

def process(data):
    print('Processing....{0}'.format(data))

@patch('time.sleep', side_effect=lambda x: None)
@patch('test_decorator.process', side_effect=lambda x, **y: None)
def test_pace_me(mock_process, mock_sleep):
    decorated_func = pace_me(data_gen, rate_per_second=3, n=6)
    wrapped = decorated_func(mock_process)
    wrapped(a=1)
    mock_process.assert_called_with([0, 1, 2, 3, 4, 5], a=1)
    calls = [
                call([0, 1, 2, 3, 4, 5], a=1), call([0, 1, 2, 3, 4, 5], a=1), 
                call([0, 1, 2, 3, 4, 5], a=1), call([0, 1, 2, 3, 4, 5], a=1),
                call([0, 1, 2, 3, 4, 5], a=1), call([0, 1, 2, 3, 4, 5], a=1)
            ]
    mock_process.assert_has_calls(calls, any_order=False)
    sleep_calls = [call(0.667), call(0.333), call(1), call(1), call(1), call(1)]
    mock_sleep.assert_called_with(1)
    mock_sleep.assert_has_calls(sleep_calls, any_order=False)