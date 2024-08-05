## Redis to S3 Exporter

This Python script exports the keys and values of a Redis database to an S3 bucket. The script uses the redis and boto3
Python libraries to interact with Redis and AWS S3, respectively.

### Installation

To use this script, you'll need to have Python 3 installed on your system, as well as the redis and boto3 Python
libraries. You can install these libraries using pip:

```sh
pip install redis boto3
```

### Configuration

The script uses a config.yaml file to manage connections to Redis and S3. The file should be placed in the same
directory as the script. Here's an example config.yaml file:

```yaml
redis:
  host: YOUR_REDIS_HOST
  port: YOUR_REDIS_PORT
  db: YOUR_REDIS_DATABASE
  password: YOUR_REDIS_PASSWORD

s3:
  aws_access_key_id: YOUR_AWS_ACCESS_KEY_ID
  aws_secret_access_key: YOUR_AWS_SECRET_ACCESS_KEY
  region_name: YOUR_AWS_REGION_NAME
  bucket: YOUR_AWS_S3_BUCKET_NAME
```

Replace the placeholders with your actual connection details.

### Usage

To use the script, simply run the redis_to_s3.py file using Python:

```sh
python3 main.py
```

The script will connect to Redis and S3 using the configuration in the config.yaml file, and export the keys and values
of the Redis database to the specified S3 bucket.
