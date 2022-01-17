# by @CREATIVE_tg1
import logging
import requests
from .. import loader, utils

logger = logging.getLogger(__name__)

def register(cb):
    cb(TagAllMod())

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

class TagAllMod(loader.Module):

    strings = {"name":"TagAll"}

    def __init__(self):
        self.config = loader.ModuleConfig("DEFAULT_MENTION_MESSAGE", "Общий сбор.", "Default message of mentions")
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client

    async def tagall5cmd(self, message):
        """Тегает по 5 человек в одном сообщении."""
        arg = utils.get_args_raw(message)

        logger.error(message)
        notifies = []
        async for user in self.client.iter_participants(message.to_id):
            notifies.append("<a href=\"tg://user?id="+ str(user.id) +"\">\u206c\u206f</a>")
        chunkss = list(chunks(notifies, 5))
        logger.error(chunkss)
        await message.delete()
        for chunk in chunkss:
            await self.client.send_message(message.to_id, (self.config["DEFAULT_MENTION_MESSAGE"] if not arg else arg) + '\u206c\u206f'.join(chunk))
            
    async def tagall50cmd(self, message):
        """Тегает по 50 человек в одном сообщении."""
        arg = utils.get_args_raw(message)

        logger.error(message)
        notifies = []
        async for user in self.client.iter_participants(message.to_id):
            notifies.append("<a href=\"tg://user?id="+ str(user.id) +"\">\u206c\u206f</a>")
        chunkss = list(chunks(notifies, 50))
        logger.error(chunkss)
        await message.delete()
        for chunk in chunkss:
            await self.client.send_message(message.to_id, (self.config["DEFAULT_MENTION_MESSAGE"] if not arg else arg) + '\u206c\u206f'.join(chunk))
            
    async def tagall100cmd(self, message):
        """Тегает по 100 человек в одном сообщении."""
        arg = utils.get_args_raw(message)

        logger.error(message)
        notifies = []
        async for user in self.client.iter_participants(message.to_id):
            notifies.append("<a href=\"tg://user?id="+ str(user.id) +"\">\u206c\u206f</a>")
        chunkss = list(chunks(notifies, 100))
        logger.error(chunkss)
        await message.delete()
        for chunk in chunkss:
            await self.client.send_message(message.to_id, (self.config["DEFAULT_MENTION_MESSAGE"] if not arg else arg) + '\u206c\u206f'.join(chunk))
            
    async def tagall500cmd(self, message):
        """Тегает по 500 человек в одном сообщении."""
        arg = utils.get_args_raw(message)

        logger.error(message)
        notifies = []
        async for user in self.client.iter_participants(message.to_id):
            notifies.append("<a href=\"tg://user?id="+ str(user.id) +"\">\u206c\u206f</a>")
        chunkss = list(chunks(notifies, 500))
        logger.error(chunkss)
        await message.delete()
        for chunk in chunkss:
            await self.client.send_message(message.to_id, (self.config["DEFAULT_MENTION_MESSAGE"] if not arg else arg) + '\u206c\u206f'.join(chunk))
          
    async def tagall1000cmd(self, message):
        """Тегает по 1000 человек в одном сообщении."""
        arg = utils.get_args_raw(message)

        logger.error(message)
        notifies = []
        async for user in self.client.iter_participants(message.to_id):
            notifies.append("<a href=\"tg://user?id="+ str(user.id) +"\">\u206c\u206f</a>")
        chunkss = list(chunks(notifies, 1000))
        logger.error(chunkss)
        await message.delete()
        for chunk in chunkss:
            await self.client.send_message(message.to_id, (self.config["DEFAULT_MENTION_MESSAGE"] if not arg else arg) + '\u206c\u206f'.join(chunk))
