#!/bin/bash

awslocal s3 mb s3://be-cs300
awslocal s3api put-bucket-cors --bucket be-cs300 --cors-configuration file://cors.json
