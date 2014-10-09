"""Utilities for getting CPU related metrics."""
import os

import decimal
import commands


def get_cpu_usage(user=None, ignore_self=True):
    """
    Returns the total CPU usage for all available cores.

    :param user: If given, returns only the total CPU usage of all processes
      for the given user.
    :param ignore_self: If ``True`` the process that runs this script will
      be ignored.

    """
    pid = os.getpid()
    cmd = "ps aux"
    output = commands.getoutput(cmd)
    total = 0
    largest_process = 0
    largest_process_name = None
    for row in output.split('\n')[1:]:
        row = row.split()
        if row[1] == str(pid):
            continue
        if user is None or user == row[0]:
            cpu = decimal.Decimal(row[2])
            if cpu > total:
                largest_process = cpu
                largest_process_name = row[10]
            total += decimal.Decimal(row[2])
    return (total, largest_process, largest_process_name)
