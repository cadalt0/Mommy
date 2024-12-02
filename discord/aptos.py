import requests

class AptosModule:
    def __init__(self, rpc_url):
        """
        Initialize the module with the Aptos RPC URL.
        :param rpc_url: The URL of the Aptos RPC endpoint.
        """
        self.rpc_url = rpc_url

    def get_account_info(self, address):
        """
        Fetches account information for a given Aptos address.
        :param address: The Aptos account address.
        :return: Account information as a dictionary or an error message.
        """
        endpoint = f"{self.rpc_url}/accounts/{address}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch account info: {response.status_code}"}

    def get_transaction(self, transaction_hash):
        """
        Fetches transaction details for a given transaction hash.
        :param transaction_hash: The transaction hash.
        :return: Transaction details as a dictionary or an error message.
        """
        endpoint = f"{self.rpc_url}/transactions/by_hash/{transaction_hash}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch transaction: {response.status_code}"}

    def get_latest_ledger_info(self):
        """
        Fetches the latest ledger information from the Aptos blockchain.
        :return: Latest ledger info as a dictionary or an error message.
        """
        endpoint = f"{self.rpc_url}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch latest ledger info: {response.status_code}"}

    def get_account_resources(self, address):
        """
        Fetches all resources for a given account.
        :param address: The Aptos account address.
        :return: Account resources as a dictionary or an error message.
        """
        endpoint = f"{self.rpc_url}/accounts/{address}/resources"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch account resources: {response.status_code}"}


# Example Usage:
if __name__ == "__main__":
    # Replace with your Aptos RPC URL
    aptos_rpc_url = "https://fullnode.devnet.aptoslabs.com/v1"
    aptos = AptosModule(aptos_rpc_url)

    # Example address and transaction hash
    test_address = "0x1"
    test_transaction_hash = "0x2"

    # Fetch and display account info
    account_info = aptos.get_account_info(test_address)
    print("Account Info:", account_info)

    # Fetch and display transaction details
    transaction_info = aptos.get_transaction(test_transaction_hash)
    print("Transaction Info:", transaction_info)

    # Fetch and display the latest ledger info
    ledger_info = aptos.get_latest_ledger_info()
    print("Latest Ledger Info:", ledger_info)

    # Fetch and display account resources
    account_resources = aptos.get_account_resources(test_address)
    print("Account Resources:", account_resources)
