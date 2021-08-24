#!/bin/bash -e
export image_name=preprocess_pipeline
export image_tag=latest
export full_image_name=${image_name}:${image_tag}

cd "$(dirname "$0")"
docker login
docker build -t "${full_image_name}" .
docker tag $full_image_name tinker000/simple_pipeline:$image_tag
docker push tinker000/simple_pipeline:$image_tag

