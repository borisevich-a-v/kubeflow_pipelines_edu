import click
import logging
import sys
from pathlib import Path

from kfp.components import InputPath, OutputPath

LOGGER = logging.getLogger(__file__)

LOGGING_FORMAT = "[%(asctime)s] - [%(name)s] - [%(levelname)s] - %(message)s"


def configure_logging():
    formatter = logging.Formatter(LOGGING_FORMAT)
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(formatter)
    file_handler = logging.FileHandler(
        Path(__file__).parents[1].joinpath("python_logging.log").absolute()
    )
    file_handler.setFormatter(formatter)
    logging.root.setLevel(logging.DEBUG)
    logging.root.addHandler(console_handler)
    logging.root.addHandler(file_handler)


@click.command()
def run(input_path: InputPath(str),
        output_images_path: OutputPath(str),
        output_text_path: OutputPath(str)):
    LOGGER.info('Begin')

    LOGGER.info('End')


if __name__ == '__main__':
    configure_logging()
    run()
