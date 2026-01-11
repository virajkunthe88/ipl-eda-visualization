"""
Initial Data Exploration Script for IPL Dataset
This script provides a quick overview of the IPL dataset structure and basic statistics.
"""

import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('../data/ipl_raw.csv')

print("="*80)
print("IPL DATASET - INITIAL EXPLORATION")
print("="*80)
print()

print(f"Dataset Shape: {df.shape}")
print(f"Total Records: {df.shape[0]:,}")
print(f"Total Features: {df.shape[1]}")
print()

print("="*80)
print("COLUMN INFORMATION")
print("="*80)
print(df.info())
print()

print("="*80)
print("DESCRIPTIVE STATISTICS")
print("="*80)
print(df.describe())
print()

print("="*80)
print("FIRST FEW ROWS")
print("="*80)
print(df.head())
print()

print("="*80)
print("MISSING VALUES")
print("="*80)
missing = df.isnull().sum()
print(missing[missing > 0])
if missing.sum() == 0:
    print("No missing values found!")
print()

print("="*80)
print("UNIQUE VALUES - CATEGORICAL COLUMNS")
print("="*80)
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    unique_count = df[col].nunique()
    print(f"{col}: {unique_count} unique values")
    if unique_count < 20:
        print(f"  Values: {df[col].unique()}")
    print()

print("="*80)
print("SEASON DISTRIBUTION")
print("="*80)
print(df['season'].value_counts().sort_index())
print()

print("="*80)
print("MATCH TYPE DISTRIBUTION")
print("="*80)
print(df['match_type'].value_counts())
print()

print("="*80)
print("TOP 10 VENUES BY MATCH COUNT")
print("="*80)
print(df['venue'].value_counts().head(10))
print()
