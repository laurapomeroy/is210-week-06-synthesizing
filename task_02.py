#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Sending automated e-mails"""


def prepare_email(appointments):
    """Send a reminder e-mail blast to each client by capturing client name and
    time

    Args:
        appointments(list): A list of two-item tuples with the client's name and
        appointment time

    Returns:
        Returns a list with the client's e-mail body

    Example:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['DearJen,\nI look forward to meeting with you on2015.\nBest,\nMe',
        'DearMax,\nI look forward to meeting with you onMarch 3.\nBest,\nMe']

    """

    email = []
    body = 'Dear{},\nI look forward to meeting with you on{}.\nBest,\nMe'
    for client in appointments:
        email.append(body.format(client[0], client[1]))

    return email
