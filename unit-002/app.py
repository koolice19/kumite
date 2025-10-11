import re
# I need to use re.search to find the string so this is including the library
def has_ligma(sentence):
    # Search for ligma regardless of case within the string
    if re.search('ligma', sentence, re.IGNORECASE):
        # Return Boolean expression evaluating if true or false
        return True
#   if untrue return false
    return False
