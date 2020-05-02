import re

def remove_special_char(text):
    text = re.sub('[áàãâ]', 'a', text)
    text = re.sub('[óòõô]', 'o', text)
    text = re.sub('[éèê]', 'e', text)
    text = re.sub('[íì]', 'i', text)
    text = re.sub('[úù]', 'u', text)
    text = re.sub('ç', 'c', text)
    return text
