import pandas as pd
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate with Kaggle API
api = KaggleApi()
api.authenticate()

# Download dataset from Kaggle (adjust dataset name accordingly)
dataset_name = 'olistbr/brazilian-ecommerce'
output_dir = './data/olist_dataset'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download the dataset
api.dataset_download_files(dataset_name, path=output_dir, unzip=True)

print(f"Dataset downloaded and extracted to {output_dir}")



