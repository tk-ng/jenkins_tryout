"""Module setup init enviorment for behave"""

import os


def before_all(context):
    """Function for hook before test run"""
    counts = {
        "ticket_count": os.getenv("TICKETS_NOT_ENTERED", "1"),
        "ticket_entered_count": os.getenv("TICKETS_ENTERED", "1"),
        "pass_count": os.getenv("PASSES_NOT_ENTERED", "1"),
        "pass_entered_count": os.getenv("PASSES_ENTERED", "1"),
    }
    for k, v in counts.items():
        setattr(context, k, int(v) if v.isdigit() else 0)


def after_all(context):
    """Function for hook after test run"""
    context.config = None
