#!/bin/bash
sam package --output-template-file packaged.yaml \
    --s3-bucket my-s3-bucket


sam deploy --template-file packaged.yaml  \
    --stack-name my-stack-name \
    --capabilities CAPABILITY_IAM \
    --region eu-central-1