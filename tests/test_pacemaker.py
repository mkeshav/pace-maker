from pacemaker.pacemaker import PaceMaker
from time import sleep, time
import pytest

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
