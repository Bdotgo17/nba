# NBA Predictor

This project is designed to predict outcomes of NBA games using machine learning techniques. It includes data loading, feature engineering, model training, and prediction functionalities.

## Project Structure

```
nba-predictor
├── src
│   ├── __init__.py
│   ├── data
│   │   └── loader.py
│   ├── features
│   │   └── build_features.py
│   ├── models
│   │   └── train.py
│   ├── predict.py
│   └── utils.py
├── data
│   ├── raw
│   └── processed
├── notebooks
│   └── exploratory.ipynb
├── models
├── tests
│   ├── test_data.py
│   └── test_models.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/nba-predictor.git
   cd nba-predictor
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Load the data using the functions in `src/data/loader.py`.
2. Build features from the raw data using `src/features/build_features.py`.
3. Train your model with `src/models/train.py`.
4. Make predictions using the trained model with `src/predict.py`.

## Notebooks

The `notebooks/exploratory.ipynb` file contains exploratory data analysis and visualizations to help understand the data better.

## Testing

Unit tests are provided in the `tests` directory. You can run the tests using:
```
pytest tests/
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.