
from pyrogram import Client, filters
from database.users_chats_db import db

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("🥲𝚂𝚘𝚛𝚛𝚢! 𝙽𝚘 𝚃𝚑𝚞𝚖𝚙𝚗𝚊𝚒𝚕 𝙵𝚘𝚞𝚗𝚍...🥲") 
		
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("𝚃𝚑𝚞𝚖𝚙𝚗𝚊𝚒𝚕 𝙳𝚎𝚕𝚎𝚝𝚎𝚍 𝚂𝚞𝚌𝚌𝚎𝚜𝚏𝚞𝚕𝚕𝚢✅️")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    LazyDev = await message.reply_text("Please Wait ...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await LazyDev.edit("𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚂𝚊𝚟𝚎𝚍 𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢✅️")
	
