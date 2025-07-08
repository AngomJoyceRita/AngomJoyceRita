import asyncio
from telegram import Bot
from telegram.constants import ParseMode
import telegram.error

BOT_TOKEN = "8148430295:AAEAmHOseF6Qga6sDpO5ergkqGx_wSiV68k"
CHAT_ID = "-4851177982" 

async def post_to_telegram(text_content):

    if not text_content:
        print("Error: Text cannot be empty.")
        return

    print("Posting ...")

    try:
        # Create bot instance
        bot = Bot(token=BOT_TOKEN)

        # Send the message 
        await bot.send_message(
            chat_id=CHAT_ID,
            text=text_content,
            parse_mode=ParseMode.MARKDOWN
        )

        print("Successfully posted!!!")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    except telegram.error.TelegramError as e:
        print(f"❌ Telegram API error: {e}")
    

if __name__ == "__main__":
    # Define your post content

    my_post = input("Hello from my  bot! 🤖\n \033[92mEnter a message: \033[0m")
    
    # Run the async function
    asyncio.run(post_to_telegram(my_post))
