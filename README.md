<div align="center">

# Deep learning template based on Hydra and Pytorch Lightning for MRI reconstruction

[![python](https://img.shields.io/badge/-Python_3.8_%7C_3.9_%7C_3.10-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pytorch](https://img.shields.io/badge/PyTorch_2.0+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
[![lightning](https://img.shields.io/badge/-Lightning_2.0+-792ee5?logo=pytorchlightning&logoColor=white)](https://pytorchlightning.ai/)
[![hydra](https://img.shields.io/badge/Config-Hydra_1.3-89b8cd)](https://hydra.cc/)
[![black](https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray)](https://black.readthedocs.io/en/stable/)
[![isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/) <br>
[![tests](https://github.com/ashleve/lightning-hydra-template/actions/workflows/test.yml/badge.svg)](https://github.com/ashleve/lightning-hydra-template/actions/workflows/test.yml)
[![code-quality](https://github.com/ashleve/lightning-hydra-template/actions/workflows/code-quality-main.yaml/badge.svg)](https://github.com/ashleve/lightning-hydra-template/actions/workflows/code-quality-main.yaml)
[![codecov](https://codecov.io/gh/ashleve/lightning-hydra-template/branch/main/graph/badge.svg)](https://codecov.io/gh/ashleve/lightning-hydra-template) <br>
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/ashleve/lightning-hydra-template#license)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/ashleve/lightning-hydra-template/pulls)
[![contributors](https://img.shields.io/github/contributors/ashleve/lightning-hydra-template.svg)](https://github.com/ashleve/lightning-hydra-template/graphs/contributors)

Absolutely! Here’s a **GitHub README.md** draft for your paper based on the provided IEEE manuscript. I’ve crafted it to be informative and professional while also maintaining clarity and readability for the open-source community.

---

# Longitudinal Brain MRI Deep Reconstruction

**Enhancing and Accelerating Brain MRI through Deep Learning Reconstruction Using Prior Subject-Specific Imaging**

[![Paper DOI Badge](https://img.shields.io/badge/DOI-Published-blue)](https://ieeexplore.ieee.org/document/XXXXXXX)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📖 Overview

This repository contains the code for the paper:
**"Enhancing and Accelerating Brain MRI through Deep Learning Reconstruction Using Prior Subject-Specific Imaging"**, by Amirmohammad Shamaei et al., IEEE Journal of Biomedical and Health Informatics.

**Abstract:**
Magnetic Resonance Imaging (MRI) is a critical tool in medical imaging but is often hindered by lengthy acquisition times. We present a deep learning framework that accelerates MRI reconstruction by incorporating prior subject-specific imaging, leveraging both deep registration (EasyReg) and transformer-based enhancement networks. This approach yields superior reconstruction quality and significantly reduces processing time compared to traditional methods, enhancing its suitability for real-time clinical applications.

---

## 🖼️ Key Features

✅ **Deep-learning-based Registration** — Uses the EasyReg model to efficiently align prior subject-specific MRI scans.
✅ **Transformer-based Enhancement Network** — Utilizes self-attention mechanisms to capture long-range dependencies and refine reconstruction.
✅ **Longitudinal MRI Dataset** — Validated on a dataset with 2,808 T1-weighted MRI slices from 18 subjects.
✅ **Multi-Acceleration Factors** — Tested at R5, R10, R15, R20.
✅ **Downstream Segmentation Analysis** — Demonstrates improved accuracy and volumetric agreement with reference segmentations.
✅ **Fast Processing Time** — Average registration time reduced to \~4.1 seconds (compared to \~90 seconds using linear registration).

---

## 📂 Repository Structure

```bash
longitudinal-mri-deep-recon/
│
├── models/
│   ├── e2evarnet.py        # Initial reconstruction network (E2E-VarNet)
│   ├── easyreg.py          # Deep registration network
│   └── transformer_net.py  # Transformer-based enhancement network
│
├── datasets/
│   ├── preprocessing.py    # Data preprocessing utilities
│   └── loaders.py          # Data loaders for MRI slices
│
├── training/
│   ├── train_reconstruction.py   # Training script for E2E-VarNet
│   ├── train_enhancement.py      # Training script for enhancement network
│
├── evaluation/
│   ├── metrics.py          # SSIM, PSNR, NRMSE calculations
│   ├── segmentation_eval.py # Segmentation analysis pipeline
│
├── utils/
│   └── helpers.py          # Utility functions
│
├── README.md
└── LICENSE
```

---

## 🚀 Getting Started

1. **Clone this repository**

   ```bash
   git clone https://github.com/amirshamaei/longitudinal-mri-deep-recon.git
   cd longitudinal-mri-deep-recon
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Data Preparation**

   * Use your dataset of undersampled k-space MRI data.
   * Organize prior subject-specific images (stored in PACS) as described in the paper.

4. **Training**

   * Train the initial reconstruction network:

     ```bash
     python training/train_reconstruction.py --config configs/e2evarnet_config.yaml
     ```
   * Train the enhancement network:

     ```bash
     python training/train_enhancement.py --config configs/transformer_config.yaml
     ```

5. **Evaluation**

   * Run the evaluation scripts to compute SSIM, PSNR, NRMSE, and segmentation metrics.

---

## 📊 Results

Our method outperforms traditional linear registration-based reconstructions on all metrics (SSIM, PSNR, NMSE) across all acceleration factors (R5, R10, R15, R20). It also shows improved agreement with reference segmentation masks.

See **Figures 2-6** in the [paper](https://ieeexplore.ieee.org/document/XXXXXXX) for detailed results and comparisons.

---

## 📎 Paper Link

For more details, please refer to the published paper:

> Shamaei, A. et al. "Enhancing and Accelerating Brain MRI through Deep Learning Reconstruction Using Prior Subject-Specific Imaging." *IEEE Journal of Biomedical and Health Informatics*, 2025.

**Preprint available upon request.**

---

## 📌 Citation

If you use this code in your work, please cite:

```bibtex
@article{Shamaei2025LongMRIRecon,
  author = {Amirmohammad Shamaei and Alexander Stebner and Salome Bosshart and Johanna Ospel and Gouri Ginde and Mariana Bento and Roberto Souza},
  title = {Enhancing and Accelerating Brain MRI through Deep Learning Reconstruction Using Prior Subject-Specific Imaging},
  journal = {IEEE Journal of Biomedical and Health Informatics},
  year = {2025},
  note = {doi:10.1109/JBHI.2025.xxxxx}
}
```

---

## 🔗 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💬 Contact

For questions or collaborations, please contact:
Amirmohammad Shamaei – [amirmohammad.shamaei@ucalgary.ca](mailto:amirmohammad.shamaei@ucalgary.ca)

---

Let me know if you’d like to expand any section (e.g. add installation instructions, demo scripts, screenshots) or tailor it to your audience! 🚀
