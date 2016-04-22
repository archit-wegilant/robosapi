'''
#=============================================================================
#     FileName: analyzer.py
#       Author: Archit Kapoor
#        Email: archit.imsec10@gmail.com
#=============================================================================
'''

import re
import unicodedata
import logging


class EmailSyntaxValidator:
    """

    This is the Syntax Validator module of the Application.
    Here, an email is received and that is validated against some set of RFCs.

    RFC-822 is probably obselete now, still used at some place.
    RFC-6531 is probably the most recent one. And hence being the latest, it is
    mandatory to syntax validate the email against this RFC. RFC-6531 considers under
    its purview some UTF-8 characters also.

    For more information, please consider reading the following docs/links:
    > https://en.wikipedia.org/wiki/Email_address
    > https://tools.ietf.org/html/rfc6531

    """

    def __init__(self):
        pass


    def validate_by_rfc822(self):
        pass



    def validate_by_rfc5321(self):
        pass



    def validate_by_rfc6531(self):
        pass
