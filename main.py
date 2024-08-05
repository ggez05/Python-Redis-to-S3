import redis
import boto3
import yaml

# Load configuration
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Connect to Redis
redis_conn = redis.Redis(
    host=config["redis"]["host"],
    port=config["redis"]["port"],
    db=config["redis"]["db"],
    password=config["redis"]["password"],
)

# Connect to S3
s3_conn = boto3.client(
    "s3",
    aws_access_key_id=config["s3"]["aws_access_key_id"],
    aws_secret_access_key=config["s3"]["aws_secret_access_key"],
    region_name=config["s3"]["region_name"],
)

# Export Redis keys and values to S3
for key in redis_conn.keys():
    value = redis_conn.get(key)
    print(key.decode("utf-8"), value.decode("utf-8"))
    s3_conn.put_object(
        Bucket=config["s3"]["bucket"],
        Key=key.decode("utf-8"),
        Body=value.decode("utf-8"),
    )
