#!/usr/bin/env pythonf

import ldap, argparse


def ldapQuery():
    ldap_host = ""
    ldap_base = ""
    ldap_entry = ""
    team = []
    l = ldap.initialize(ldap_host)
    result = l.search_s(ldap_base,ldap.SCOPE_SUBTREE,ldap_entry)

def parseCSV(filename):
    filename = args.filename
    reader = csv.reader(open(filename, "rb"), delimiter=',')

if __name__ == "__main__":
    parser = argparse.ArgumentParse(description="Comparing CSV to LDAP")

    parser.add_argument('-f',
                        required=True,
                        dest="filename",
                        help='The .csv file containing hosts and exclusions')

    parser.add_argument('--ldap-host','-m',
                        #required=True,
                        dest='lookup_host',
                        help='enter the LDAP source host uri for example: ldap.example.com')

    parser.add_argument('--basedn','-b',
                        #required=True,
                        dest='basedn',
                        help='The search base for LDAP for example: dc=example,dc=com')

    parser.add_argument('--cacert','-c',
                        #required=True,
                        dest='cacert',
                        help='The path to the CA cert file or directory containing it,  if a directory then make sure it is managed by the c_rehash utility')

    parser.add_argument('--password', metavar='password', \
                        dest='password', \
                        nargs='*', \
                        #required=True, \
                        action=PromptAction, \
                        help='Plain text password for user')




