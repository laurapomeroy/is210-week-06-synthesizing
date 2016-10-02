#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Organizing a party"""


def get_party_stats(families, table_size=6):
    """Returns headcount for caterer and total number of tables

    Args:
        families(list): Lists families.
        table_size(int): Size of the table, 6.

    Returns:
        The headcount and total number of tables needed as a tuple.

    Examples:
    >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
    (6, 3)

    """
    totalguests = 0
    totaltables = 0
    for members in families:
        totalguests += len(members)
        totaltables += -(-len(members) // table_size)

    return (totalguests, totaltables)
