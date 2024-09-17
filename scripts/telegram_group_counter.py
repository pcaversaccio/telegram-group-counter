import os, asyncio
from dotenv import load_dotenv
from telethon import TelegramClient


load_dotenv()


async def main():
    async with TelegramClient(
        "session", os.getenv("API_ID"), os.getenv("API_HASH")
    ) as client:
        await client.start(phone=os.getenv("PHONE_NUMBER"))
        # Fetch all dialogs (chats and channels) for the user.
        dialogs = await client.get_dialogs()
        # Count the number of groups.
        group_count = sum(dialog.is_group for dialog in dialogs)
        print(f"You are in {group_count} Telegram groups.")


asyncio.run(main())
