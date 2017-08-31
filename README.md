# Gitim

[![MIT License][License Image]][License]
[![Python Version][Python Image]][Python]
![Project Status: Active][Project Status Image]

~~~~
   _______   ______       __               _ __  _     
  /  _/ _ | / __/ /____ _/ /____ _______ _(_) /_(_)_ _ 
 _/ // __ |_\ \/ __/ _ `/ __/ -_)___/ _ `/ / __/ /  ' \
/___/_/ |_/___/\__/\_,_/\__/\__/    \_, /_/\__/_/_/_/_/
                                   /___/               
~~~~
    created by "Mustafa Hasturk" <hi [at] mustafahasturk [dot] com>
    modified by "EWD Rozier" <erozier [at symbol] iastate {put in a dot} edu>
    Version: 0.1.0

    usage: 'python -m gitim -u'
                Username and password will be prompted.

    Clones all git repositories under an organization.
    To use this for grading at ISU, supply an assignment identifier using the -a flag
    For example, if the assignment shows as <assignmentname>-<username> use
    python gitim.py -o <orgname> -a <assignmentname>
    
    optional arguments:
      -h, --help            show this help message and exit
      -u USER, --user USER  Your github username
      -p PASSWORD, --password PASSWORD
                            Github password
      -t TOKEN, --token TOKEN
                            Github OAuth token
      -o ORG, --org ORG     Organisation/team. User used by default.
      -d DEST, --dest DEST  Destination directory. Created if doesn't exist.
                            [curr_dir]
      --nopull              Don't pull if repository exists. [false]
      -a ASSIGNMENT, --assignment ASSIGNMENT
      	 	     	    Pull only assignments with prefix

# Installation

You will likely have to install the module PyGithub to provide the package Github.

##### Licence
MIT

[License Image]: https://img.shields.io/badge/license-MIT-brightgreen.svg "MIT License"
[License]: https://github.com/muhasturk/gitim/blob/master/LICENSE "MIT License"

[Python Image]: https://img.shields.io/badge/python-3.5-blue.svg "Python Version: 3.5"
[Python]: https://docs.python.org/3.5/whatsnew/changelog.html#python-3-5-0-final "Python 3.5 Changelog" 

[Project Status Image]: https://img.shields.io/badge/project-active-green.svg "Project Status: Active"
