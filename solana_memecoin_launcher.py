import asyncio
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from agentipy import SolanaAgentKit
from agentipy.types import PumpfunTokenOptions

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel

from pydantic import BaseModel
from pydantic_ai.models.groq import GroqModel

console = Console()

class CustomPumpfunTokenOptions(PumpfunTokenOptions):
    priority_fee: Optional[float] = None

class LaunchTokenInput(BaseModel):
    token_name: str
    token_ticker: str
    description: str
    image_url: str
    initial_liquidity_sol: Optional[float] = None
    priority_fee: Optional[float] = None
    twitter: Optional[str] = None
    telegram: Optional[str] = None
    website: Optional[str] = None
    slippage_bps: Optional[int] = None

async def launch_token_tool(ctx: RunContext, input: LaunchTokenInput) -> str:
    """
    Launches a Solana meme token using the provided input data.
    """
    # Replace the placeholders with your own keys or environment variables
    agent = SolanaAgentKit(
        private_key="<PRIVATE_KEY>",
        rpc_url="https://mainnet.helius-rpc.com/?api-key=<API_KEY>",
    )

    options = CustomPumpfunTokenOptions(
        twitter=input.twitter or "",
        telegram=input.telegram or "",
        website=input.website or "",
        initial_liquidity_sol=input.initial_liquidity_sol or 0.00001,
        slippage_bps=input.slippage_bps or 50,
        priority_fee=input.priority_fee or 0.0004
    )

    try:
        response = await agent.launch_pump_fun_token(
            token_name=input.token_name,
            token_ticker=input.token_ticker,
            description=input.description,
            image_url=input.image_url,
            options=options
        )
        return f"Token launched successfully: {response}"
    except Exception as e:
        return f"Failed to launch token: {e}"

# Initialize the AI model (replace with your OpenAI key)
model = OpenAIModel('gpt-4o-mini', api_key='API_KEY')
# model = GroqModel('llama-3.3-70b-versatile', api_key='API_KEY')

# Initialize the chat agent with a helpful system prompt
chat_agent = Agent(
    model=model,
    system_prompt=(
        "You are an assistant that interacts with the Solana blockchain. "
        "You can perform actions like checking token balances, fetching prices, and more. "
        "Use the provided tools to fetch and return accurate information."
    )
)

# Register the launch token function as a tool for the AI
@chat_agent.tool
async def launch_token(ctx: RunContext, input: LaunchTokenInput) -> str:
    """
    Launch a new token on the Solana blockchain with specific parameters.
    """
    return await launch_token_tool(ctx, input)

async def rich_main():
    """
    Main CLI loop.
    """
    console.print(Panel("[bold blue]Welcome to the Solana Meme Token Launch CLI Chatbot![/bold blue]"))

    while True:
        # Prompt user for a query
        user_query = Prompt.ask("[bold green]Enter your query (type 'exit' to quit):[/bold green]")
        
        if user_query.lower() == "exit":
            console.print("[bold yellow]Goodbye![/bold yellow]")
            break

        console.print("\n[bold cyan]Processing your request...[/bold cyan]")

        # Display a spinner while the AI processes the request
        with console.status("[bold green]Launching token based on your query...[/bold green]", spinner="dots"):
            try:
                # Send the query to the AI agent
                response = await chat_agent.run(user_query)

                # Ask the AI to reformat the response for user-friendliness
                reformatted_response = await chat_agent.run(
                    f"Format the following response in a user-friendly way:\n{response.data}"
                )

                # Show the reformatted response
                console.print(Panel(f"[bold green]Formatted Response:[/bold green]\n{reformatted_response.data}"))
            except Exception as e:
                console.print(Panel(f"[bold red]Error:[/bold red] {e}"))

if __name__ == "__main__":
    asyncio.run(rich_main())
