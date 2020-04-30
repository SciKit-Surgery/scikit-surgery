# coding=utf-8

"""Command line processing"""


import argparse
from sksurgery import __version__
from sksurgery.ui.sksurgery_demo import run_demo


def main(args=None):
    """Entry point for scikit-surgery application"""

    parser = argparse.ArgumentParser(description='scikit-surgery')

    parser.add_argument("-t", "--text",
                        required=False,
                        default="This is scikit-surgery",
                        type=str,
                        help="Text to display")

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "-v", "--version",
        action='version',
        version='scikit-surgery version ' + friendly_version_string)

    args = parser.parse_args(args)

    run_demo(args.text)
