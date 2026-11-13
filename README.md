# GreenGrid: Big Data Analytics and Household Energy Consumption Forecasting

An academic project that analyses daily household electricity consumption and builds a Random Forest regression model to forecast `kwh`. The notebook also contains a single-node Apache Hadoop/HDFS setup and Hadoop Streaming jobs for household-wise, date-wise, and heating-type aggregations.

## Project overview

The project combines:

- **Apache Hadoop 3.5.0 and HDFS** for a single-node learning environment.
- **Hadoop Streaming** to run Python Mapper and Reducer scripts.
- **Pandas, NumPy, Matplotlib, and Seaborn** for preprocessing, exploratory data analysis, and visualisation.
- **Scikit-learn RandomForestRegressor** for daily electricity consumption prediction.

The target variable is `kwh`, measured in kilowatt-hours. The source dataset is synthetic; it does not contain real household customer records.

## Repository structure

```text
GreenGrid_Project/
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── sample_submission.csv
├── notebooks/
│   └── GreenGrid_Hadoop_Project.ipynb
├── src/
│   ├── mapper.py
│   └── reducer.py
├── outputs/
│   ├── daily_consumption_summary.csv
│   ├── heating_type_eda.csv
│   ├── model_metrics.csv
│   ├── greengrid_predictions.csv
│   └── charts/
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset

The notebook uses the supplied training and test files. The training data contains the `kwh` target; the test data is used to generate predictions. The notebook performs duplicate removal, date parsing, missing-value handling, and feature preparation.

> **Dataset redistribution:** Before publishing the CSV files publicly, verify the original dataset's licence and competition rules. If redistribution is not permitted, remove the CSV files from `data/` and add instructions for obtaining them from the authorised source.

## Running the notebook

### Recommended environment

The Hadoop portion of the notebook was authored for **Google Colab on a Linux runtime**, with Java 17 and Apache Hadoop 3.5.0. It uses Colab-specific paths such as `/content/` and shell commands (`!`, `%%writefile`). It is not a ready-to-run native Windows/VS Code notebook without adapting those environment-specific cells.

1. Open Google Colab.
2. Upload `notebooks/GreenGrid_Hadoop_Project.ipynb`.
3. Upload `data/train.csv` and `data/test.csv` to the Colab runtime (or update the notebook paths).
4. Run the cells from top to bottom.
5. Download the generated prediction and chart files from the runtime.

For VS Code, use a Python environment with the packages in `requirements.txt`. The ML and EDA sections can be adapted to local paths; the Hadoop setup section requires a Linux environment with Java and Hadoop correctly installed.

## Hadoop and MapReduce scope

The notebook configures a **single-node HDFS environment** (NameNode and DataNode on the same runtime) and invokes three Hadoop Streaming jobs:

1. Household-wise average electricity consumption.
2. Date-wise average electricity consumption.
3. Heating-type average electricity consumption.

`src/mapper.py` parses tab-separated key/value records. `src/reducer.py` calculates the average and record count for each key.

**Execution limitation:** The notebook records successful job-submission messages, but its later verification step reports the three final HDFS output files as missing after HDFS becomes unavailable. Therefore, this repository does not claim that the final Hadoop output files were persistently verified. Treat the Hadoop implementation as an executed single-node experiment whose final outputs need to be rerun and checked in a stable Hadoop environment.

## Machine learning

The notebook trains a `RandomForestRegressor` after date feature extraction and categorical encoding. It uses a chronological 80:20 train/validation split, reports MAE, RMSE, and R², displays feature importance, retrains on all labelled training rows, and writes test predictions to `greengrid_predictions.csv`.

Model metrics depend on the exact notebook run and environment; consult the notebook output rather than assuming fixed values.

## Reproducibility notes

- Keep the data files in `data/` and update paths in the notebook as needed.
- The notebook has Colab-specific setup commands and filesystem paths.
- Hadoop output persistence should be verified by checking each HDFS `part-00000` file after the jobs finish.
- Do not commit large generated model files or raw datasets unless their licences and repository size are suitable.

## Technologies

Python · Apache Hadoop · HDFS · Hadoop Streaming · MapReduce · Pandas · NumPy · Matplotlib · Seaborn · Scikit-learn · Random Forest Regression
