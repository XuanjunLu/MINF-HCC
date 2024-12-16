#!/usr/bin/env python

from __future__ import print_function
import os
import openslide
import logging

import pathomics
from pathomics import featureextractor
import pandas as pd

import multiprocessing
from multiprocessing import Pool, Manager
from itertools import repeat

from pathomics.helper import save_mat_mask, save_matfiles_info_to_df, select_image_mask_from_src, save_results_to_pandas

import warnings
warnings.filterwarnings("ignore")
# Get the Pypathomics logger (default log-level = INFO)
logger = pathomics.logger
logger.setLevel(
    logging.DEBUG
)  # set level to DEBUG to include debug log messages in log file

# Set up the handler to write out all log entries to a file
handler = logging.FileHandler(filename='testLog.txt', mode='w')
formatter = logging.Formatter("%(levelname)s:%(name)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# Define settings for signature calculation
# These are currently set equal to the respective default values
settings = {}


def run(imageName, maskName, features):
    # Initialize feature extractor
    extractor = featureextractor.PathomicsFeatureExtractor(**settings)

    # Disable all classes except histoqc
    extractor.disableAllFeatures()

    # Only enable morph in nuclei
    extractor.enableFeaturesByName(**features)

    try:
        featureVector = extractor.execute(imageName, maskName, ifbinarization=False)
        return featureVector
    except Exception as e:
        return None


if __name__ == '__main__':
    import time
    start = time.time()
    # Step 1: set enabled features and basic parameters
    features = dict(flock=[], morph=[], haralick=[])      # flock=[], morph=[], haralick=[]
    n_workers = 4
    # patient_id = '1918911'
    image_dir = rf"../test_folder/image"
    save_dir = rf"../test_folder/save_dir"
    os.makedirs(save_dir, exist_ok=True)

    # Step 2: convert mat-format nuclear masks into png files
    mat_dir = rf"../test_folder/mat"
    mat_var_name = 'inst_map'
    png_mask_save_dir = rf'{save_dir}/mask'
    png_mask_filepaths = save_mat_mask(mat_dir, mat_var_name,
                                       png_mask_save_dir, n_workers)

    # Step 3: filter patches, get first 400 patches with max nuclear size
    select_size = 400
    info_name = 'inst_type'
    only_ndarray_size = True
    target_value = None
    save_info_path = rf'{save_dir}/{info_name}.csv'
    df = save_matfiles_info_to_df(mat_dir, n_workers, info_name,
                                  only_ndarray_size, target_value, save_info_path)
    sort_col_name = info_name + f'_size'
    df = df.sort_values(by=sort_col_name, ascending=False, key=lambda col: col)
    save_results_to_pandas(df, save_info_path)
    select_names = list(df['name'])[:select_size]

    save_select_filepaths_info = rf'{save_dir}/top_400_nuclear_size_files.csv'
    image_paths, mask_paths = select_image_mask_from_src(
        select_names, image_dir, '.png', png_mask_save_dir, '.png',
        save_select_filepaths_info)

    # Step 4: compute features by multiprocessing
    with Pool(processes=n_workers) as pool:
        featureVectors = pool.starmap(
            run,
            zip(image_paths, mask_paths, repeat(features, len(image_paths))))

    # Step 5: save results
    save_results_csv_path = rf'{save_dir}/40x_patch_nuclear_feat.csv'
    data = {}
    # data['patient_id'] = []
    data['patch_id'] = []
    for i in range(len(featureVectors)):
        if featureVectors[i] is None:
            continue
        # data['patient_id'].append(patient_id)
        data['patch_id'].append(select_names[i])
        for feature_name, feature_value in featureVectors[i].items():
            if data.get(feature_name) is None:
                data[feature_name] = [feature_value]
            else:
                data[feature_name].append(feature_value)

    df = save_results_to_pandas(data, save_results_csv_path)
    end = time.time()
    print('time:', (end-start)/60)
