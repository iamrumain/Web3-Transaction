from web3 import Web3, HTTPProvider


# rpc url
rpc = ''
w3 = Web3(HTTPProvider(rpc))

# Enter private key and address
pk = '0x123465798'
address = '0x123465798'


# to address
to_address = ''



balance = 0.01



tx = {
    
    'nonce': w3.eth.get_transaction_count(address),
    'chainId': w3.eth.chain_id,
    'to': address,
    'value': w3.toWei(balance,'ether'),
    'gasPrice':w3.eth.gas_price,
    'gas': 21000,

}
signed_tx = w3.eth.account.sign_transaction(tx, pk)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
hash_xd = w3.toHex(tx_hash)
print(f'Transaction : {hash_xd}')
