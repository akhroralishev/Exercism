async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Tugmani bosganda loadingni yo‘qotish uchun

    user_id = query.from_user.id

    # Kanalga obuna bo'lganmi tekshiramiz
    if not await check_subscription(user_id, context):
        await context.bot.send_message(
            chat_id=user_id,
            text="❗️ Siz kanalga obuna bo'lmagansiz. Iltimos, avval kanalga obuna bo'ling."
        )
        await context.bot.send_message(
            chat_id=user_id,
            text=f"🔗 Kanalga obuna bo'lish uchun: [Kanalga o'tish](https://t.me/{CHANNEL_USERNAME})",
            parse_mode="Markdown"
        )
        return

    # Foydalanuvchi javobini tekshirish
    if query.data == "correct":
        await context.bot.send_message(chat_id=user_id, text="✅ To‘g‘ri javob! 🎉")
    else:
        await context.bot.send_message(chat_id=user_id, text="❌ Noto‘g‘ri javob. 😔 To‘g‘ri javob: A")
