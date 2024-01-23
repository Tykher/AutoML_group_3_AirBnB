from joblib import load
import pandas as pd


model_filename = 'rf_hyper_model.joblib'
# Load the model from disk
loaded_model = load(model_filename)
feature_names = ['person_capacity', 'multi', 'biz', 'cleanliness_rating', 'guest_satisfaction_overall', 'bedrooms', 'dist', 'metro_dist', 'city', 'host_is_superhost', 'room_type']
sample_input = [2, 1, 0, 10, 93, 1, 5, 2, 0, 0, 1]
sample_input_df = pd.DataFrame([sample_input], columns=feature_names)
prediction_single_sample = loaded_model.predict(sample_input_df)
print(f"Prediction for single sample: {prediction_single_sample}")