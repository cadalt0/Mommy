import datetime
import json
import random
from web3 import Web3
import ipfshttpclient

# Mock data for user activity
USER_ACTIVITY = [
    {"user_id": f"user_{i}", "last_active": datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 60))}
    for i in range(1, 101)
]

class DecentralizedUserUploader:
    def __init__(self, rpc_url, contract_address, contract_abi, ipfs_url="/ip4/127.0.0.1/tcp/5001"):
        """
        Initializes the uploader with Ethereum and IPFS details.
        :param rpc_url: Ethereum node RPC URL.
        :param contract_address: Address of the smart contract.
        :param contract_abi: ABI of the smart contract.
        :param ipfs_url: URL for the IPFS client.
        """
        self.web3 = Web3(Web3.HTTPProvider(rpc_url))
        self.contract = self.web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)
        self.ipfs = ipfshttpclient.connect(ipfs_url)

    def collect_active_users(self, days):
        """
        Filters users active within the last `days` days.
        :param days: Number of days to consider for activity.
        :return: List of active user IDs.
        """
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
        return [user["user_id"] for user in USER_ACTIVITY if user["last_active"] >= cutoff_date]

    def upload_to_ipfs(self, data):
        """
        Uploads data to IPFS.
        :param data: Data to upload.
        :return: IPFS hash.
        """
        json_data = json.dumps(data)
        result = self.ipfs.add_str(json_data)
        return result

    def upload_to_smart_contract(self, ipfs_hash, sender_address, private_key):
        """
        Calls the smart contract to upload metadata.
        :param ipfs_hash: IPFS hash of the uploaded data.
        :param sender_address: Ethereum address of the sender.
        :param private_key: Private key of the sender.
        :return: Transaction receipt.
        """
        tx = self.contract.functions.storeData(ipfs_hash).build_transaction({
            'from': sender_address,
            'nonce': self.web3.eth.get_transaction_count(sender_address),
            'gas': 3000000,
            'gasPrice': self.web3.to_wei('20', 'gwei')
        })

        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(tx_hash)


# Example Usage
if __name__ == "__main__":
    # Configuration
    ETH_RPC_URL = "https://mainnet.infura.io/v3/YOUR_PROJECT_ID"  # Replace with your RPC URL
    CONTRACT_ADDRESS = "0xYourSmartContractAddress"
    CONTRACT_ABI = [...]  # Replace with your contract ABI
    SENDER_ADDRESS = "0xYourWalletAddress"
    PRIVATE_KEY = "YourPrivateKey"

    uploader = DecentralizedUserUploader(ETH_RPC_URL, CONTRACT_ADDRESS, CONTRACT_ABI)

    # Collect last day's active users
    active_users_day = uploader.collect_active_users(days=1)
    print(f"Active users in the last day: {active_users_day}")

    # Collect last month's active users
    active_users_month = uploader.collect_active_users(days=30)
    print(f"Active users in the last month: {active_users_month}")

    # Upload to IPFS
    ipfs_hash = uploader.upload_to_ipfs({"last_day": active_users_day, "last_month": active_users_month})
    print(f"Data uploaded to IPFS with hash: {ipfs_hash}")

    # Upload IPFS hash to smart contract
    tx_receipt = uploader.upload_to_smart_contract(ipfs_hash, SENDER_ADDRESS, PRIVATE_KEY)
    print(f"Smart contract transaction successful: {tx_receipt}")
