import os

import telebot



TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if not TOKEN:
  
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not configured")
  


bot = telebot.TeleBot(TOKEN, parse_mode="HTML")



@bot.message_handler(commands=["start"])

def start(message):
  
    bot.reply_to(
      
        message,
      
        "မင်္ဂလာပါ။ Bot အလုပ်လုပ်နေပါပြီ။\n\n"
      
        "စာတစ်ု ပို့ကြည့်ပါ—ပြန်စာပေးပါမယ်။\n"
      
        "/help ကိုလည်း အသုံးပြုနိုင်ပါတယ်။",
      
    )
  


@bot.message_handler(commands=["help"])

def help_message(message):
  
    bot.reply_to(
      
        message,
      
        "အသုံးပြုနိုင်သော command များ:\n"
      
        "/start — Bot စတင်ရန်\n"
      
        "/help — အကူအညီပြရန်",
      
    )
  


@bot.message_handler(content_types=["text"])

def echo(message):
  
    bot.reply_to(message, f"သင့်စာကို လက်ံရရှိပါတယ်။\n\n{message.text}")
  


if __name__ == "__main__":
  
    print("Safe Telegram reply bot is running", flush=True)
  
    bot.infinity_polling(skip_pending=True, timeout=20, long_polling_timeout=20)
  





















