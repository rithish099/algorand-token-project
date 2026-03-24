from algosdk import account, mnemonic

# Generate new account
private_key, address = account.generate_account()

print("New Account Address:", address)
print("Private Key:", private_key)