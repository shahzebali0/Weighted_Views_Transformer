# Weighted Views + Transformer for Molecular Learning

This repository contains the implementation of the Weighted Views framework combined with Transformer-based architectures for:
- QM7 molecular property prediction
- Enantiomer ranking using docking scores

---

## Repository Structure



```text
Weighted_Views_Transformer/
├── Code/
   ├── common_utils
        ├──  enantiomer_single_atom.py
        ├──  qm7_single_atom.py
        ├──  qm7_weightedviews.py
        ├──  views_test.py
        ├──  views_train.py
        ├──  views_val.py
   ├── Enantiomer_ranking
        ├──  Enantiomer _work.ipynb     
   ├── QM7
        ├── qm7_work.ipynb
        
│
├── notebooks/
│   ├── full_split.ipynb
│   │   └─ Enantiomer ranking using neural networks only
│   ├── fullsplit_singleproperties.ipynb
│   │   └─ Ranking with additional single atom properties
│   ├── data_information.ipynb
│   │   └─ Dataset analysis and statistics
│   └── chirality_transformer_coulomb.ipynb
│       └─ Transformer based model with Coulomb and chirality aware features
│
└── README.md
```


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

## QM7 Task

- **qm7_work**
  - Main file for property prediction analysis on the QM7 dataset

---

## Enantiomer Ranking Task

- **Enantiomer_work**
  - Main file for ranking enantiomers using docking scores

---

## Data

The `Data/` folder contains:

- **enantiomer_ranking/**
  - Sample dataset used in this study  
  - Full dataset: https://figshare.com/s/e23be65a884ce7fc8543  

- **qm7/**
  - Complete QM7 dataset  

---

## Results

The `Results/` folder contains:

- **enantiomer_ranking_results/**
  - Sample results for ranking task  

- **qm7_results/**
  - Sample results for QM7 prediction task  
