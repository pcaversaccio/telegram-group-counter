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
        # See: https://docs.telethon.dev/en/stable/modules/client.html#telethon.client.dialogs.DialogMethods.get_dialogs.
        dialogs = await client.get_dialogs()
        # Count the number of groups and megagroups.
        # See: https://docs.telethon.dev/en/stable/modules/custom.html#telethon.tl.custom.chatgetter.ChatGetter.is_group.
        group_count = sum(dialog.is_group for dialog in dialogs)
        # Count the number of broadcast channels.
        # See: https://docs.telethon.dev/en/stable/modules/custom.html#telethon.tl.custom.chatgetter.ChatGetter.is_channel.
        channel_count = sum(
            dialog.is_channel and not dialog.is_group for dialog in dialogs
        )
        print(
            f"You are in {group_count} Telegram groups and {channel_count} Telegram channels."
        )


asyncio.run(main())
