# MINF-HCC

Nuclear features-based histological predictor of overall survival for resected hepatocellular carcinoma patients: a multicenter, retrospective study

Nuclear segmentation: https://github.com/vqdang/hover_net

## Abstract

Background &Aims: Nuclear features have been demonstrated to correlate with prognosis in numerous cancers. However, their prognostic value in hepatocellular carcinoma (HCC) remains unclear. This study aimed to develop and validate a nuclear features-based histological predictor of overall survival (OS) for HCC patients after hepatectomy.

Methods: Retrospective clinical and pathological data of 1125 HCC patients from four cohorts who underwent hepatectomy were collected. The multidimensional integrated nuclear feature (MINF) extracted from digitized hematoxylin and eosin (H&E)-stained whole-slide images (WSIs) was constructed based on a LASSO Cox regression model in the model development cohort (160 patients). The prognostic value of MINF was evaluated in the discovery cohort and three external validation cohorts (749 patients in total) through univariable and multivariable analyses.

Results: A set of 15 discriminative nuclear features were selected to construct MINF. In multivariable analysis, higher MINF was significantly associated with poorer OS in the discovery cohort (HR 2.24, [95% CI 1.77-2.83], p < 0.0001) and in the external validation cohort C1 (1.56, [1.32-1.85], p < 0.0001), C2 (1.36, [1.18-1.57], p < 0.0001), and C3 (1.31, [1.05-1.64], p = 0.0159). Furthermore, integrating MINF with clinicopathological variables could significantly enhance the prognostic performance compared to the clinicopathological variables in the discovery cohort (C-index, 0.810 vs. 0.715) and in the external validation cohort C1 (0.699 vs. 0.585), C2 (0.717 vs. 0.667), and C3 (0.696 vs. 0.640).

Conclusions: MINF serves as an independent prognostic biomarker, providing auxiliary diagnostic support for clinicians in HCC.

## Feature extraction

### conda install

`$ conda create --name MINF python=3.8`

`$ conda activate MINF`

`$ python -m pip install -r requirements.txt`

`$ cd MINF`

`$ python -m pip install -e .`

### run examples
`$ cd example`

`$ python example.py`
