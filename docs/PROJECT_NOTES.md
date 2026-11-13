# Project notes

- Dataset: synthetic household energy-consumption records.
- Target: `kwh` (daily household electricity consumption).
- Hadoop environment: single-node Google Colab runtime, Hadoop 3.5.0, Java 17.
- MapReduce groups: `household_id`, `date`, and `heating_type`.
- ML model: Scikit-learn Random Forest Regression.
- Validation: chronological 80:20 split.
- Final HDFS output directories were not verified as persistent in the notebook's final verification cell; rerun and verify them before claiming validated MapReduce outputs.
