import requests
import percache
import os
from bs4 import BeautifulSoup
from rich.console import Console

cache = percache.Cache(".cache")
console = Console()

URL = "https://adventofcode.com/2021"


@cache
def submit(day: int, level: int, answer: any):
    assert os.getenv(
        "AOC_SESSION"
    ), "Set the session cookie environment variable (export AOC_SESSION='your session cookie')"
    console.log(f"Posting [bold]{answer}[/bold] for {day=} {level=}")
    result = requests.post(
        f"{URL}/day/{day}/answer",
        dict(level=level, answer=answer),
        cookies={"session": os.getenv("AOC_SESSION")},
    )
    assert result.status_code == 200, result.text
    soup = BeautifulSoup(result.text, features="html.parser")
    print(soup.body.main.article.prettify())


@cache
def get_input(day, no_split=False):
    assert os.getenv(
        "AOC_SESSION"
    ), "Set the session cookie environment variable (export AOC_SESSION='your session cookie')"
    console.log("Fetching from server")
    result = requests.get(
        f"{URL}/day/{day}/input",
        cookies={"session": os.getenv("AOC_SESSION")},
    )
    assert result.status_code == 200, result.text
    if no_split:
        return result.text
    return result.text.splitlines()


def get_int_input(day):
    res = get_input(day)
    return [int(r) for r in res]
