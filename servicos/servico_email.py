import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.get_env import get_env
from email_validator import validate_email

EMAIL_LOGIN = get_env("EMAIL_LOGIN")
SENHA_LOGIN = get_env("SENHA_LOGIN")
HOST = get_env("HOST") #smtp.gmail.com
PORTA = get_env("PORTA") #587

def enviar_emails(destinatarios:list) -> int:    
    emails_enviados = 0
    servidor=smtplib.SMTP(HOST,PORTA)
    try:
        servidor.starttls()
        servidor.login(EMAIL_LOGIN, SENHA_LOGIN)
        for destinatario in destinatarios:
            mensagem = MIMEMultipart()
            mensagem['From'] = EMAIL_LOGIN
            mensagem['TO'] = destinatario['email']
            mensagem['subject'] = destinatario['titulo_email']

            conteudo_email = MIMEText(destinatario['mensagem'], 'plain')
            mensagem.attach(conteudo_email)
            try:
                servidor.send_message(mensagem)
                emails_enviados += 1
            except:
                pass
            del mensagem
    except:
        pass
    finally:
        servidor.quit()
        return emails_enviados  

def email_valido(email:str) -> bool:
    try:
        validate_email(email)     
        return True
    except:
        return False