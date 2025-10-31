import time
import argparse
from get_pet_labels import get_pet_labels
from classify_images import classify_images

# Start timer
start_time = time.time()

# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default='pet_images/', help='Directory of pet images')
parser.add_argument('--arch', type=str, default='vgg', help='CNN model architecture')
parser.add_argument('--dogfile', type=str, default='dognames.txt', help='File containing dog names')
in_arg = parser.parse_args()

# Get pet labels
results = get_pet_labels(in_arg.dir)

# Classify images
results = classify_images(results, in_arg.dir, in_arg.arch, in_arg.dogfile)

# Stop timer
end_time = time.time()
print(f"\nElapsed runtime: {end_time - start_time:.2f} seconds")

# Display sample results
for k, v in list(results.items())[:5]:
    print(f"{k}: {v}")
