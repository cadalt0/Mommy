import requests

class EthereumModule:
    def __init__(self, rpc_url):
        self.rpc_url = rpc_url

    def get_block(self, block_number):
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBlockByNumber",
            "params": [hex(block_number), True],
            "id": 1
        }
        response = requests.post(self.rpc_url, json=payload)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch block info: {response.status_code}"}

    def get_transaction(self, tx_hash):
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getTransactionByHash",
            "params": [tx_hash],
            "id": 1
        }
        response = requests.post(self.rpc_url, json=payload)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch transaction info: {response.status_code}"}


# Example Usage:
if __name__ == "__main__":
    eth_rpc_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
    eth = EthereumModule(eth_rpc_url)

    print(eth.get_block(12345678))
    print(eth.get_transaction("0x1234..."))
