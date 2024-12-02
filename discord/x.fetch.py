import os
import requests
from web3 import Web3
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import WebApplicationClient

# Load environment variables
load_dotenv()

# X.com OAuth2 settings
CLIENT_ID = os.getenv("X_CLIENT_ID")
CLIENT_SECRET = os.getenv("X_CLIENT_SECRET")
REDIRECT_URI = os.getenv("X_REDIRECT_URI")
AUTHORIZATION_URL = "https://api.x.com/oauth2/authorize"
TOKEN_URL = "https://api.x.com/oauth2/token"
USER_INFO_URL = "https://api.x.com/2/me"
POSTS_URL = "https://api.x.com/2/timeline/home"

# Smart contract settings (Ethereum)
ETH_RPC_URL = os.getenv("ETH_RPC_URL")
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS")
CONTRACT_ABI = [...]  # Replace with your contract ABI
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))
contract = web3.eth.contract(address=Web3.toChecksumAddress(CONTRACT_ADDRESS), abi=CONTRACT_ABI)

# Initialize OAuth2 Client
client = WebApplicationClient(CLIENT_ID)

def get_oauth_session():
    """
    Initialize OAuth2 session for user authorization.
    """
    oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_URL)
    print(f"Please go to {authorization_url} and authorize the application.")
    return oauth

def get_access_token(oauth, authorization_response):
    """
    Retrieve the access token using the authorization response.
    """
    token = oauth.fetch_token(
        TOKEN_URL,
        authorization_response=authorization_response,
        client_secret=CLIENT_SECRET,
    )
    return token

def fetch_user_info(oauth):
    """
    Fetch user details from X.com API after obtaining the access token.
    """
    response = oauth.get(USER_INFO_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch user information")

def fetch_user_posts(oauth):
    """
    Fetch posts (tweets) of the authenticated user from X.com API.
    """
    response = oauth.get(POSTS_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch posts")

def check_user_interactions(posts):
    """
    Check if the user liked or reposted (retweeted) any posts.
    Return the number of interactions (points).
    """
    points = 0
    for post in posts['data']:
        if post.get('liked') or post.get('retweeted'):
            points += 1
    return points

def upload_data_to_smart_contract(points, user_id):
    """
    Upload user points to a smart contract on Ethereum.
    """
    # Create the transaction to store data on the blockchain
    tx = contract.functions.storeUserPoints(user_id, points).build_transaction({
        'from': SENDER_ADDRESS,
        'nonce': web3.eth.get_transaction_count(SENDER_ADDRESS),
        'gas': 3000000,
        'gasPrice': web3.toWei('20', 'gwei')
    })
    signed_tx = web3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return web3.eth.wait_for_transaction_receipt(tx_hash)

def main():
    """
    Main function to handle user authentication, fetch posts, calculate points,
    and upload data to the smart contract.
    """
    # Step 1: Initialize OAuth session and ask user to authorize
    oauth = get_oauth_session()
    
    # Step 2: Get the authorization response (Redirect URL with code)
    authorization_response = input("Paste the full redirect URL here: ")
    
    # Step 3: Get access token
    token = get_access_token(oauth, authorization_response)
    
    # Step 4: Fetch user info and posts
    user_info = fetch_user_info(oauth)
    posts = fetch_user_posts(oauth)
    
    # Step 5: Calculate points based on user interactions (likes/retweets)
    user_id = user_info['id']  # Use user ID from X.com
    points = check_user_interactions(posts)
    
    print(f"User {user_id} has earned {points} points based on interactions.")
    
    # Step 6: Upload data to the smart contract (Decentralized)
    tx_receipt = upload_data_to_smart_contract(points, user_id)
    print(f"Data uploaded successfully! Transaction receipt: {tx_receipt}")

if __name__ == "__main__":
    main()
