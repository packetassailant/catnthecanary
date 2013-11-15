# catnthecanary

## Objective
```
Catnthecanary is an application to query the canary.pw (https://canary.pw/) data set for potentially
sensitive data that has been disclosed on various public repositories, such as pastebin. Currenlty,
the maintainers of canary.pw don't expose an API to interface with the data set. Therefore, this
application attempts to create a method to programmatically perform single and bulk queries. The
supported canary.pw operators are as follows. Although, these have been obfuscated and simply use
command line optargs to perform the queries.

Operators: !ip, !email, !host, !hash, !phone, !http
```


## Usage
```
$ python catnthecanary.py -u
  Info: catnthecanary was created by Chris Patten
  Purpose: search canary.pw for leaked company data
  Contact: cpatten[a.t.]packetresearch.com and @packetassailant

  Usage: ./catnthecanary.py <options> <arguments>
  -u or --usage    Print this help menu
  -i or --ip       IP address (Required)
  -I or --ifile    Newline delimited IP file (Required)
  -e or --email    Email address (Required)
  -E or --efile    Newline delimited email file (Required)
  -h or --host     System hostname (Required)
  -H or --hfile    Newline delimited hostname file (Required)
  -a or --hash     System hash (Required)
  -A or --afile    Newline delimited hash file (Required)
  -p or --phone    Phone number (Required)
  -P or --pfile    Newline delimited phone file (Required)
  -w or --http     Url address (Required)
  -W or --wfile    Newline delimited URL file (Required)
```

## Installation
```
# Installation
# -----------------------------------------------
# Catnthecanary was tested on Ubuntu 12.04 and OSX ML
# ----------- OSX ---------------
# OSX Deps: pip install -U -r environment.txt
# ----------- Linux -------------
# Linux: sudo apt-get install python-pip
# Linux Deps: pip install -U -r environment.txt
```

## Sample Run
```
$ python catnthecanary.py -I hosts.txt
10.10.1.1: Number of results: 13: https://canary.pw/search/?q=!ip+10.10.1.1
10.10.1.2: Number of results: 5: https://canary.pw/search/?q=!ip+10.10.1.2
10.10.1.3: Number of results: 1: https://canary.pw/search/?q=!ip+10.10.1.3
10.10.1.4: Number of results: 1: https://canary.pw/search/?q=!ip+10.10.1.4
10.10.1.5: Number of results: 1: https://canary.pw/search/?q=!ip+10.10.1.5
10.10.1.7: Number of results: 1: https://canary.pw/search/?q=!ip+10.10.1.7
```

## Developing
```
Alpha code under active development
```

## Contact
```
# Author: Chris Patten
# Contact (Email): cpatten[t.a.]packetresearch[t.o.d]com
# Contact (Twitter): packetassailant
```




