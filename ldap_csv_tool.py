#!/usr/bin/env python

import ldap, argparse, csv
from ldap import sasl, modlist


def ldapQuery(entry):
    ldap_host = args.ldap_host
    ldap_base_dn = args.basedn
    search_entry = entry

    l = ldap.initialize(ldap_host)

    # Authenticated connection created, GSSAPI is used
    auth = ldap.sasl.gssapi("")


    if ldap_host.startswith('ldap://'):
        ldap_connection = ldap.initialize(ldap_host)
    else:
        ldap_connection = ldap.initialize("ldap://" + ldap_host)

    ldap_connection.sasl_interactive_bind_s("", auth)

    result = ldap_connection.search_s( ldap_base_dn, ldap.SCOPE_SUBTREE, "cn="+search_entry)
    print result
    return result
    #result = l.search_s(ldap_base,ldap.SCOPE_SUBTREE,ldap_entry)

def parseCSV(filename, args):
    reader = csv.reader(open(filename, "rb"), delimiter=',')
    exists_in_ldap = []
    not_in_ldap = []
    # print list(reader)
    # create a list of the CSV data
    group_list = list(reader)
    for group in group_list:
        print "Group: ", group[0]
        result = ldapQuery(group[0])
        if not result:
            print "group: ", group[0], " is not in LDAP"
            not_in_ldap.append(group[0])
        else:
            exists_in_ldap.append(group[0])
        print "#################\n"
    return not_in_ldap

if __name__ == "__main__":
    global args
    parser = argparse.ArgumentParser(description="Comparing CSV to LDAP")

    parser.add_argument('-f',
                        required=True,
                        dest="filename",
                        help='The .csv file containing hosts and exclusions')

    parser.add_argument('--ldap-host','-m',
                        required=True,
                        dest='ldap_host',
                        help='enter the LDAP source host uri for example: ldap.example.com')

    parser.add_argument('--basedn','-b',
                        required=True,
                        dest='basedn',
                        help='The search base for LDAP for example: dc=example,dc=com')

    # parser.add_argument('--cacert','-c',
    #                     required=True,
    #                     dest='cacert',
    #                     help='The path to the CA cert file or directory containing it,  if a directory then make sure it is managed by the c_rehash utility')

    # parser.add_argument('--password', metavar='password', \
    #                     dest='password', \
    #                     nargs='*', \
    #                     #required=True, \
    #                     action=PromptAction, \
    #                     help='Plain text password for user')

    args = parser.parse_args()
    filename = args.filename
    not_in_ldap = parseCSV(filename, args)
    print "Groups not in LDAP: ", not_in_ldap
