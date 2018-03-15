def filter_leetify(a, **kw):
    """Leetify text ('a' becomes '4', 'e' becomes '3', etc.)"""
    return a.replace('a','4').replace('e','3').replace('i','1').replace('o','0').replace('u','^')

def filter_dhcp_search_encode(string):
    '''
    Converts a comma separated DNS search string to RFC3397 binary encoded format.
    '''
    import sys
    hexlist = []
    for domain in string.split(" "):
        for part in domain.split("."):
            part = part.strip()
            hexlist.append("%02x" % len(part))
            for c in part:
                hexlist.append(c.encode("hex"))
        hexlist.append("00")
    return "".join(hexlist)


def filter_reverse_dns_ptr(address):
    from netaddr import *
    ip = IPAddress(address)
    if ip.version != 4 and ip.version != 6:
        return None
    else:
        return ip.reverse_dns

def filter_dns_ptr_host(address, reverse_domain):
    rev_domain = reverse_domain
    ptr_string = filter_reverse_dns_ptr(address)
    index = ptr_string.find(rev_domain)
    return ptr_string[0:index]

