import smtplib
import getpass
VERSION='0.3'
#Server Info
serverAddress='smtp.gmail.com'
portNumber=587


def main():
    print('Welcome to gsmtp CLI {} by Ashkan Taravati'.format(VERSION))
    print('This program currently works with Gmail SMTP server with TLS.')
    print("Don't forget to allow less-secure programs to authenticate using your gmail account.")
    input('Press any key to continue...')
    print("Gmail credentials needed. Your credentials won't be saved anywhere.")
    authEmail=input("Enter your gmail address:\t")
    authPassword=getpass.getpass(prompt='Enter your gmail password:\t')
    #Mail Info
    senderAddress=defaultedInput(authEmail,"Enter sender's email address:\t")
    recipientAddress=input("Enter recipient's email address:\t")
    subject=defaultedInput('Test message','Enter subject:\t')
    messageText=defaultedInput('A Test Message From Simple SMTP client','Enter Message:\t',multiLineInput)
    data='Subject: {}\n\n{}'.format(subject, messageText)
    print("Attempting to send...")
    server = smtplib.SMTP(serverAddress,portNumber )
    server.starttls()
    try:
        server.login(authEmail, authPassword)
    except Exception as ex:
        printError(ex,"Error occured while logging in!","quitting")
        server.quit()
        quit()
    print("Authenticated.")
    try:
        server.sendmail(senderAddress, recipientAddress, data)
    except Exception as ex:
        printError(ex,"Error occured while sending!","quitting")        
    finally:
        server.quit()
    print("Your Email was sent successfully.")
    quit()

def defaultedInput(defaultValue,promptMsg,inputFunc=input):
    print(promptMsg+"you can leave blank. default is '{}'".format(defaultValue))
    
    inputStr=inputFunc()
    if not inputStr:
        inputStr=defaultValue
    return inputStr
def printError(exception,generalMessage,nextBehavior):
    print("{}\nError message is as follows:\n{}\n{}".format(generalMessage,str(exception),nextBehavior))

def multiLineInput(promptText,printNotice=True):
    notice="Enter/Paste your content and send EOF character to save. *nix:Ctrl-D, Windows:Ctrl-Z"
    if printNotice:
        print(notice)
    contents = []
    while True:
        try:
            line = input(promptText)
        except EOFError:
            break
        contents.append(line)
    return '\n'.join(contents)


if __name__ == '__main__':
    main()

    # except SMTPHeloError:
    #     print("The server didn't reply properly to the helo greeting.")
    # except SMTPRecipientsRefused:
    #     print("The server rejected ALL recipients (no mail was sent).")
    # except SMTPSenderRefused:
    #     print("The server didn't accept the from_addr.")
    # except SMTPDataError:
    #     print("The server replied with an unexpected error code (other than a refusal of a recipient).")
    # except SMTPNotSupportedError:
    #     print("The mail_options parameter includes 'SMTPUTF8' but the SMTPUTF8 extension is not supported by the server.") 