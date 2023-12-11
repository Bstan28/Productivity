#! /usr/bin/python3
import smtplib
import ssl
import sys
from datetime import datetime

#Following crontab entry will run this script Monday through Friday from 8am to 4pm.
#0 8-16 * * 1-5 /path/to/script/Reminder-Text-Notification.py

# Map each day of the week to its corresponding topic
schedule = {
    'Monday': 'stretch',
    'Tuesday': 'pushups',
    'Wednesday': 'bodyweight squats',
    'Thursday': 'lunges',
    'Friday': 'stretch'
}

# Get the current day
current_day = datetime.now().strftime('%A')

# Check if it is a weekday and the day is in the schedule
if current_day in schedule:
    topic = schedule[current_day]
    message = f"Don't forget to do {topic}!"

    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    sender_email = "" #who the email is coming from
    password = "" #add email password
  
    #Certain phone providers allow you to send an email text. 
    #For example: ATT = 10-digit-phone-number@txt.att.net    Verizon = 10-digit-phone-number@vtext.com
    receiver_email = "" #who the email/text should be sent too.

    # Compose the email
    subject = 'Schedule Reminder'
    email_text = f'Subject: {subject}\n\n{message}'

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls(context=ssl.create_default_context())
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, recipient, email_text)
        print('Email sent successfully!')

    except Exception as e:
        print(f'An error occurred while sending the email: {str(e)}')

    finally:
        # Disconnect from the SMTP server
        server.quit()
else:
    sys.exit()
