import sys

# Add the project src directory tp the python search path
sys.path.insert(0, "src")

import pytest
import block_subsidy

def test_block_subsidy_edge_cases():
    assert block_subsidy.get_block_subsidy(0) == 5000000000  
    assert block_subsidy.get_block_subsidy(209999) == 5000000000  
    assert block_subsidy.get_block_subsidy(210000) == 2500000000
    assert block_subsidy.get_block_subsidy(210001) == 2500000000
    assert block_subsidy.get_block_subsidy(6930000) == 0
    assert block_subsidy.get_block_subsidy(6930001) == 0

def test_block_subsidy_negative_cases():
    with pytest.raises(ValueError):
        block_subsidy.get_block_subsidy(-1)
    with pytest.raises(ValueError):
        block_subsidy.get_block_subsidy(-10)
    
def test_block_subsidy_normal_cases():
    assert block_subsidy.get_block_subsidy(10) == 5000000000  
    assert block_subsidy.get_block_subsidy(210010) == 2500000000
    assert block_subsidy.get_block_subsidy(6930010) == 0 
    
    
