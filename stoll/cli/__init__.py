# SPDX-FileCopyrightText: 2021-present Ofek Lev <oss@ofek.dev>
#
# SPDX-License-Identifier: MIT
import click

from stoll._version import version
from stoll.fib import fibonacci


# NOTE: The group/command decorators must come last to avoid the following issue at runtime:
# https://github.com/pallets/click/issues/1199


@click.version_option(version=version, prog_name='stoll')
@click.group()
def stoll_cli():
    click.echo("RUNNING STOLL_CLI")
    pass


@click.argument('n', type=int)
@stoll_cli.command()
def fib(n: int):
    click.echo("RUNNING fib")
    click.echo(fibonacci(n))
