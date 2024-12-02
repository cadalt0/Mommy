import discord
from discord.ext import commands
import google.generativeai as genai
from web3 import Web3

# Configure Gemini AI
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Web3
web3 = Web3(Web3.HTTPProvider("https://your_rpc_url"))  # Replace with your provider
contract_address = "YOUR_CONTRACT_ADDRESS"  # Replace with your contract address
abi = []  # Replace with your contract ABI
contract = web3.eth.contract(address=contract_address, abi=abi)

# Initialize bot
# Configure bot intents
intents = discord.Intents.all()
intents.messages = True
intents.guilds = True
intents.members = True



# Track channels to watch
watched_channels = set()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="watch")
@commands.has_permissions(administrator=True)
async def watch_channel(ctx):
    """Start watching the current channel."""
    watched_channels.add(ctx.channel.id)
    await ctx.send(f"Watching this channel: {ctx.channel.mention}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id in watched_channels:
        # Generate a reply using Gemini AI
        try:
            response = model.generate_content(message.content)
            ai_reply = response.text

            # Log the conversation in Web3
            try:
                tx = contract.functions.logMessage(message.author.id, message.content, ai_reply).transact(
                    {'from': web3.eth.default_account}
                )
                web3.eth.wait_for_transaction_receipt(tx)
            except Exception as e:
                print(f"Web3 logging error: {e}")

            await message.channel.send(ai_reply)
        except Exception as e:
            print(f"Gemini AI error: {e}")
            await message.channel.send("Sorry, I couldn't generate a response.")

    await bot.process_commands(message)

async def load_cogs():
    try:
        # Load new cogs
        await bot.load_extension("okto_wallet")   # For Okto wallet functionality
        await bot.load_extension("x_com_oauth_and_upload")  # For X.com OAuth and uploading data
        await bot.load_extension("aptos_rpc")  # For Aptos RPC interaction
        await bot.load_extension("sui_rpc")  # For SUI RPC interaction
        await bot.load_extension("ethereum_rpc")  # For Ethereum RPC interaction
        await bot.load_extension("solana_rpc")  # For Solana RPC interaction
        await bot.load_extension("avalanche_rpc")  # For Avalanche RPC interaction
        await bot.load_extension("neithermind_rpc")  # For Neithermind RPC interaction (Near Protocol)
        await bot.load_extension("collect_user_activity")  # For collecting user activity and uploading to decentralized DB
        await bot.load_extension("smart_contract_upload")  # For uploading to decentralized network via smart contract
        await bot.load_extension("x_com_reposts_points")  # For tracking X.com reposts and likes for points and uploading data

        logger.info("Cogs loaded successfully.")
    except Exception as e:
        logger.error(f"Failed to load cogs: {e}")


# Replace 'YOUR_DISCORD_TOKEN' with your bot's token
bot.run('YOUR_DISCORD_TOKEN')
