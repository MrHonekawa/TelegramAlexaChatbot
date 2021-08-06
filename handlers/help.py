from telegram.ext import CommandHandler


def help(update, context):
    update.effective_message.reply_text(
        "Hey there,.\nI am an AI ChatBot, Developed with love for interacting with users! \nI am developed for having chats but not on private \nFor Activation of my AI you must add me on group and type /start@AlexaChatRoBot & Done \nFrom then i can talk with you all in groups!!"
    )


__handlers__ = [
    [
        CommandHandler(
            "start",
            help
        )
    ]
]
