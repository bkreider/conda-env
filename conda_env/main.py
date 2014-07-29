# (c) 2014 Continuum Analytics, Inc. / http://continuum.io
# All Rights Reserved
#
# conda is distributed under the terms of the BSD 3-clause license.
# Consult LICENSE.txt or http://opensource.org/licenses/BSD-3-Clause.

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys
import argparse
import os.path

import conda_api

from conda_env import __version__

def main():
    p = argparse.ArgumentParser(
        description='tool for managing conda environments'
    )

    p.add_argument(
        '-l', '--list',
        action="store_true",
        help="""only run the build, without any post processing or
testing. Implies --no-test and --no-binstar-upload""",
    )
    p.add_argument(
        '-V', '--version',
        action='version',
        version = 'conda-env %s' % __version__,
    )
    p.add_argument(
        '-q', "--quiet",
        action="store_true",
        help="do not display progress bar",
    )
    p.add_argument(
        '-d', '--delete',
        action="store_true",
        help="""## Not Implemeted ##:  delete the environment"""
    )

    p.set_defaults(func=execute)

    args = p.parse_args()
    args_func(args, p)

def execute(args, parser):

    if args.list:
        envs = conda_api.get_envs()

        for env in envs:
            base = os.path.basename(env)

            # skip system envs
            if base[0] != "_":
                print(base)
        return

    if args.delete:
        raise NotImplementedError

    print("No command found")
    return

def args_func(args, p):
    try:
        args.func(args, p)
    except RuntimeError as e:
        sys.exit("Error: %s" % e)
    except Exception as e:
        if e.__class__.__name__ not in ('ScannerError', 'ParserError'):
            message = """\
An unexpected error has occurred, please consider sending the
following traceback to the conda GitHub issue tracker at:

https://github.com/conda/conda-env/issues

Include the output of the command 'conda info' in your report.

"""
            print(message, file=sys.stderr)
        raise # as if we did not catch it

if __name__ == '__main__':
    main()
