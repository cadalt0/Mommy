import random
import string

class OktoWallet:
    def __init__(self):
        self.wallets = {}

    def create_wallet(self, username):
        """
        Creates a wallet for a user.
        :param username: Unique username for the wallet.
        :return: Wallet address.
        """
        if username in self.wallets:
            return {"error": "Wallet already exists for this username."}
        
        wallet_address = self._generate_wallet_address()
        self.wallets[username] = {
            "address": wallet_address,
            "auth_method": None,
            "verified": False
        }
        return {"message": "Wallet created successfully!", "address": wallet_address}

    def set_auth_method(self, username, auth_method):
        """
        Set the authentication method for the user.
        :param username: The user's unique username.
        :param auth_method: 'google' or 'otp'.
        :return: Success or error message.
        """
        if username not in self.wallets:
            return {"error": "Wallet not found for this username."}
        
        if auth_method not in ["google", "otp"]:
            return {"error": "Invalid authentication method. Choose 'google' or 'otp'."}
        
        self.wallets[username]["auth_method"] = auth_method
        return {"message": f"Authentication method set to '{auth_method}' for {username}."}

    def verify_auth(self, username, code=None):
        """
        Verifies the user's authentication based on the selected method.
        :param username: The user's unique username.
        :param code: OTP code, required if using OTP authentication.
        :return: Success or error message.
        """
        if username not in self.wallets:
            return {"error": "Wallet not found for this username."}

        auth_method = self.wallets[username]["auth_method"]
        if auth_method is None:
            return {"error": "Authentication method not set."}

        if auth_method == "google":
            # Simulate Google Auth verification
            return {"message": "Google authentication successful!"}

        elif auth_method == "otp":
            if not code:
                return {"error": "OTP code required for verification."}
            # Simulate OTP verification
            if code == "123456":  # Replace with your OTP verification logic
                self.wallets[username]["verified"] = True
                return {"message": "OTP verification successful!"}
            else:
                return {"error": "Invalid OTP code."}

    def _generate_wallet_address(self):
        """
        Generates a random wallet address.
        :return: Wallet address.
        """
        return "0x" + ''.join(random.choices(string.hexdigits[:16], k=40))


# Example Usage:
if __name__ == "__main__":
    okto_wallet = OktoWallet()

    # Create a wallet
    result = okto_wallet.create_wallet("user123")
    print(result)

    # Set authentication method
    auth_result = okto_wallet.set_auth_method("user123", "otp")
    print(auth_result)

    # Verify authentication
    verify_result = okto_wallet.verify_auth("user123", code="123456")
    print(verify_result)
