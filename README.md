# NoSQLdb
**Background:** This is an assignment for my CS1660 Cloud Computing class. The python script creates a NoSQL database to store experimental data using AWS.

**Setup:** To be able to run the dynamoNoSQL.py script locally on your computer... 

  (1) Use your AWS account and insert your access key and secret access key in the script as specified. If you do not have these keys, create a new user and make sure it has the following permissions: AmazonEC2FullAccess, AmazonS3FullAccess, and AmazonDynamoDBFullAccess
  
  (2) Download the following experimental data in the repo (master experimental .csv file is also avaliable). Though do note, the experimental data is publicly accessible through these links:
  
    a.) https://datacontui.s3-us-west-2.amazonaws.com/exp1.csv
    b.) https://datacontui.s3-us-west-2.amazonaws.com/exp2.csv
    c.) https://datacontui.s3-us-west-2.amazonaws.com/exp3.csv
    d.) https://datacontui.s3-us-west-2.amazonaws.com/exp4.csv
    e.) https://datacontui.s3-us-west-2.amazonaws.com/exp5.csv
    
   (3) Modify the dynamoNoSQL.py script (Lines 70 and 73) and change the filepath to the place where you downloaded the data mentioned above.
   
   (4) Make sure you downloaded Boto3 in order to use the AWS CLI and run the dynamoNoSQL.py script with no errors. 
