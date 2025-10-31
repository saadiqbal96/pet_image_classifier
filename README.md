# Pet Image Classifier

A Python project for classifying pet images using CNN models (VGG, ResNet, AlexNet).  
This project extracts pet labels from image filenames, compares them to classifier outputs, and checks if the labels correspond to dogs.

---

## **Project Structure**

- `main.py` → Main script that runs the program.  
- `get_pet_labels.py` → Extracts pet labels from image filenames.  
- `classify_images.py` → Classifies images and compares with pet labels.  
- `check_images.py` → Optional: prints detailed results.  
- `dognames.txt` → List of dog names for classification.  
- `run_models_batch.sh` → Runs the program with different CNN models.  

---

## **How to Use**

1. Make sure your pet images are in a folder called `pet_images/`.  
2. Run the main script:

```bash
python3 main.py

bash run_models_batch.sh

---

If you paste this into GitHub as `README.md`, your repo will instantly look professional and explain everything clearly.  

