from celery import shared_task
from django.core.mail import send_mail
from .models import EmailMessage
from django.conf import settings
import telegram

bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)

@shared_task
def send_daily_email():
    users = EmailMessage.objects.all()
    count = 0
    for user in users:

        send_mail(
            subject="celery",
            message="assalom",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        count += 1
    bot.send_message(
        chat_id=settings.TELEGRAM_CHAT_ID,
        text=f"{count} message jonatildi"
    )

    return f"{count} tg uchun habar"