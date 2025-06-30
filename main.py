# --- START OF FILE main.py ---
import asyncio
from pytgcalls import idle
import os
import sys
import random
import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls
from bot import start_zombiebot
from pyromod import listen

loop = asyncio.get_event_loop()

if __name__ == "__main__":
    try:
        loop.run_until_complete(start_zombiebot())
    except KeyboardInterrupt:
        print("Bot stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
# --- END OF FILE main.py ---