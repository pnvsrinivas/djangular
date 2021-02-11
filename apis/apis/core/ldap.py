import ldap

from django.conf import settings
from apis.core.utils import literal_eval_as_dict

def authenticate(username, password, address='127.0.0.1'):
    try:
        if settings.DEBUG:
            return True, "Successfull"
            
        conn = ldap.initialize('ldap://' + address)
        conn.protocol_version = 3
        conn.set_option(ldap.OPT_REFERRALS, 0)
        result = conn.simple_bind_s(username, password)
        return isinstance(result, list) and len(result) == 4 and result[0] == 97, 'Login successful'
    except ldap.LDAPError as e:
        msg = literal_eval_as_dict(str(e)).get('desc')
        if not msg:
            msg = 'Unable to contact ldap server!!'
        return False, msg