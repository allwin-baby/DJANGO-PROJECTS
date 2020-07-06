import smtplib
gmail_user = 'xiaomitotom@gmail.com'
gmail_password = 'PASSWORD'
sent_from = 'xiaomitotom@gmail.com'
to = ['xiaomitotom@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, whats up?\n\n- You'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print( 'Email sent!')
except:
    print ('Something went wrong...')