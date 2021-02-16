#problem link : https://coderbyte.com/editor/Codeland%20Username%20Validation:Python3
#time : O (1)

import re
def CodelandUsernameValidation(s):

  # code goes here
  if s[len(s)-1] == '_':

   return 'false'
  elif 25<len(s)<4:
    return 'false'
  elif not (re.match('[a-zA-Z]' , s[0] ) ):
    return 'false' 
  elif  (re.findall('[!@#$%^&*()+}{;:.]', s)) :
    return 'false'
  else:
    return 'true'
# keep this function call here 
print(CodelandUsernameValidation(input()))
        
