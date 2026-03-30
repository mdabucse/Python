from utils.data_ingestion import load_data
from utils.preprocessing import handle_missing_values
from utils.feature_engineering import engineer_features
from utils.train import train_and_compare
import warnings
warnings.filterwarnings("ignore")


df = load_data("data/customer_data.csv")
df = handle_missing_values(df)
df = engineer_features(df)
train_and_compare(df)