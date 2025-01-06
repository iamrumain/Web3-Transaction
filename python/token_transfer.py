import json
from web3 import Web3
from eth_account import Account



# Connect to Ethereum node (Infura or local node)
infura_url = "YOUR RPC URL"
w3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected
if w3.isConnected():
    print("Connected network")
else:
    print("Failed to connect network")




private_key = "YOUR PRIVATE KEY"
sender_account = Account.privateKeyToAccount(private_key)
sender_address = sender_account.address



# Set the contract address
token_address = "TOKEN CONTRACT ADDRESS"


# Create contract instance
token_contract = w3.eth.contract(address=token_address, abi=json.load(open('./abi/token.abi')))


balanceOf = token_contract.functions.balanceOf(sender_address).call()
symbol = token_contract.functions.symbol().call()

print(f'Sender Total Balance : {balanceOf/10**18} \n Token Symbol : {symbol}')





recipient_address = "RECIPIENT_ADDRESS"

# Total send amount
amount = 100 * (10 ** 18)  # assuming 18 decimals for the token





gas_estimate = token_contract.functions.transfer(recipient_address, balanceOf).estimateGas({'from': sender_address,})

transaction = token_contract.functions.transfer(
    recipient_address, amount
).buildTransaction({
    'chainId': w3.eth.chain_id,  
    'gas': gas_estimate,
    'gasPrice': w3.eth.gas_price,
    'nonce': w3.eth.getTransactionCount(sender_address),
    'from': sender_address
})

# Sign the transaction with the private key (make sure it's kept secure)
signed_txn = w3.eth.account.sign_transaction(transaction, "SENDER_PRIVATE_KEY")

# Send the transaction
txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

# Wait for the receipt
txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
print(f"Transaction successful with hash: {txn_hash.hex()}")
print(f"Transaction receipt: {txn_receipt}")
