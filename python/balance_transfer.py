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




recipient_address = "RECIPIENT_ADDRESS"

# Total send amount
amount = 0.01


tx = {

    'nonce': w3.eth.get_transaction_count(sender_address),
    'chainId': w3.eth.chain_id,
    'to': recipient_address,
    'value': w3.toWei(amount,'ether'),
    'gasPrice':w3.eth.gas_price,
    'gas': 21000,

}
# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(tx, private_key)

# Send the transaction
txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

# Wait for receipt and check the status
txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
print(f"Transaction successful with hash: {txn_hash.hex()}")
print(f"Transaction receipt: {txn_receipt}")
