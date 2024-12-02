import requests

class NethermindModule:
    def __init__(self, rpc_url):
        """
        Initialize the module with the Nethermind RPC URL.
        :param rpc_url: The URL of the Nethermind RPC endpoint.
        """
        self.rpc_url = rpc_url

    def send_rpc_request(self, method, params=None):
        """
        Sends a generic RPC request to Nethermind.
        :param method: The JSON-RPC method to call.
        :param params: The parameters for the method.
        :return: Response from the RPC call.
        """
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": 1
        }
        response = requests.post(self.rpc_url, json=payload)
        if response.status_code == 200:
            return response.json()
        return {"error": f"RPC request failed: {response.status_code}"}

    def get_block_number(self):
        """
        Fetches the latest block number.
        :return: The latest block number or error message.
        """
        return self.send_rpc_request("eth_blockNumber")

    def get_block_by_number(self, block_number):
        """
        Fetches a block by its number.
        :param block_number: The block number (integer).
        :return: Block details or error message.
        """
        hex_block_number = hex(block_number)
        return self.send_rpc_request("eth_getBlockByNumber", [hex_block_number, True])

    def get_transaction_by_hash(self, tx_hash):
        """
        Fetches transaction details by hash.
        :param tx_hash: The transaction hash.
        :return: Transaction details or error message.
        """
        return self.send_rpc_request("eth_getTransactionByHash", [tx_hash])

    def get_balance(self, address):
        """
        Fetches the balance of an address.
        :param address: The Ethereum address.
        :return: Balance in Wei or error message.
        """
        return self.send_rpc_request("eth_getBalance", [address, "latest"])


# Example Usage:
if __name__ == "__main__":
    # Replace with your Nethermind RPC URL
    nethermind_rpc_url = "http://127.0.0.1:8545"  # Example for local node
    nethermind = NethermindModule(nethermind_rpc_url)

    # Get the latest block number
    block_number = nethermind.get_block_number()
    print("Latest Block Number:", block_number)

    # Fetch a block by number
    block_info = nether
