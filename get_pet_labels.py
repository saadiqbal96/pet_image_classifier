import os

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (key) and a list with the label (value).
    """
    results = {}
    filenames = os.listdir(image_dir)
    for filename in filenames:
        if filename.startswith('.'):
            continue
        label = " ".join([word.lower() for word in filename.split("_") if word.isalpha()]).strip()
        results[filename] = [label]
    return results
