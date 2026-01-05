def get_block_subsidy(block_height):
    INITIAL_BLOCK_SUBSIDY = 5000000000 # Set buy Satoshi
    HALVING_INTERVAL = 210000 # Height (block number - zero indexed)

    if block_height < 0:
        raise ValueError("Invalid: negative height")
    elif block_height < 210000: 
        return 5000000000
        
    halving_count = block_height // HALVING_INTERVAL # Floor division
    subsidy = INITIAL_BLOCK_SUBSIDY / (2 ** halving_count)

    if subsidy < 1:
        return 0
    return subsidy
