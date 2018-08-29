# Initializing our blockchain list
blockchain = []

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchanin value to the blockchain
        Arguemnts:
            :transaction_amount: The amount that should be added.
            :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input("your choice: ")
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print(" Outputtin Block")
        print(block)
    else:
        print('_' * 20)


def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if  block_index == 0:
            continue
        elif blockchain[block_index] [0] == blockchain[block_index -1]:
            is_valid = True
        else:
            is_valid = False
        # if block_index == 0:
        #     block_index += 1
        #     continue
        # if block[0] == blockchain[block_index -1]:
        #     is_valid = True
        # else:
        #     is_valid = False
        #     break
        # block_index += 1
    return is_valid

waitin_for_input = True

while waitin_for_input:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice =  get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif  user_choice == 'q':
        waitin_for_input = False
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    else:
        print("Input was invalid, pleazse pick a value from the list!")
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid Blockchain!")
        break
else:
    print("User left!")

print("Done!")