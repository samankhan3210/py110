def valid_structure(given_no_of_blocks):
    remaining_blocks = given_no_of_blocks
    current_layer = 0
    current_layer_blocks_req = 0
    
    while remaining_blocks >= current_layer_blocks_req:
        remaining_blocks -= current_layer_blocks_req
        current_layer += 1
        current_layer_blocks_req = current_layer * current_layer

    return remaining_blocks

def main():
    print(valid_structure(0) == 0)  # True
    print(valid_structure(1) == 0)  # True
    print(valid_structure(2) == 1)  # True
    print(valid_structure(4) == 3)  # True
    print(valid_structure(5) == 0)  # True
    print(valid_structure(6) == 1)  # True
    print(valid_structure(14) == 0) # True

if __name__ == "__main__":
    main() 