"""Module is runner of behave"""
import sys
from behave.__main__ import main as behave_main

if __name__ == "__main__":
    ARGS = "--no-capture --no-capture-stderr --no-logcapture " + \
      "--show-timings " + \
      "features/ticket_utility/auto_gen_ticket_pass.feature "
    behave_main(ARGS)
    sys.exit(0)
