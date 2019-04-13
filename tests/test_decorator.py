import pytest
from pacemaker._decorator import pace_me

from unittest.mock import patch, call

def data_gen(n=3):
    for i in range(n):
        yield [x for x in range(n)]

def process(data):
    print('Processing....{0}'.format(data))

@patch('time.sleep', side_effect=lambda x: None)
@patch('test_decorator.process', side_effect=lambda x: None)
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