import os
import requests
import boto3
import logging
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()  # AWS Region: eu-west-2

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Constants
API_KEY = os.getenv("OPENWEATHER_API_KEY")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET_NAME")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
DATA_FOLDER = "data"

# Debug prints to check environment variables
logger.debug(f"API_KEY: {API_KEY}")
logger.debug(f"AWS_ACCESS_KEY: {AWS_ACCESS_KEY}")
logger.debug(f"AWS_SECRET_KEY: {AWS_SECRET_KEY}")
logger.debug(f"AWS_REGION: {AWS_REGION}")
logger.debug(f"S3_BUCKET: {S3_BUCKET}")

# Check if all required environment variables are set
if not all([API_KEY, AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET]):
    logger.error("One or more environment variables are missing.")
    raise EnvironmentError("One or more environment variables are missing.")

# Initialize S3 client
try:
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )
    logger.info("S3 client initialized successfully.")
except Exception as e:
    logger.error(f"Error initializing S3 client: {e}")
    raise

# Function to get weather data
def get_weather(city):
    url = f"{BASE_URL}?q={city}&units=imperial&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        logger.info(f"Weather data fetched successfully for {city}.")
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred for {city}: {http_err}")
        raise
    except Exception as err:
        logger.error(f"Other error occurred for {city}: {err}")
        raise

# Function to format weather data
def format_weather_data(data):
    formatted_data = {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "conditions": data["weather"][0]["description"],
        "city": data["name"],
        "timestamp": datetime.now().isoformat()
    }
    return formatted_data

# Function to save data to JSON file
def save_to_json(data, city):
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
    filename = f"{DATA_FOLDER}/{city}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(data, f)
    logger.info(f"Weather data saved to {filename}")
    return filename

# Function to upload file to S3
def upload_to_s3(filename):
    try:
        s3_client.upload_file(filename, S3_BUCKET, os.path.basename(filename))
        logger.info(f"File {filename} uploaded to S3 bucket {S3_BUCKET}")
    except Exception as e:
        logger.error(f"Error uploading file to S3: {e}")
        raise

# Main execution
if __name__ == "__main__":
    cities = input("Enter cities separated by commas: ").split(',')
    cities = [city.strip() for city in cities]  # Remove any leading/trailing whitespace
    for city in cities:
        try:
            weather_data = get_weather(city)
            formatted_data = format_weather_data(weather_data)
            json_filename = save_to_json(formatted_data, city)
            upload_to_s3(json_filename)
        except Exception as err:
            logger.error(f"Failed to process weather data for {city}: {err}")