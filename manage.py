#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from pathlib import Path

import environ


def main():
    BASE_DIR = Path(__file__).resolve().parent

    env = environ.Env()
    environ.Env.read_env(BASE_DIR / ".env")

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        env(
            "DJANGO_SETTINGS_MODULE",
            default="config.settings.development",
        ),
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
