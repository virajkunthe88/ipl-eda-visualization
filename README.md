# IPL EDA and Visualization

Exploratory Data Analysis and Visualization project for Indian Premier League (IPL) cricket data.

## Project Structure

```
IPL EDA and visualization/
├── data/              # Raw and processed data files
│   └── ipl_raw.csv    # Raw IPL match data (1169 matches)
├── notebooks/         # Jupyter notebooks for analysis
├── src/              # Python source code and modules
├── outputs/          # Generated visualizations and reports
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## Dataset Information

The IPL dataset contains **1,169 matches** from the Indian Premier League with the following features:

### Key Columns:
- **Teams**: `team1`, `team2`, `winner`, `toss_winner`
- **Match Details**: `match_date`, `season`, `match_number`, `match_type`
- **Result**: `result`, `result_margin`, `target_runs`, `target_overs`, `super_over`
- **Venue**: `venue`, `city`
- **Players**: `team1_players`, `team2_players`, `player_of_match`
- **Toss**: `toss_decision` (bat/field)

### Dataset Statistics:
- **Total Records**: 1,169 matches
- **Features**: 19 columns
- **Seasons Covered**: Multiple IPL seasons (starting from 2008)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start Jupyter Notebook:
```bash
jupyter notebook
```

3. Open or create notebooks in the `notebooks/` directory

## Requirements 

- Python 3.7+
- pandas >= 1.5.0
- numpy >= 1.23.0
- matplotlib >= 3.6.0
- seaborn >= 0.12.0
- jupyter >= 1.0.0
- plotly >= 5.14.0 (for interactive visualizations)

## Usage

1. Start by loading the data in a notebook:
```python
import pandas as pd
df = pd.read_csv('data/ipl_raw.csv')
```

2. Explore the data structure and begin your analysis

3. Save visualizations to the `outputs/` directory

## Analysis Goals

- Team performance analysis
- Player statistics and contributions
- Venue-based analysis
- Toss impact on match outcomes
- Season-wise trends
- Head-to-head team comparisons
