import ipaddress
class CidrMaskConvert:

    def cidr_to_mask(self, val):
        val = str(val)
        try: 
            mask = ipaddress.ip_interface(f"0.0.0.0/{val}")
        except ValueError:
            return 'Invalid'
        return str(mask.netmask)

    def mask_to_cidr(self, val):
        val = str(val)
        try: 
            mask = ipaddress.IPv4Address(val)
        except ValueError:
            return 'Invalid'
        try:
            mask = ipaddress.IPv4Network(f"0.0.0.0/{val}").prefixlen
        except:
            return 'Invalid'
        return str(mask)

class IpValidate:

    def ipv4_validation(self, val):
        try:
            val = ipaddress.IPv4Address(val)
        except:
            return False
        return True
