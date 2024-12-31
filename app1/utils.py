from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_contact_email(contact_data):
    """
    Send email notification for contact form submission
    """
    subject = f"New Contact Form Submission - {contact_data['subject']}"
    message = render_to_string('app1/email_template.txt', {
        'name': contact_data['name'],
        'email': contact_data['email'],
        'subject': contact_data['subject'],
        'message': contact_data['message'],
    })
    
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['muhammedashique8281@gmail.com'],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Email error: {str(e)}")
        return False