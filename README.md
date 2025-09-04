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

2. Set up your Supabase credentials in Streamlit secrets:

```toml
# .streamlit/secrets.toml
supabase_url = "your_supabase_url"
supabase_key = "your_supabase_key"
```

3. Run the app:

```bash
streamlit run app.py
```

## Dependencies

- Streamlit >= 1.28.0
- Pandas >= 2.0.0
- Plotly >= 5.17.0
- Supabase >= 2.18.0

## Data Source

The app connects to a Supabase database containing dog breed information from
the Continental Kennel Club (CKC).

## Deployment

This app is designed to be deployed on Streamlit Community Cloud. Make sure your
Supabase credentials are properly configured in the Streamlit Cloud secrets.
