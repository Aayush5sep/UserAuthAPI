import re
from django.core.exceptions import ValidationError

# Custom validators for password complexity

class UppercaseValidator(object):

    '''Minimum 1 uppercase Letter'''

    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError("The password must contain at least 1 uppercase letter, A-Z.")

    def get_help_text(self):
        return "Your password must contain at least 1 uppercase letter, A-Z."


class SpecialCharValidator(object):

    ''' Minimum 1 special character among @#$%!^&* '''

    def validate(self, password, user=None):
        if not re.findall('[@#$%!^&*]', password):
            raise ValidationError("The password must contain at least 1 special character: @#$%!^&*")

    def get_help_text(self):
        return "Your password must contain at least 1 special character: @#$%!^&*"