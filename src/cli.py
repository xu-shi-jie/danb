"""Command-line interface for danb."""

from downloader import main


def cli():
    """Entry point for the danb command-line tool."""
    return main()


if __name__ == "__main__":
    cli()