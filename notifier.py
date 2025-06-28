import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Update these credentials
EMAIL_SENDER = "your_email_address"
EMAIL_PASSWORD = "email_password"
EMAIL_RECEIVER = "reciever_email_address"  # Could also accept this per user

# Send reminder email
def send_email(event):
    subject = f"⏰ Reminder: {event['title']}"
    body = f"""
    <h2>Event Reminder</h2>
    <p><strong>Title:</strong> {event['title']}</p>
    <p><strong>Description:</strong> {event['description']}</p>
    <p><strong>Starts At:</strong> {event['start_time']}</p>
    <p><strong>Ends At:</strong> {event['end_time']}</p>
    """

    # Email formatting
    message = MIMEMultipart()
    message['From'] = EMAIL_SENDER
    message['To'] = EMAIL_RECEIVER
    message['Subject'] = subject
    message.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message.as_string())
        server.quit()
        print(f"✅ Email sent for event '{event['title']}'")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
