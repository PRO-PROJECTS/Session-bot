from StringSessionBot.database.users_sql import Users, num_users
from StringSessionBot.database import SESSION
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.user(1669178360) & ~filters.edited & filters.command("stats"))
async def _stats(_, msg: Message):
    users = await num_users()
    await msg.reply(f"Total Users : {users}", quote=True)
