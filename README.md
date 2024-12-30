# AWS Lambda Python(Image/ECR) for CSV Processing with DuckDB

This repository contains an AWS SAM application that utilizes a Python-based AWS Lambda function(Image/ECR) to process CSV files stored in Amazon S3. A key feature of this application is its use of [DuckDB](https://duckdb.org/) for efficient in-memory data exploration and analytics.

## Overview

- The application is written in Python and runs on AWS Lambda.
- It uses DuckDB to query and analyze CSV data from your S3 bucket.
- You can build and deploy it using the AWS SAM CLI.

## Prerequisites

1. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configured.
2. [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) installed.
3. A CSV file uploaded to your S3 bucket.

## Pre-Deployment Steps

1. **Upload the CSV File**  
   Upload your CSV file to an S3 bucket of your choice. For example:
   ```
   s3://YOUR-BUCKET/FILENAME.csv
   ```
2. **Modify `template.yml`**  
   In the `template.yml` file, locate the parameter `S3URI` and update it to match your bucket and file name. For example:
   ```yaml
   S3URI: s3://YOUR-BUCKET/FILENAME.csv
   ```

## Build and Deploy

The following commands will build and deploy the application using the AWS SAM CLI.

1. **Build the Application**  
   ```
   $ sam build
   ```

2. **Deploy the Application**  
   ```
   $ sam deploy --guided
   ```
   Once the deployment is complete, SAM will provide outputs such as the Lambda function name or API endpoints (if any).

## Important Notes on DuckDB and Lambda

- AWS Lambda does not set a `HOME` environment variable by default.
- DuckDB installs extensions inside the HOME directory.
- Therefore, to ensure successful extension installation, we set `HOME` to `/tmp` within the Lambda function’s environment variables.
- Otherwise, you'll encounter errors as follows:
    ```
    D INSTALL httpfs;
    IO Error: Can't find the home directory at ''
    Specify a home directory using the SET home_directory='/path/to/dir' option.

    ...

    D CREATE SECRET (
          TYPE S3,
          PROVIDER CREDENTIAL_CHAIN
      );
    Extension Autoloading Error: An error occurred while trying to automatically install the required extension 'aws':
    Can't find the home directory at ''
    Specify a home directory using the SET home_directory='/path/to/dir' option.
    ```
