import pytest
from src.main import sum, isGreaterThan

def testSumWithCharacter():
  with pytest.raises(TypeError):
    sum(2,"5")

@pytest.mark.parametrize(
  "number_1,number_2, expected",
  [
    (5,1,6),
    (sum(4,2),1,7),
  ]
)
def testSumParams(number_1,number_2, expected):
  assert sum(number_1,number_2) == expected

def testSumIsInt():
  assert isinstance(sum(2,3), int)

def testIsGreaterThan():
  assert isGreaterThan(5,2)

def testIsNotGreaterThan():
  assert not isGreaterThan(2,3)