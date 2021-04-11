from django.core.exceptions import ValidationError
def phone_number_validator(value):
    if len(str(value)) == 10:
        return value
    raise ValidationError("Phone number can only be of 10 digits")

def password_len_validator(value):
    if(len(value)>8):
        return value
    raise ValidationError("Password should contain more than 8 characters")
