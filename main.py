import random
import smtplib

my_email = 'saniyakhatun896@gmail.com'
password = 'lqfybhdtcsjbenos'
# with  smtplib.SMTP('smtp.gmail.com',  587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs='anishgharti10@gmail.com', msg="SUbject:hello\n\n hi i am learning")


with open('quotes.txt') as data:
   quotes = data.readlines()
   random_quote = random.choice(quotes)
   print(random_quote)
   

with  smtplib.SMTP('smtp.gmail.com',  587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs='anishgharti10@gmail.com', msg=f" subject:hello \n\n {random_quote}")