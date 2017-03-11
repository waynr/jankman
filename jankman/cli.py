# -*- coding: utf-8 -*-

import logging

import click


logger = logging.getLogger(__name__)


@click.command()
@click.option("-v",
              help="Set verbosity. Once for INFO, twice for DEBUG.",
              default=0,
              count=True)
@click.option("--conf",
              help="path to configuration file",
              default="./jankman.conf")
def main(v, conf, args=None):
    """Console script for jankman"""
    lvl = None
    if v > 0:
        lvls = [
            logging.INFO,
            logging.DEBUG,
        ]
        lvl = lvls[v-1]
        logging.basicConfig(level=lvl)
    logger.addFilter(logging.Filter('jankman'))


if __name__ == "__main__":
    main()
