from email.mime.application import MIMEApplication
# Add an attachment
with open('example.pdf','rb') as f:
    attach = MIMEApplication(f.read(), _subtype='pdf')
    attach.add_header('content-disposition', 'attachment', filename='example.pdf')
    msg.attach(attach)

    