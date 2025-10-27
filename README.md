# utils-crop_patch


# 🧩 Utils Crop Patch

This repository contains a set of Python utilities for **crop patch generation** and dataset preprocessing used in kidney stone image analysis experiments.  
The scripts automate the creation of cropped image patches at different resolutions for training and evaluation of deep learning models.

---

## 🚀 Features

- **Automatic patch generation** from large microscopy or endoscopic images  
- **Customizable patch size and overlap**
- **Support for multiple datasets and subtypes**
- **Utility functions** for dataset organization and analysis

---

## 📁 Data Organization

The dataset is expected to follow the structure below:

```bash
dataset/
├── SEC/
│   ├── train/
│   │   ├── SEC-Subtype_Ia/
│   │   ├── SEC-Subtype_IIa/
│   │   ├── SEC-Subtype_IIIa/
│   │   ├── SEC-Subtype_IVc/
│   │   ├── SEC-Subtype_IVd/
│   │   └── SEC-Subtype_Va/
│   └── test/
│       ├── SEC-Subtype_Ia/
│       ├── SEC-Subtype_IIa/
│       ├── SEC-Subtype_IIIa/
│       ├── SEC-Subtype_IVc/
│       ├── SEC-Subtype_IVd/
│       └── SEC-Subtype_Va/
└── SUR/
├── train/
└── test/
```


Each **subtype folder** must include:
- Original images: `.jpg`, `.png`, `.tif`, etc.  
- A **`mask/` subfolder** containing the corresponding segmentation masks.  
  Each mask should have the same name as its paired image (the file extension can differ).

---

## 🧠 Main Scripts

| Script | Description |
|---------|--------------|
| **crop_patch.py** | Main entry point for automatic crop patch generation. |
| **utils_functions.py** | Helper functions for estimating image counts, patch statistics, and folder handling. |
| **utils_make_patch_auto.py** | Automates patch extraction across multiple subtypes or datasets. |
| **utils_make_patch_on_images.py** | Core patch extraction logic (handles sliding windows, overlap, etc.). |

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/friscolt/utils-crop_patch.git
cd utils-crop_patch
pip install -r requirements.txt
```

## 🧩 Example Usage

```bash
python crop_patch.py \
    --dir /path/to/dataset/SEC/train/SEC-Subtype_Ia \
    --window_size 256 \
    --percent 0.8 \
    --req_patch 200
```


## 🧪 Requirements

See requirements.txt for the complete list of dependencies.


## ✨ Author

Francisco Lopez-Tiro
Researcher in deep learning and medical imaging