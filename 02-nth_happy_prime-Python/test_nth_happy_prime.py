import os,sys
sys.path.append(os.getcwd())
from nth_happy_prime import fun_nth_happy_prime
import pytest


@pytest.mark.parametrize('a, result',[
    (0,7),(1,10),(2,13),(3,19),(4,23)
])
def test_fun_nth_happy_prime(a, result):
    assert fun_nth_happy_prime(a) == result

