
import datetime
import time

#for a premade AI chatterbot
#from chatterbot import ChatBot
#chatbot = ChatBot("Baxter")

#for a premade clever chatbot
from cleverbot import Cleverbot
chatbot = Cleverbot()

# Credentials
username = 'gmailUsername'
password = 'gmailPassword'

date = (datetime.date.today() - datetime.timedelta(7)).strftime("%d-%b-%Y")

def sendEmail(toaddrs,subject,text):
    import smtplib

    fromaddr = username+'@gmail.com'

    # Prepare actual message
    msg = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (fromaddr, toaddrs,#", ".join(toaddrs),
           subject, text)
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        print 'I successfully sent the email'
    except:
        print "Terribly sorry sir, I failed to send the email"

def checkMail():#checks mail for specific commands or replies to texts
    import imaplib
    
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(username+'@gmail.com', password)
    mail.list()
    # Out: list of "folders" aka labels in gmail.
    mail.select("inbox") # connect to inbox.

    """check for text messages"""
    result, data = mail.uid('search', None, '(SENTSINCE {date} FROM "gvNumber.sendersNumber.random?cf85Dm8WDh@txt.voice.google.com")'.format(date=date))
    try:
        result, data = mail.uid('fetch', data[0][-2:], '(BODY[TEXT])')#prints the body tex
        raw_email = data[0][1] # here's the body, which is raw text of the whole email
        body=raw_email.strip()
        if body:
            subject=' '
			toAddr='gvNumber.sendersNumber.randomChars?@txt.voice.google.com'
            #emailText=chatbot.get_response(body) #for chatterbot
			emailText=chatbot.ask(body) #for cleverbot
            sendEmail(toAddr,subject,emailText)
            mail.store("1:*", '+X-GM-LABELS', '\\Trash')
    except:
    #else:
        print "no texts yet"
    mail.close()
    mail.logout()


while True:
    if (int(datetime.datetime.now().strftime('%H')) >= 6 and
        int(datetime.datetime.now().strftime('%H')) <= 23):
        print('checking...')
        try:
            checkMail()
        except:
            print("Check mail error")
        time.sleep(600) #so you don't waste precious clock cycles checking
    else:#don't check between 11pm and 6am
        time.sleep(6000)
