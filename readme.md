# AI Agents for Blockchain Tracking and Rewards System

This project integrates **AI agents** to monitor, track, and engage users across multiple blockchain networks. It allows for decentralized reward distribution, transaction tracking, content moderation, and cross-chain interactions. By using smart contracts, AI agents can automate user activities and enhance decentralized applications (DApps). This project enables a robust user engagement and reward system across ecosystems like **Solana**, **Ethereum**, **Aptos**, **Avalanche**, and **Sui**.

The project is designed to be scalable, utilizing various blockchain protocols, smart contracts, and real-time data processing to offer enhanced user experiences and reward systems for decentralized applications.

---

## Features

- **AI-Powered Blockchain Activity Tracking**: Monitors and analyzes user activities across multiple blockchain networks.
- **Decentralized Reward Distribution**: Distributes rewards to users in their wallets based on their interaction with supported blockchain ecosystems.
- **Cross-Chain Data Flow**: Supports multiple blockchains for seamless interaction, ensuring that users are rewarded for their activities across platforms.
- **AI Chatbot for User Engagement**: Uses AI to respond to user queries, manage user interaction, and assist with reward-related information.
- **Content Moderation**: AI agents are designed to moderate content, ensuring compliance with community guidelines in decentralized ecosystems.
- **Smart Contract Integration**: All reward management, user interaction, and activity tracking are handled through decentralized smart contracts.
- **Real-Time Transaction Monitoring**: Tracks transactions across blockchain ecosystems, providing up-to-date insights for users.

---

## Technologies Used

- **Python**: The main programming language for the backend.
- **Web3.py**: Used to interact with Ethereum and other compatible blockchains.
- **Solana Python SDK**: For Solana blockchain interaction.
- **Aptos SDK**: For interacting with Aptos blockchain.
- **Avalanche SDK**: For interacting with the Avalanche blockchain.
- **Sui SDK**: For interacting with the Sui blockchain.
- **Google Generative AI (Gemini)**: To enhance content moderation and provide AI-powered chatbot interactions.
- **Twitter API**: For integrating Twitter functionalities like fetching posts and user activities.
- **Smart Contracts**: Deployed on Ethereum, Solana, and other blockchains to handle reward distribution and user management.
- **Decentralized File Storage**: For storing user data and logs in a decentralized manner (e.g., IPFS).
- **Router Protocol**: Used for cross-chain interactions between different blockchain networks.

---


### 1. Blockchain API Keys
The project requires API keys for interaction with different blockchain networks. Please obtain the required keys from the respective providers.

- **Solana**: Create a wallet and get the API key from Solana's network.
- **Aptos**: Obtain your API key from the Aptos network.
- **Ethereum**: Use Infura or Alchemy to get an Ethereum API key.
- **Sui**: Get the API key for the Sui blockchain.

### 2. Set API Keys in `config.py`

Add the obtained API keys to the `config.py` file:

```python
SOLANA_API_KEY = "your_solana_api_key"
APTOS_API_KEY = "your_aptos_api_key"
ETHEREUM_API_KEY = "your_ethereum_api_key"
SUI_API_KEY = "your_sui_api_key"
```

### 3. Set Up Blockchain Networks
Configure the blockchain networks you wish to interact with in the `config.py` file:

```python
BLOCKCHAIN_NETWORKS = ["Solana", "Ethereum", "Aptos", "Avalanche", "Sui"]
```

### 4. Smart Contract Configuration
Add the addresses for the deployed smart contracts and configure reward parameters:

```python
SMART_CONTRACTS = {
    "solana": "your_solana_contract_address",
    "ethereum": "your_ethereum_contract_address",
    "aptos": "your_aptos_contract_address",
    "avalanche": "your_avalanche_contract_address",
    "sui": "your_sui_contract_address"
}

REWARD_SYSTEM = {
    "transaction_rewards": 10,
    "staking_rewards": 20,
    "activity_rewards": 5
}
```

---

## Key Functionalities

### 1. **Blockchain RPC Methods**
Each blockchain interaction, whether it’s to fetch transaction details, track balances, or query smart contracts, is handled using blockchain-specific RPC methods.

#### Example - Solana RPC:
```python
from solana.rpc.api import Client

solana_client = Client("https://api.mainnet-beta.solana.com")
transaction = solana_client.get_transaction(transaction_signature)
```

#### Example - Ethereum RPC using Web3.py:
```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))
transaction = w3.eth.getTransaction(transaction_hash)
```

---

### 2. **AI-Powered User Interaction**
The **AI chatbot** is integrated using Google Generative AI (Gemini), which enables personalized user interaction, content moderation, and reward query handling.

#### Example - AI Content Moderation and Chatbot:
```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

def get_ai_response(query):
    response = model.generate_content(query)
    return response.text
```

### 3. **Twitter Integration**
The project includes integration with the Twitter API to track user engagement and facilitate airdrop participation through social media interactions.

#### Example - Fetching Tweets:
```python
import tweepy

client = tweepy.Client(bearer_token='your_bearer_token')

tweets = client.search_recent_tweets(query='#AI', max_results=10)
```

### 4. **Cross-Chain Rewards Distribution**
Rewards are distributed based on user activity across different blockchain networks. The AI agents monitor activity on each chain and trigger rewards when certain conditions are met.

#### Example - Reward Distribution on Ethereum:
```python
from web3 import Web3

def distribute_rewards(user_address, amount):
    contract = w3.eth.contract(address=SMART_CONTRACTS['ethereum'], abi=contract_abi)
    tx = contract.functions.distributeRewards(user_address, amount).transact({'from': admin_address})
    return tx
```

---

## Usage

### Running the AI Agent

Start the AI agent to begin tracking user activities and rewarding them on multiple blockchains:

```bash
python main.py
```

### Engaging with the AI Chatbot

Users can interact with the AI chatbot by querying about their rewards, transaction statuses, and blockchain activities. The chatbot leverages the Google Gemini AI to respond intelligently to user queries.

### Cross-Chain Data Sync and Reward Distribution

The AI agents monitor activities across Solana, Ethereum, Aptos, and other chains. Based on the user's engagement, rewards are distributed via smart contracts on each blockchain.

---

## Roadmap

- **Phase 1**: Initial integration with Solana, Ethereum, and Aptos blockchains.
- **Phase 2**: Expand to more blockchains (e.g., Avalanche, Binance Smart Chain, Sui).
- **Phase 3**: Enhance AI capabilities to personalize rewards and user interactions.
- **Phase 4**: Cross-chain data synchronization and airdrop automation via social media platforms.

---



---


