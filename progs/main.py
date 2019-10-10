import sys
import unittest
import HtmlTestRunner

if len(sys.argv) != 2:
    print("Usage: main.py <test config.csv>")
    print("Exiting...")
    exit(-1)
    
ts = unittest.TestSuite()
fh = open(sys.argv[1], 'rt')
for line in fh:
    tc = line.strip().split(',')
    if "module" in tc or tc[-1] not in 'yY01':
        continue
    #tc is a list of ['TestBank', 'test_sacreate', 'y']
    #import TestBank
    exec('import ' + tc[0])
    ts.addTest(eval("{}.{}('{}')".format(tc[0],tc[1],tc[2])))
    
#r = unittest.TextTestRunner(verbosity = 3)
r = HtmlTestRunner.HTMLTestRunner(output='reports')
r.run(ts)



#D:\training\python\oct7\progs>pip install html-testRunner
#Requirement already satisfied: html-testRunner in d:\sw\python37\lib\site-packages (1.2)
#Requirement already satisfied: Jinja2==2.9.5 in d:\sw\python37\lib\site-packages (from html-testRunner) (2.9.5)
#Requirement already satisfied: MarkupSafe>=0.23 in d:\sw\python37\lib\site-packages (from Jinja2==2.9.5->html-testRunner) (1.1.1)
#WARNING: You are using pip version 19.2.1, however version 19.2.3 is available.
#You should consider upgrading via the 'python -m pip install --upgrade pip' command.
#
#D:\training\python\oct7\progs>pip show html-testRunner
#Name: html-testRunner
#Version: 1.2
#Summary: A Test Runner in python, for Human Readable HTML Reports
#Home-page: https://github.com/oldani/HtmlTestRunner
#Author: Ordanis Sanchez Suero
#Author-email: ordanisanchez@gmail.com
#License: MIT license
#Location: d:\sw\python37\lib\site-packages
#Requires: Jinja2
#Required-by:
#
#D:\training\python\oct7\progs>pip list
#Package                  Version
#------------------------ ---------
#arrow                    0.15.2
#Babel                    2.7.0
#certifi                  2019.6.16
#chardet                  3.0.4
#Django                   2.2.6
#django-core              1.4.1
#django-extra-views       0.11.0
#django-haystack          2.8.1
#django-oscar             2.0.2
#django-phonenumber-field 2.0.1
#django-tables2           1.21.2
#django-treebeard         4.3
#django-widget-tweaks     1.4.5
#factory-boy              2.12.0
#Faker                    2.0.2
#html-testRunner          1.2
#idna                     2.8
#Jinja2                   2.9.5
#jinja2-time              0.2.0
#make                     0.1.4
#MarkupSafe               1.1.1
#phonenumbers             8.10.19
#Pillow                   6.1.0
#pip                      19.2.1
#purl                     1.5
#pycountry                19.8.18
#python-dateutil          2.8.0
#pytz                     2019.2
#requests                 2.22.0
#setuptools               40.8.0
#six                      1.12.0
#sorl-thumbnail           12.5.0
#sqlparse                 0.3.0
#text-unidecode           1.3
#urllib3                  1.25.3
#WARNING: You are using pip version 19.2.1, however version 19.2.3 is available.
#You should consider upgrading via the 'python -m pip install --upgrade pip' command.

    
    
