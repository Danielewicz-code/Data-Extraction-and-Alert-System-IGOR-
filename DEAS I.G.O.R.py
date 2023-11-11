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
        _ , email_ids = server.search(None, '(UNSEEN FROM "The.email.you.want@gmail.com")') # _ is nothing more than the status
        if email_ids[0]:
            #here we just search for the possible e-mail id we could have and split it if we have more than one
            for email_id in email_ids[0].split():
                _ , email_data = server.fetch(email_id, '(RFC822)') #here we get the email id and the content of the email
                email_message = email.message_from_bytes(email_data[0][1]) # 0 and 1 are the featched data which we are converting using message_from_bytes do decode it

                #here we can get the subject, from (who send the mail) and body of the message among other things
                subject = email_message['subject']
                from_id = email_message['from']


                body_content = ' '
                
                #loop to get every part of the text (body)
                for part in email_message.walk():
                    if part.get_content_type() == 'text/plain': #extract only text/numeric data
                        body_content += part.get_payload(decode=True).decode('utf-8') #Decode the payload

                #hide this useles data for the purpose of the proyect
                body_content = body_content.replace('Content-Type: text/plain; charset="UTF-8"', ' ') 
                
                igor_alert('The.email.you.want@gmail.com', from_id, subject, body_content) #here you can use mobile services or e-mails

        else:
            print('no new messages')
            


    except Exception as e:
        print('the program has an error: ', str(e))    

    #even if an error occurrs it will logout always
    finally:
        server.logout()




#this function will be the one responsible to send the alert
def igor_alert(to, from_id, subject, body):

    msg = EmailMessage()
    msg.set_content(f'Message from: {from_id} \n \n {body}')
    msg['subject']= (f'New Alert: {subject}')
    msg['to'] = to

    #user and password
    user = 'The.email.you.want@gmail.com'
    msg['from'] = user
    password = 'Your password'

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
    user = 'The.email.you.want@gmail.com'
    password = 'Your password'
    extract_info(user, password)     
    
