# A comparative study of fairness methods for clinical predictions using the MIMIC-IV database
This repository contains the Jupyter notebooks that make up the coding portion of the thesis work conducted to fulfill the requirements for the master's degree in data science from the University of Barcelona as supervised by Dr. Laura Igual Muñoz. Additionally, it contains the [thesis report](./docs/report.pdf), which provides an in-depth description of the study, and the presentation slides (coming soon), which provide a concise summary of the work.

Fairness-aware interpretable modeling (FAIM) [1] is an in-processing fairness method that avoids extreme performance degradation while improving fairness and maintaining interpretability. This study consists of the reproduction of the results reached in the original FAIM paper with the clinical prediction task of hospital admission after emergency department (ED) stay utilizing the code provided in [2], followed by stress-testing the FAIM method with the distinct task of invasive mechanical ventilation (IMV) prediction as inspired by [3]. For the purpose of this study, we use real-world clinical data from the [MIMIC-IV database](https://mimic.mit.edu/). In addition to comparing the "fairness-aware" FAIM model to the "fairness-unaware" baseline logistic regression model, we also compare fairness metrics among other state-of-the-art fairness methods, namely: Unawareness, Reweighing, Reductions, Equalized Odds, Calibrated Equalized Odds, Reject Option Classifier and Adversarial Learning. 

## Notebooks:
For the replication, we first [re-create the dataset](./notebooks/replication/hosp_admission_dataset.ipynb) used in the original task of hospital admission following the code provided in [4]. Then we do [bias analysis](./notebooks/replication/hosp_admission_bias_analysis.ipynb) to ensure that there is bias in the original task before running the [FAIM workflow](./notebooks/replication/hosp_admission_faim_workflow.ipynb) to get final results. Separately, we get [adversarial learning results](./notebooks/replication/hosp_admission_adversarial_fairness.ipynb) following [5] to insert into our fairness methods comparison table. 

Similarly, for the new clinical task of IMV allocation prediction, we [create a dataset](./notebooks/imv/imv_dataset.ipynb) extracting clinically relevant features, do an inital [bias analysis](./notebooks/imv/imv_bias_analysis.ipynb) beforehand, get [adversarial learning results](./notebooks/imv/imv_adversarial_fairness.ipynb), and finally run the [FAIM workflow](./notebooks/imv/imv_task_faim_workflow.ipynb).


## References
[1] M. Liu et al., "FAIM: Fairness-aware interpretable modeling for trustworthy machine learning in healthcare," *Patterns*, vol. 5, Oct. 2024. https://doi.org/10.1016/j.patter.2024.241059

[2] NliuLab, “FAIM: Fairness-aware interpretable modeling.” GitHub repository, 2025. Available: https://github.com/nliulab/FAIM

[3] F. M. Abdelmalek et al., "Association between patient race and ethnicity and use of invasive ventilation in the United States," *Ann. Am. Thorac. Soc.*, vol. 21, no. 2, pp. 287-295, Feb. 2024. https://doi.org/10.1513/AnnalsATS.202305-485OC

[4] NliuLab, “mimic4ed-benchmark.” GitHub repository, 2022. Available: https://github.com/nliulab/mimic4ed-benchmark

[5] Yang, J., "Adversarial Learning Bias Mitigation," GitHub repository. https://github.com/yangjenny/adversarial_learning_bias_mitigation
 
