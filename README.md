# Weather Dashboard

## Overview

The Weather Dashboard is a Python-based application that fetches weather data for multiple cities from the OpenWeather API, formats the data, saves it as JSON files, and uploads the files to an AWS S3 bucket. This project demonstrates how to integrate various services and handle data processing and storage in a cloud environment.

## Features

- Fetches weather data from the OpenWeather API for multiple cities.
- Formats the weather data to include temperature, humidity, conditions, city name, and timestamp.
- Saves the formatted data as JSON files in a local directory.
- Upload the JSON files to a specified AWS S3 bucket.
- Logs the process and handles errors gracefully.

## Prerequisites

- Python 3.6 or higher
- AWS account with access to S3
- OpenWeather API key

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/weather-dashboard.git
cd weather-dashboard

To transfer the note to your README file, you can follow these steps:

1. Open your 

README.md

 file in your text editor.
2. Copy the detailed note provided.
3. Paste the note into your 

README.md

 file.
4. Save the file.

Here is the content to copy and paste into your 

README.md

 file:

```markdown
# Weather Dashboard

## Overview

The Weather Dashboard is a Python-based application that fetches weather data for multiple cities from the OpenWeather API, formats the data, saves it as JSON files, and uploads the files to an AWS S3 bucket. This project demonstrates how to integrate various services and handle data processing and storage in a cloud environment.

## Features

- Fetches weather data from the OpenWeather API for multiple cities.
- Formats the weather data to include temperature, humidity, conditions, city name, and timestamp.
- Saves the formatted data as JSON files in a local directory.
- Uploads the JSON files to a specified AWS S3 bucket.
- Logs the process and handles errors gracefully.

## Prerequisites

- Python 3.6 or higher
- AWS account with access to S3
- OpenWeather API key

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/weather-dashboard.git
cd weather-dashboard
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory of the project and add the following environment variables:

```properties
OPENWEATHER_API_KEY=your_openweather_api_key
AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_KEY=your_aws_secret_key
AWS_REGION=your_aws_region
S3_BUCKET_NAME=your_s3_bucket_name
```

Replace the placeholders with your actual API key and AWS credentials.

### 5. Add `.env` to 

.gitignore



Ensure that your `.env` file is not tracked by Git to keep your credentials secure. Add the following line to your 

.gitignore

 file:

```plaintext
.env
```

## Usage

### Running the Script

Activate the virtual environment if not already activated:

```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Run the script:

```bash
python src/weather_dashboard.py
```

### Enter Cities

When prompted, enter the cities separated by commas. For example:

```plaintext
Enter cities separated by commas: London, Abuja, Kent, Toronto, Tokyo, Japan, New York, Dubai, Berlin, Washington DC, Beijing
```

The script will fetch the weather data for each city, format it, save it as JSON files in the `data/` folder, and upload the files to the specified S3 bucket.

### Logs

The script logs the process and any errors encountered. The logs are printed to the console and include timestamps, log levels, and messages.

## Example Output

```plaintext
2025-01-07 22:00:44,980 - INFO - S3 client initialized successfully.
Enter cities separated by commas: London, Abuja, Kent, Toronto, Tokyo, Japan, New York, Dubai, Berlin, Washington DC, Beijing
2025-01-07 22:01:40,764 - INFO - Weather data fetched successfully for London.
2025-01-07 22:01:40,767 - INFO - Weather data saved to data/London_20250107220140.json
2025-01-07 22:01:40,969 - INFO - File data/London_20250107220140.json uploaded to S3 bucket weather-data-storage1
...
```

## Error Handling

The script includes error handling for various scenarios, such as missing environment variables, HTTP errors when fetching weather data, and errors when uploading files to S3. Errors are logged with appropriate messages to help diagnose issues.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
```

