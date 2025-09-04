# Dog Breed Explorer 🐶

A Streamlit web application for exploring dog breed characteristics and
statistics.

## Features

- Interactive visualizations of dog breed data
- Scatter plots showing height vs weight relationships
- Bar charts displaying average lifespans by breed group
- Sunburst charts categorizing breeds by size and group
- Data export functionality

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run app.py
```

## Dependencies

- Streamlit >= 1.28.0
- Pandas >= 2.0.0
- Plotly >= 5.17.0

## Data Source

The app uses the local `breeds.csv` file containing dog breed information from
the Continental Kennel Club (CKC). No external database connection required!

## Deployment

This app is designed to be deployed on Streamlit Community Cloud. Simply push your
code to GitHub and deploy - no additional configuration needed!
