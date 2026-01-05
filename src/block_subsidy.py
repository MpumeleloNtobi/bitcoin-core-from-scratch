def get_block_subsidy(block_height):
    """Takes the height of a blockchain block and returns the block subsidy (rewaed) in satoshis.
    
    Arguments:
        - block_subsidy (int): the block height (genesis block is at height zero). 

    Returns: 
        - subsidy (float): the block subsidy in satoshis.
        
    """

    INITIAL_BLOCK_SUBSIDY = 5000000000 # Set by Satoshi
    HALVING_INTERVAL = 210000 # Height (block number - zero indexed)

    if block_height < 0:
        raise ValueError("Invalid: negative height")
    elif block_height < HALVING_INTERVAL: 
        return INITIAL_BLOCK_SUBSIDY
        
    halving_count = block_height // HALVING_INTERVAL # Floor division
    subsidy = INITIAL_BLOCK_SUBSIDY / (2 ** halving_count)

    if subsidy < 1:
        return 0
    return subsidy
