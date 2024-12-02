import requests

class SolanaModule:
    def __init__(self, rpc_url):
        self.rpc_url = rpc_url

    def get_account_info(self, pubkey):
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [pubkey]
        }
        response = requests.post(self.rpc_url, json=payload)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch account info: {response.status_code}"}

    def get_block(self, slot):
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBlock",
            "params": [slot]
        }
        response = requests.post(self.rpc_url, json=payload)
        if response.status_code == 200:
            return response.json()
        return {"error": f"Failed to fetch block info: {response.status_code}"}


# Example Usage:
if __name__ == "__main__":
    sol_rpc_url = "https://api.mainnet-beta.solana.com"
    solana = SolanaModule(sol_rpc_url)

    print(solana.get_account_info("YourPubkey"))
    print(solana.get_block(12345678))
