def getRealMail(email):
    domStart = email.find('@')
    domain = email[domStart:]
    adress = email[0:domStart].replace('.', '')
    if '+' in adress:
        adress = adress[0:adress.find('+')]
    return adress + domain

def getUniqEmails(*emails):
    print(set((getRealMail(mail) for mail in emails)))
    return len(set((getRealMail(mail) for mail in emails))) 
