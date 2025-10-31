#!/bin/bash
echo "Running models batch..."
python3 main.py --arch vgg
python3 main.py --arch resnet
python3 main.py --arch alexnet
