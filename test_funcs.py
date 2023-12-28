import pytest
import numpy as np
from funcs import *

def test_new_array():
    assert len(new_array(5)) == 5
    