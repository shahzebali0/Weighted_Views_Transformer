
# Weighted Views Transformer for Molecular Learning
This repository contains the implementation of the Weighted Views framework combined with Transformer-based architectures for:
- QM7 molecular property prediction
- Enantiomer ranking using docking scores
- Lipophilicity prediction
- Blood-Brain Barrier Penetration (BBBP) classification
---
## Repository Structure
```text
Weighted_Views_Transformer/
├── Code/
   ├── common_utils
        └─  enantiomer_single_atom.py
        └─  qm7_single_atom.py
        └─  qm7_weightedviews.py
        └─  bbbp_single_atom.py
        └─  bbbp_weightedviews.py
        └─  lipo_single_atom.py
        └─  lipo_weightedviews.py
        └─  views_test.py
        └─  views_train.py
        └─  views_val.py
   ├── Enantiomer_ranking
        └─  Enantiomer_work.ipynb     
   ├── QM7
        └─ qm7_work.ipynb
   ├── BBBP
        └─ bbbp_work.ipynb
   ├── Lipophilicity
        └─ lipo_work.ipynb
├── Data/
│   ├── Enantiomer_ranking_dataset
│   │   └─   sample_test.pkl
        └─   sample_train.pkl
        └─   sample_val.pkl 
│   ├── QM7 dataset
│   │   └─ qm7.mat
│   ├── BBBP_dataset
│   │   └─ BBBP.csv
└── README.md
```
---
# Reproduction
## Molecule Property Prediction
1. Load `qm7_work.ipynb` along with:
   - `qm7_weightedviews.py`
   - `QM7_single_atom.py`
2. Load `qm7.mat` from the `Data/` folder.
3. `qm7_work.ipynb` contains the main analysis pipeline.
---
## Ranking Enantiomers by Docking Scores
1. Load `Enantiomer_work.ipynb` along with:
   - `enantiomer_single_atom.py`
   - `views_train.py`
   - `views_val.py`
   - `views_test.py`
2. Download the dataset from:
   https://figshare.com/s/e23be65a884ce7fc8543
3. A small sample dataset containing a few molecules is also available in the `Data/` folder for testing purposes.
---
## Predicting Lipophilicity
1. Load `lipo_work.ipynb` along with:
   - `lipo_weightedviews.py`
   - `lipo_single_atom.py`
2. Dataset is provided by AstraZeneca and available via MoleculeNet.
---
## Predicting Blood-Brain Barrier Penetration (BBBP)
1. Load `bbbp_work.ipynb` along with:
   - `bbbp_weightedviews.py`
   - `bbbp_single_atom.py`
2. Load `BBBP.csv` from the `Data/BBBP_dataset` folder.
---
## Utilities
### QM7 Utilities
- **qm7_weightedviews**
  - Generates weights and views for the QM7 dataset
  - Supports reduced view options:
    - Carbon as origin
    - Excluding hydrogen as origin
    - Heavy atom as origin
- **QM7_single_atom**
  - Generates broken views
  - Adds atomic properties
---
### Enantiomer Ranking Utilities
- **views_train, views_val, views_test**
  - Generate weights and views for training, validation, and test sets
- **enantiomer_single_atom**
  - Generates broken views
  - Adds atomic properties
---
### Lipophilicity Utilities
- **lipo_weightedviews**
  - Generates weights and views for the Lipophilicity dataset
- **lipo_single_atom**
  - Generates broken views
  - Adds atomic properties
---
### BBBP Utilities
- **bbbp_weightedviews**
  - Generates weights and views for the BBBP dataset
- **bbbp_single_atom**
  - Generates broken views
  - Adds atomic properties
---
## QM7 Task
- **qm7_work**
  - Main file for property prediction analysis on the QM7 dataset
---
## Enantiomer Ranking Task
- **Enantiomer_work**
  - Main file for ranking enantiomers using docking scores
---
## Lipophilicity Task
- **lipo_work**
  - Main file for lipophilicity regression analysis
---
## BBBP Task
- **bbbp_work**
  - Main file for blood-brain barrier penetration classification
---
## Data
The `Data/` folder contains:
- **Enantiomer_ranking_dataset/**
  - Sample dataset used in this study  
  - Full dataset: https://figshare.com/s/e23be65a884ce7fc8543  
- **QM7 dataset/**
  - Complete QM7 dataset
- **BBBP_dataset/**
  - BBBP.csv used in this study
---
