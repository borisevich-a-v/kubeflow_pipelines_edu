import os
import sys

import click
import logging
from pathlib import Path
from minio import Minio

from kfp.components import InputPath, OutputPath

from config import config_logger

logger = logging.getLogger(__file__)

client = Minio("10.244.0.13:9000", "minio", "minio123", secure=False)


@click.command()
@click.option('--input-path')
@click.option('--output-images-path')
@click.option('--output-text-path')
def run(input_path: InputPath(str),
        output_images_path: OutputPath(str),
        output_text_path: OutputPath(str)
        ):
    logger.info(f'Run pdf preprocess on file {input_path} '
                f'with result dir images - {output_images_path} '
                f'and result dir text - {output_text_path}')

    input_path = input_path.lstrip('minio://')
    file_path = 'tmp/' + input_path.split('/')[-1]
    client.fget_object(bucket_name=input_path.split('/', maxsplit=1)[0],
                       object_name=input_path.split('/', maxsplit=1)[1],
                       file_path=file_path)
    file_path = Path(file_path)
    logger.info(f'Файл загружен из Minio, размер файла {file_path.stat().st_size}')

    logger.info('End')


if __name__ == '__main__':
    config_logger()
    run()
