import smtplib 
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
import random
import os
# SMTP server details (for Gmail) 

def send_email( send_email_to):
    smtp_server = "smtp.gmail.com" 
    smtp_port = 587 
    #Sender's email and password 
    sender_email = "doremondeep26@gmail.com"
    sender_password = "qdqarbgupfcnhqau" 
    # Recipient's email 
    recipient_email = send_email_to
    # Subject and body of the email 
    subject = "OTP FOR VERIFICATION"
    body = str(random.randint(100000,999999))
    # Create the email message 
    message = MIMEMultipart() 
    message["From"] = sender_email 
    message["To"] = recipient_email
    message["Subject"] = subject 
    message.attach(MIMEText(body, "plain")) 
    # Connect to the SMTP server and send the email 
    try: 
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() 
        # Secure the connection 
        server.login(sender_email, sender_password) 
        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully!") 
    except Exception as e: 
        print(f"Error: {e}") 
        
    finally:
        server.quit()
    return body

# print(send_email(send_email_to = "nikadeep26@gmail.com"))