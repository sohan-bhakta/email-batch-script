from redmail import EmailSender
import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

GOOGLE_EMAIL = os.getenv("GOOGLE_EMAIL")
GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")
resume_path = "../data/sohan_bhakta_resume.pdf"
df = pd.read_csv('../data/emails.csv')


email = EmailSender(
    host='smtp.gmail.com',
    port=587,
    username=GOOGLE_EMAIL,
    password=GOOGLE_APP_PASSWORD,
    use_starttls=True
)

subject = "Interest in Charlie Health"

for index, row in df.iterrows():
    first_name = str(row['first_name'])
    first_name = first_name[0].upper() + first_name[1:]

    print(f"sending to {first_name}...")
    try:
        html_body = f"""
                    <html>
                        <body>
                            <p>Hi {first_name},</p>
                            <p>It's a pleasure to meet you. I am a 4th-year student finishing up this 
                            semester from the University of Arizona. Outside of school, I have had 
                            a handful of full-stack, machine learning, and management experience from 
                            Komatsu, Avnet, & Amazon. My interests align with the mission of 
                            Charlie Health of helping personalized mental health support to your customers.</p>
                            
                            <p>I wanted to reach out directly because my interest and skills align with 
                            the Software Engineer, Full Stack role. I understand that this may be an 
                            informal way of reaching out, but I am highly committed and persistent and 
                            hopefully can help you continue to uphold your company's values.</p>

                            <p>I have attached my resume below.</p>

                            <p>Thank you for your time,</p>
                            <p>Sohan Bhakta</p>
                        </body>
                    </html>
                    """


        email.send(
            subject=subject,
            sender=GOOGLE_EMAIL,
            receivers=[row['email']],
            html=html_body,
            attachments=[resume_path]
        )
    except Exception as e:
        print(f"Failed to send email to {row['email']}: {e}")
    
print("complete...")


