#!/usr/bin/env python

from __future__ import print_function
from getpass import getpass
from argparse import ArgumentParser
from os import chdir, path, makedirs, pardir, environ, getcwd
from subprocess import call, Popen, check_output
from functools import partial
from platform import python_version_tuple
import fileinput
import re

from github import Github

if python_version_tuple()[0] == u'2':
    input = lambda prompt: raw_input(prompt.encode('utf8')).decode('utf8')

__author__ = u'"Samuel Marks", "Mustafa Hasturk" <mustafa.hasturk@yandex.com>'
__modified__ = u'"EWD Rozier", <erozier@iastate.edu>'
__version__ = '0.1.0'


class Gitim():
    def __init__(self):
        print(u"""
   _______   ______       __               _ __  _     
  /  _/ _ | / __/ /____ _/ /____ _______ _(_) /_(_)_ _ 
 _/ // __ |_\ \/ __/ _ `/ __/ -_)___/ _ `/ / __/ /  ' \ 
/___/_/ |_/___/\__/\_,_/\__/\__/    \_, /_/\__/_/_/_/_/ 
                                   /___/
                                   
created by {__author__}
modified by {__modified__}
Version: {__version__}
""".format(__author__=__author__, __modified__=__modified__, __version__=__version__))

    def set_args(self):
        """ Create parser for command line arguments """
        parser = ArgumentParser(
                usage=u'python -m gitim -u\'\n\t\t\tUsername and password will be prompted.',
                description='Clone all your Github repositories.')
        parser.add_argument('-u', '--user', help='Your github username')
        parser.add_argument('-p', '--password', help=u'Github password')
        parser.add_argument('-t', '--token', help=u'Github OAuth token')
        parser.add_argument('-o', '--org', help=u'Organisation/team. User used by default.')
        parser.add_argument('-d', '--dest', help=u'Destination directory. Created if doesn\'t exist. [curr_dir]')
        parser.add_argument('--nopull', action='store_true', help=u'Don\'t pull if repository exists. [false]')
        parser.add_argument('-a', '--assignment', help=u'Assignment Prefix')
        return parser

    def make_github_agent(self, args):
        """ Create github agent to auth """
        if args.token:
            f = open(args.token, "r")
            myToken = f.readline().rstrip("\n\r")
            g = Github(myToken)
        else:
            user = args.user
            password = args.password
            if not user:
                user = input(u'Username: ')
            if not password:
                password = getpass('Password: ')
            if not args.dest:
                args.dest = input(u'Destination: ')
            g = Github(user, password)
        return g

    def clone_main(self):
        """ Clone all repos """
        parser = self.set_args()
        args = parser.parse_args()
        g = self.make_github_agent(args)
        user = g.get_user().login
        # (BadCredentialsException, TwoFactorException, RateLimitExceededException)

        join = path.join
        if args.dest:
            if not path.exists(args.dest):
                makedirs(args.dest)
                print(u'mkdir -p "{}"'.format(args.dest))
            join = partial(path.join, args.dest)

        get_repos = g.get_organization(args.org).get_repos if args.org else g.get_user().get_repos
        for repo in get_repos():
            match = re.search(args.assignment, repo.name)
            if not match:
                continue
            if not path.exists(join(repo.name)):
                print(u'Cloning "{repo.full_name}"'.format(repo=repo))
                call([u'git', u'clone', repo.clone_url, join(repo.name)])
            elif not args.nopull:
                print(u'Updating "{repo.name}"'.format(repo=repo))
                call([u'git', u'pull'], env=dict(environ, GIT_DIR=join(repo.name, '.git').encode('utf8')))
            else:
                print(u'Already cloned, skipping...\t"{repo.name}"'.format(repo=repo))
            # Repo should be cloned/updated now
            myDir = getcwd()
            chdir(repo.name)

            call([u'git', u'checkout', u'master'])
            gitResult = check_output([u'git', u'branch', '-r']).split()
            for branch in gitResult:
                match = re.search('HEAD|master|->', branch)
                if not (match):
                    match = re.search('origin/(\S+)', branch)
                    print("???\tIAState-gitim: Guessing branch to be " + match.group(1))
                    call([u'git', u'fetch', u'origin',  match.group(1)])
                    call([u'git', u'checkout', match.group(1)])
                    submitted = check_output([u'git', u'log', u'--remotes',  u'--format="%aN %aE %ad"', u'-1'])
                    print("???\tIAState-gitim: Guessing submission to be " + submitted)
            chdir(myDir)
        print(u'FIN')


if __name__ == '__main__':
    gitim = Gitim()
    gitim.clone_main()
