import string
import random

# Base62 characters
BASE62 = string.ascii_letters + string.digits


# Generate unique short code
# Example: aB91xK

def generate_short_code(length=6):
    return ''.join(
        random.choices(BASE62, k=length)
    )