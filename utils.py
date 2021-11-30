import requests
import percache
import os
import logging

cache = percache.Cache(".cache")


def error(*args):
    logging.error(args if len(args) > 1 else args[0], stacklevel=3)


def warning(*args):
    logging.warning(args if len(args) > 1 else args[0], stacklevel=3)


def info(*args):
    logging.info(args if len(args) > 1 else args[0], stacklevel=3)


@cache
def get_input(day, no_split=False):
    assert os.getenv(
        "AOC_SESSION"
    ), "Set the session cookie environment variable (export AOC_SESSION='your session cookie')"
    warning("Fetching from server")
    result = requests.get(
        f"https://adventofcode.com/2021/day/{day}/input",
        cookies={"session": os.getenv("AOC_SESSION")},
    )
    assert result.status_code == 200, result.text
    if no_split:
        return result.text
    return result.text.splitlines()


def get_int_input(day):
    res = get_input(day)
    return [int(r) for r in res]
