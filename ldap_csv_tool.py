#!/usr/bin/env python

import ldap, argparse


def ldapQuery():
    ldap_host = ""
    ldap_base = ""
    ldap_entry = ""
    team = []
    l = ldap.initialize(ldap_host)
    result = l.search_s(ldap_base,ldap.SCOPE_SUBTREE,ldap_entry)

def parseCSV():

if __name__ == "__main__":
    parser = argparse.ArgumentParse(description="Comparing CSV to LDAP")
    
    parser.add_argument(
