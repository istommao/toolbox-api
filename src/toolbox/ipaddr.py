"""ip address validator."""
import re

IP_ADDRESS_REGEX = (r'^(((\d{1,2})|(1\d{2,2})|(2[0-4][0-9])|'
                    r'(25[0-5]))\.){3,3}((\d{1,2})|(1\d{2,2})|'
                    r'(2[0-4][0-9])|(25[0-5]))$')


def is_valid_ip_address(ipaddr):
    """Validate ip address is valid."""
    is_valid = re.match(IP_ADDRESS_REGEX, ipaddr)
    return True if is_valid else False

