'''
#=============================================================================
#     FileName: email_syntax_validator.py
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

    @staticmethod
    def validate_email(self, email = None):
        """

        The method takes an email id/email address, and verifies whether it is a valid email address
        or not according to various RFC Formats.
        It returns a boolean value(True/False) depending on the result of the various checks it makes by
        calling internally calling private methods _validate_by_rfc822(), _validate_by_rfc5321(), _validate_by_rfc6531().

        This is a static method, meaning this method can be invoked directly without creating an object for this class.
        
        """

        if email is not None:
            email = str(email)  ## TODO: str() method will faulter for unicode email addresses. So, add support for UTF-8 and remove str() function.
            email = email.strip()
            ## TODO: call the various (private) validator methods internally from this method.
            valid_by_rfc822 = self._validate_by_rfc822(email)
            if not valid_by_rfc822:
                valid_by_rfc5321 = self._validate_by_rfc5321(email)
                if not valid_by_rfc5321:
                    valid_by_rfc6531 = self._validate_by_rfc6531(email)
                    
                    return valid_by_rfc6531
                
                else:
                    return True
                
            else:
                return True
            
         else:
             return None
            
        pass
    

    def _validate_by_rfc822(self):
        """
        
        This is a private method. It validates an email address/id against RFC-822 standard.

        Return value: a boolean value - True/False

        """
        pass



    def _validate_by_rfc5321(self):
        """
        
        This is a private method. It validates an email address/id against RFC-5321 standard.

        Return value: a boolean value - True/False

        """
        pass



    def _validate_by_rfc6531(self):
        """
        
        This is a private method. It validates an email address/id against RFC-6531 standard.

        Return value: a boolean value - True/False

        """
        pass
