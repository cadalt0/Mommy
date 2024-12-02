import requests

class SuiModule:
    def __init__(self, rpc_url):
        """
        Initialize the module with the Sui RPC URL.
        :param rpc_url: The URL of the Sui RPC endpoint.
        """
        self.rpc_url = rpc_url

    def get_object_info(self, object_id):
        """
        Fetches object details for a given object ID.
        :param object_id: The ID of the Sui object.
        :return: Object details as a dictionary or an error message.
        """
        endpoint = f"{self.rpc_url}/getObject"
        payload = {"object_id": object_id}
        response = requests.post(endpoint, json=payload)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch object info: {response.status_code}"}

    def get_account_info(self, address):
        """
        Fetches account information for a given Sui address.
        :param address: The Sui account address.
        :return: Account information as a dictionary or an error message.
        """
        endpoint = f"{self.rpc_url}/getAddressInfo"
        payload = {"address": address}
        response = requests.post(endpoint, json=payload)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch account info: {response.status_code}"}

    def get_latest_checkpoint(self):
        """
        Fetches the latest checkpoint information on the Sui blockchain.
        :return: Latest checkpoint info as a dictionary or an error message.
        """
        endpoint = f"{self.rpc_url}/getLatestCheckpoint"
        response = requests.post(endpoint, json={})
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch latest checkpoint info: {response.status_code}"}

    def get_transaction(self, transaction_digest):
        """
        Fetches transaction details for a given transaction digest.
        :param transaction_digest: The transaction digest.
        :return: Transaction details as a dictionary or an error message.
        """
        endpoint = f"{self.rpc_url}/getTransaction"
        payload = {"transaction_digest": transaction_digest}
        response = requests.post(endpoint, json=payload)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch transaction info: {response.status_code}"}


# Example Usage:
if __name__ == "__main__":
    # Replace with your Sui RPC URL
    sui_rpc_url = "https://fullnode.mainnet.sui.io"
    sui = SuiModule(sui_rpc_url)

    # Example inputs
    test_address = "0x123456789abcdef"
    test_object_id = "0xabcdef123456789"
    test_transaction_digest = "0x987654321fedcba"

    # Fetch and display object info
    object_info = sui.get_object_info(test_object_id)
    print("Object Info:", object_info)

    # Fetch and display account info
    account_info = sui.get_account_info(test_address)
    print("Account Info:", account_info)

    # Fetch and display latest checkpoint info
    checkpoint_info = sui.get_latest_checkpoint()
    print("Latest Checkpoint Info:", checkpoint_info)

    # Fetch and display transaction info
    transaction_info = sui.get_transaction(test_transaction_digest)
    print("Transaction Info:", transaction_info)
