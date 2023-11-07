#extract data
import imaplib
#send 
import smtplib
#message and email management
import email
from email.message import EmailMessage



def extract_info(user, password):
    #server creation
    server = imaplib.IMAP4_SSL('imap.gmail.com') #here you sould put the specific mail service that you want to use or similars

    try:
        #login, and selection
        server.login(user, password)
        server.select('Inbox')


        #select the emails and information to extract
        _ , email_ids = server.search(None, '(UNSEEN FROM "The.mail.you.want@gmail.com")')
        if email_ids[0]:
            #here we just search for the possible gmails from where we are getting mails
            for email_id in email_ids[0].split():
                _ , email_data = server.fetch(email_id, '(RFC822)')
                #here we pass the email data which has the email id and the body in RFC822 format
                email_message = email.message_from_bytes(email_data[0][1])

                #here we can get the subject and body of the message
                subject = email_message['subject']

                #here we just get the plain text or the body of the message, for that we use this for loop
                body_content = ' '
                
                for part in email_message.walk():
                    if part.get_content_type() == 'text/plain':
                        body_content += part.as_string()

                body_content = body_content.replace('Content-Type: text/plain; charset="UTF-8"', ' ') #this just hides something you don't want when reciving the alerts       

                
                igor_alert('The.mail.you.want@gmail.com', subject, body_content) #here you can use mobile services or e-mails

        else:
            print('no new messages')
            


    except Exception as e:
        print('the program has an error: ', str(e))    

    #even if an error occurrs it will logout always
    finally:
        server.logout()




#this function will be the one responsible to send the alert
def igor_alert(to, subject, body):

    #email creation giving the data we have on extract_info()
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject']= "New Alert!: " + subject
    msg['to'] = to

    #user and password
    user = 'The.mail.you.want@gmail.com'
    msg['from'] = user
    password = 'Your.password'
    
    #server creation and activation to send the alert
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    print('message sent')

    #log out the server
    server.quit()

#this gives the program more "security" for sensible data

if __name__ == '__main__':
    user = 'The.mail.you.want@gmail.com'
    password = 'Your.password'
    extract_info(user, password)   
    