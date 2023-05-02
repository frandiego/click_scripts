import subprocess
import click
import re


@click.group()
def aws():
    print


@aws.command()
def aws_show_profiles(
    path: str = "~/.aws/config",
    prefix_string: str = "profile",
    suffix_string: str = "]",
):
    string = str(subprocess.check_output(f"cat {path}", shell=True))
    positions = [(m.start(), m.end()) for m in re.finditer(prefix_string, string)]
    res = []
    for start, _ in positions:
        end = start + string[start:].find(suffix_string)
        word = string[start:end].replace(prefix_string, "")
        word = word.replace(suffix_string, "")
        res.append(word.strip())
    res_str = ", ".join(res)
    click.secho(res_str, blink=True, bold=True)


if __name__ == "__main__":
    aws()
