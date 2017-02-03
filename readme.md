# elasticsearch-lambda-snapshots

Uses AWS Lambda to take snapshots of an Elasticsearch cluster

## Configuration
This Lambda is configured with the following environment variables:

    URL="http://elasticsearch.mydomain.com:9200"
    BUCKET="mybucket"
    ROOT_PATH="/mycluster/"

## Getting Started
1.  Test the lambda function
  1.  Set environment variables
            export URL="http://elasticsearch.mydomain.com:9200"
            export BUCKET="mybucket"
            export ROOT_PATH="/path/for/backup/storage/"
  2.  Run lambda
            python lambda/es-snapshot/es-snapshot.py
2.  create zip
        ./build.sh
3.  Create Lambda function using zip file. **Must pass environment variables** (Automated in pod config)

## Notes
1. The iam and input dirs, as well as lambder.json are for use by Lambder. You can use Lambder for testing, but it is not part of our workflow at this time.
2. The Dockerfile is included only for testing purposes.
