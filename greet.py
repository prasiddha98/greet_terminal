#!/usr/bin/env python3
from datetime import datetime
import getpass


def greet():
    current_time = datetime.now()
    username = getpass.getuser()
    if current_time.hour< 12:
        message =f"G00D_M0rn!ng {username}"
    elif 12 <= current_time.hour < 18:
     message=f" G00D_Aftern00n {username} "
    else:
        message= f" G00D_Even!ng {username} "
    
    return message
message=greet()
print(message)