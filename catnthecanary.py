#!/usr/bin/env python2.7
# Project Name: catnthecanary
# Purpose: canary.pw frontend query utility
# Operators: !ip, !email, !host, !hash, !phone, !http
# Author: Chris Patten
# Contact (Email): cpatten[t.a.]packetresearch[t.o.d]com
# Contact (Twitter): packetassailant
#
# Installation
# -----------------------------------------------
# Catnthecanary was tested on Ubuntu 12.04 and OSX ML
# ----------- OSX ---------------
# OSX Deps: pip install -U -r environment.txt
# ----------- Linux -------------
# Linux: sudo apt-get install python-pip
# Linux Deps: pip install -U -r environment.txt


from bs4 import BeautifulSoup
import getopt
import requests
import sys

def usage():
    print 'Info: catnthecanary was created by Chris Patten'
    print 'Purpose: search canary.pw for leaked company data'
    print 'Contact: cpatten[a.t.]packetresearch.com and @packetassailant\n'
    print 'Usage: ./catnthecanary.py <options> <arguments>'
    print '-u or --usage    Print this help menu'
    print '-i or --ip       IP address (Required)'
    print '-I or --ifile    Newline delimited IP file (Required)'
    print '-e or --email    Email address (Required)'
    print '-E or --efile    Newline delimited email file (Required)'
    print '-h or --host     System hostname (Required)'
    print '-H or --hfile    Newline delimited hostname file (Required)'
    print '-a or --hash     System hash (Required)'
    print '-A or --afile    Newline delimited hash file (Required)'
    print '-p or --phone    Phone number (Required)'
    print '-P or --pfile    Newline delimited phone file (Required)'
    print '-w or --http     Url address (Required)'
    print '-W or --wfile    Newline delimited URL file (Required)'

def stage_request(kval, sval):
    reqval = kval.strip()
    query = "!%s+%s" % (sval, reqval)
    canurl = ("https://canary.pw/search/?q=" + query)
    r = requests.get(canurl)
    if r.status_code is 200:
        process_response(r, reqval, canurl)
    else:
        print "Error: HTTP response returned: %s" % (r.status_code)

def make_requests(argdict):
    for k in argdict.keys():
        if 'ip' in k:
            ip = argdict.get(k)
            stage_request(ip,'ip')
        if 'ifile' in k:
            ifile = argdict.get(k)
            try:
                for ip in ifile:
                    stage_request(ip,'ip')
            finally:
                ifile.close()
        if 'email' in k:
            email = argdict.get(k)
            stage_request(email,'email')
        if 'efile' in k:
            efile = argdict.get(k)
            try:
                for email in efile:
                    stage_request(email,'email')
            finally:
                efile.close()
        if 'host' in k:
            host = argdict.get(k)
            stage_request(host,'host')
        if 'hfile' in k:
            hfile = argdict.get(k)
            try:
                for host in hfile:
                    stage_request(host,'host')
            finally:
                hfile.close()
        if 'hash' in k:
            hash = argdict.get(k)
            stage_request(hash,'hash')
        if 'afile' in k:
            afile = argdict.get(k)
            try:
                for hash in afile:
                    stage_request(hash,'hash')
            finally:
                afile.close()
        if 'phone' in k:
            phone = argdict.get(k)
            stage_request(phone,'phone')
        if 'pfile' in k:
            pfile = argdict.get(k)
            try:
                for phone in pfile:
                    stage_request(phone,'phone')
            finally:
                pfile.close()
        if 'http' in k:
            http = argdict.get(k)
            stage_request(http,'http')
        if 'wfile' in k:
            wfile = argdict.get(k)
            try:
                for http in wfile:
                    stage_request(http,'http')
            finally:
                wfile.close()

def process_response(res, ip, requrl):
    data = res.text
    soup = BeautifulSoup(data)
    for link in soup.findAll('p'):
        plink = ''.join(link.findAll(text=True))
        if "Number of results" in plink:
            print "%s: %s: %s" % (ip, plink, requrl)

def main():
    argdict = {}

    isingleflag = False
    imultiflag = False
    esingleflag = False
    emultiflag = False
    hsingleflag = False
    hmultiflag = False
    asingleflag = False
    amultiflag = False
    psingleflag = False
    pmultiflag = False
    wsingleflag = False
    wmultiflag = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ui:I:e:E:h:H:a:A:p:P:w:W:", ["ip=",
                                                                               "ifile=",
                                                                               "email=",
                                                                               "efile=",
                                                                               "host=",
                                                                               "hfile=",
                                                                               "hash=",
                                                                               "afile=",
                                                                               "phone=",
                                                                               "pfile=",
                                                                               "http=",
                                                                               "wfile="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    if len(opts) == 0:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-u", "--usage"):
            usage()
            sys.exit(2)
        if opt in ("-i", "--ip"):
            ip = arg
            isingleflag = True
            argdict["ip"] = ip
        elif opt in ("-I", "--ifile"):
            ifile = open(arg, 'r')
            imultiflag = True
            argdict["ifile"] = ifile
        if opt in ("-e", "--email"):
            email = arg
            esingleflag = True
            argdict["email"] = email
        elif opt in ("-E", "--efile"):
            efile = open(arg, 'r')
            emultiflag = True
            argdict["efile"] = efile
        if opt in ("-h", "--host"):
            host = arg
            hsingleflag = True
            argdict["host"] = host
        elif opt in ("-H", "--hfile"):
            hfile = open(arg, 'r')
            hmultiflag = True
            argdict["hfile"] = hfile
        if opt in ("-a", "--hash"):
            hash = arg
            asingleflag = True
            argdict["hash"] = hash
        elif opt in ("-A", "--afile"):
            afile = open(arg, 'r')
            amultiflag = True
            argdict["afile"] = afile
        if opt in ("-p", "--phone"):
            phone = arg
            psingleflag = True
            argdict["phone"] = phone
        elif opt in ("-P", "--pfile"):
            pfile = open(arg, 'r')
            pmultiflag = True
            argdict["pfile"] = pfile
        if opt in ("-w", "--http"):
            web = arg
            wsingleflag = True
            argdict["web"] = web
        elif opt in ("-W", "--wfile"):
            wfile = open(arg, 'r')
            wmultiflag = True
            argdict["wfile"] = wfile
        if (isingleflag and imultiflag) or \
           (esingleflag and emultiflag) or \
           (hsingleflag and hmultiflag) or \
           (asingleflag and amultiflag) or \
           (psingleflag and pmultiflag) or \
           (wsingleflag and wmultiflag):
            print "Error: mutually exclusive -- use either a single object (e.g., IP) " \
                  "or a file of objects (e.g., ipfile)\n"
            usage()
            sys.exit(2)

    # Bootstrap
    make_requests(argdict)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "Caught KeyboardInterrupt, terminating execution"
        sys.exit(0)
