import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message

API_TOKEN = "7848410546:AAFMkxIz0QT6N2lSzm52ToVFDuYUInggXvM"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


lybrary_books = [
        {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "inventory": 3},
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "inventory": 0},
    ]

async def search_books_by_title(title: str) -> list[dict]:
    for book in lybrary_books:
        if title.lower() in book["title"].lower():
            yield book
        else:
            continue


@dp.message(Command(commands=["start"]))
async def start_handler(message: Message):
    await message.reply("Hello! This is a library bot. Type /help to see available commands.")


@dp.message(Command(commands=["help"]))
async def help_handler(message: Message):
    await message.reply(
        "Commands:\n"
        "/search [book title] - Search for a book\n"
        "/borrow [book ID] - Borrow a book\n"
    )


@dp.message(Command(commands=["search"]))
async def search_handler(message: Message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await message.reply("Please specify a book title. Example: /search The Great Gatsby")
        return

    title = args[1]
    books = search_books_by_title(title)

    found_books = []
    async for book in books:
        found_books.append(book)

    if not found_books:
        await message.reply("Unfortunately, no books were found with this title.")
    else:
        reply = "Here are the books found:\n"
        for book in found_books:
            status = "Available" if book["inventory"] > 0 else "Unavailable"
            reply += f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Status: {status}\n"
        await message.reply(reply)



@dp.message(Command(commands=["borrow"]))
async def borrow_handler(message: Message):
    args = message.text.split(maxsplit=1)

    if len(args) < 2 or not args[1].isdigit():
        await message.reply("Please specify a book ID. Example: /borrow 1")
        return

    book_id = int(args[1])
    await message.reply(f"Book with ID {book_id} successfully borrowed!")


async def main():
    logging.info("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
