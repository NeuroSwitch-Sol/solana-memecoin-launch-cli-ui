# Solana Memecoin Launch CLI UI

This application is a UI-based CLI (Command-Line Interface) chatbot designed to help you launch a memecoin on the Solana blockchain. It uses:

* The Rich library for colorful CLI output
* SolanaAgentKit for interacting with the Solana blockchain
* Pydantic-AI for AI-driven conversation and structured inputs
* OpenAIModel/Llama3.2(Groq) for powering AI responses

## Features

* Rich CLI: User-friendly, color-coded prompts and status spinners
* Token Launch: Easily configure token name, ticker, description, images, and liquidity options
* OpenAI Integration: Allows for sophisticated query processing and conversation

## Installation

1. Clone the repository (or copy the script below into a file):

```bash
git clone https://github.com/NeuroSwitch-Sol/solana-memecoin-launch-cli-ui.git
cd solana-memecoin-launch-cli-ui
```

Install dependencies
```bash
pip install -r requirements.txt
```

### Set up your API keys
Solana private key: Typically, a 64-character hex string or a base58-encoded string.

Helius RPC or other Solana RPC URL (e.g., https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY).

OpenAI API key or Groq API key(free).

### Option A: Hardcode credentials
Replace the placeholders in the script with your actual keys.

### Option B: Use environment variables
1. Remove the placeholders from the script.
2. Use something like:
```bash
import os

private_key = os.getenv("SOLANA_PRIVATE_KEY")
rpc_url = os.getenv("SOLANA_RPC_URL")
openai_api_key = os.getenv("OPENAI_API_KEY")
```
3. Then export them in your shell:
```bash
export SOLANA_PRIVATE_KEY="YOUR_PRIVATE_KEY"
export SOLANA_RPC_URL="https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY"
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

## Usage
Run the Application
```bash
python solana_memecoin_launcher.py

```
Follow the Prompts
- The CLI will ask you to enter your query.
- If you want to launch a token, provide information in the format required (examples below).
- Type exit to quit at any time.

### Example Query
```bash
Enter your query (type 'exit' to quit):: launch_token called MyMemeToken with a ticker='MMT' having description of A brand-new meme coin! and with image_url='https://example.com/image.png'
```

## Troubleshooting

Missing/Invalid API keys: Ensure all credentials are correct. If using environment variables, check that they are properly set.
Dependency errors: Reinstall or upgrade the package versions in requirements.txt.
Network issues: Verify your internet connection and confirm that the RPC URL is valid.

Enjoy launching your memecoins in Solana! If you have any issues, feel free to open an issue on GitHub and contact us in X/Discord.