
from functions import replace_last, m_Prefix, p_Prefix, di_Prefix, ke_Prefix, ter_Prefix, ber_Prefix, Suffix, Verify

#Main function to stem malay words
def malaystemmer(text):
    if text[0] + text[1] == 'pe':
        stemmedword = p_Prefix(text)
    elif text[0] + text[1] == 'me':
        stemmedword = m_Prefix(text)
    elif text[0] + text[1] == 'di':
        stemmedword = di_Prefix(text)
    elif text[0] + text[1] == 'ke':
        stemmedword = ke_Prefix(text)
    elif text[0] + text[1] + text[2] == 'ter':
        stemmedword = ter_Prefix(text)
    elif text[0] + text[1] + text[2] == 'ber':
        stemmedword = ber_Prefix(text)
    else:
        stemmedword = p_Prefix(text)
        
    return stemmedword
