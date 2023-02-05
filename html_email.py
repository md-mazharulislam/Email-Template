from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Create the message
msg = MIMEMultipart()
msg['From'] = 'mazharulislam54492@gmail.com'
msg['To'] = 'md.mazharulislam6153@gmail.com'
msg['Subject'] = 'Test Email'

#Add the html content to the messsage
html = """
<html>
    <body>
    <p>Hello,<br>
        How are you?<br>
        You want more traffic, right?

        I have the answer: capitalize on SEO trends before they leave you in the dust.

        Search marketing changes fast; my webinar can help you stay ahead of the curve.

        Join me and my team, NP Digital, at 8am PST on 1/31 (next Tuesday) for our webinar:

        Search Engine Rewind: What We Learned In 2022 and Where SEO Is Going in 2023.

        Click here to register! See you then.

        Cheers,

        Neil Patel

        Here is the <a href="https://mail.google.com/">link</a> you wanted.
    </p>
    </body>
</html>
"""
part = MIMEText(html, 'html')
msg.attach(part)

#Send the message
import smtplib
s = smtplib.SMTP('localhost')
print(s.help())
s.sendmail(msg['From'], msg['To'],msg.as_string())
s.quit()