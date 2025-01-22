from django.db.models.signals import post_save
from django.dispatch import Signal
from django.dispatch import receiver
from apps.authentication.models import UserMaster
from apps.authentication.models.otp_master import OtpMaster
from apps.helpers.random_otp_generator import generate_random_otp
from django.core.mail import send_mail
from django.conf import settings


# create a profile after a user is created
@receiver(post_save, sender=UserMaster)
def save_profile(sender, instance, created, **kwargs):
    if created:
        final_data = {"user": instance, "otp": generate_random_otp(length=6)}
        OtpMaster.objects.create(**final_data)


@receiver(post_save, sender=OtpMaster)
def save_profile(sender, instance, created, **kwargs):
    if created:
        try:
            subject = "OTP Verification Code"
            message = f"Hello {instance.user.name},\n\n welcome to Task management app\n\nYour OTP for verification is: {instance.otp}\n\nThank you!"
            recipient_list = [instance.user.email]

            # Send email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # from_email,
                recipient_list,
            )
        except:
            return "Couldn't send email"
