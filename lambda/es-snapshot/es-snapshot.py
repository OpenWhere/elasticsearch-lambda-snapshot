import logging
import json
import requests
import datetime
import sys
from os import environ
from os import path

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)


# This is the method that will be registered
# with Lambda and run on a schedule
def handler(event={}, context={}):
    now = datetime.datetime.now()

    logger.info("started")

    logger.info("getting environment variables")
    # TODO: get variables here
    domain = environ['URL'].strip('/ ')
    bucket = environ['BUCKET'].strip()
    basePath = environ['ROOT_PATH'].strip('/ ')

    logger.info("setting repository json")
    repository = {
        "type": "s3",
        "settings": {
            "bucket": bucket,
            "base_path": path.join("/", basePath, "")
        }
    }
    logger.info("repository json is " + json.dumps(repository))

    logger.info("setting url path")
    url = path.join(domain, "_snapshot/lambda_s3_repository")
    logger.info("url path is " + url)

    # create repository
    logger.info("creating repository")
    try:
        response = requests.put(
            url,
            data=json.dumps(repository)
            )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(e)
        logger.error(response.content)
        sys.exit(1)

    logger.info(response.content)

    # start snapshot
    logger.info("starting snapshot")
    url = path.join(url, str(now.strftime("%Y-%m-%dt%H:%M")))
    try:
        response = requests.put(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(e)
        logger.error(response.content)
        sys.exit(2)

    logger.info(response.content)
    logger.info("new snapshot started at " + url)


# If being called locally, just call handler
if __name__ == '__main__':
    import os
    import json
    import sys

    logging.basicConfig()
    event = {}

    # TODO if argv[1], read contents, parse into json
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file, 'r') as f:
            data = f.read()
        event = json.loads(data)

    result = handler(event)
    output = json.dumps(
        result,
        sort_keys=True,
        indent=4,
        separators=(',', ':')
    )
    logger.info(output)
