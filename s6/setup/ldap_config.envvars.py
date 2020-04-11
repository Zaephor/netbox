## Worthwhile reference 
## https://github.com/netbox-community/netbox-docker/blob/release/configuration/ldap_config.py
import os
import ldap

def read_secret(secret_name):
    try:
        f = open('/run/secrets/' + secret_name, 'r', encoding='utf-8')
    except EnvironmentError:
        return ''
    else:
        with f:
            return f.readline().strip()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Server URI
#AUTH_LDAP_SERVER_URI = "ldaps://ad.example.com"
AUTH_LDAP_SERVER_URI = os.getenv('LDAP_SERVER_URI')

# The following may be needed if you are binding to Active Directory.
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}

# Set the DN and password for the NetBox service account.
#AUTH_LDAP_BIND_DN = "CN=NETBOXSA, OU=Service Accounts,DC=example,DC=com"
AUTH_LDAP_BIND_DN = os.getenv('LDAP_BIND_ON')
#AUTH_LDAP_BIND_PASSWORD = "demo"
AUTH_LDAP_BIND_PASSWORD = os.getenv('LDAP_BIND_PASSWORD', read_secret('ldap_bind_password'))

# Include this setting if you want to ignore certificate errors. This might be needed to accept a self-signed cert.
# Note that this is a NetBox-specific setting which sets:
#     ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
LDAP_IGNORE_CERT_ERRORS = True
