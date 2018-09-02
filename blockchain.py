# Initializing our blockchain list
genesis_block = {'previous_hash': '', 'index': 0, 'transactions': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'Matt'


def hashs_block():
    return  '-'.join([str(block[key]) for key in block])



def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender = owner, amount = 1.0):
    """ Append a new value as well as the last blockchanin value to the blockchain
        Arguemnts:
            :sender: The sender of the coins.
            :recipient: The recipient of the coins.
            :amount: The quantity of coins sent with the transaction (default 1.0).
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)
   

def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hashs_block(last_block)
    block = {'previous_hash': hashed_block, 'index': len(blockchain), 'transactions': open_transactions}
    blockchain.append(block)

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
    """Verify the current blockchain and return True if it's valid, False if it's invalid"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] == hashs_block(blockchain[index - 1]):
            return False
    return True


waitin_for_input = True

while waitin_for_input:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Mine a new block")
    print("3: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice =  get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add transaction amount to the blockchain
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif  user_choice == 'q':
        waitin_for_input = False
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '', 'index': 0, 'transactions': [{'sender': 'Max', 'recipient': 'Mat', 'amount': 100.0}]}
    else:
        print("Input was invalid, pleazse pick a value from the list!")
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid Blockchain!")
        break
else:
    print("User left!")

print("Done!")