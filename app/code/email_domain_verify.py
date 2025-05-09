import requests
import re
def is_valid_email_domain(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(email_regex, email):
        domain = email.split('@')[1]
        try:
            requests.request('GET',url=f'https://{domain}',timeout=10)
            return True
        except:
            return False
    else:
        return False
    
print(is_valid_email_domain("pranjulpal@gmail.com"))
