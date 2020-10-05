import boto3
import csv

#Sona Padinjarekutt
#CS1660 
#Assignment Three

#Add your AWS user credentials to access the resources under your IAM account
s3 = boto3.resource('s3',
    aws_access_key_id='<add your access key here>',
    aws_secret_access_key='<add your secret key here>')

#Try to create a new bucket called datacontui
try:
    s3.create_bucket(Bucket='datacontui', CreateBucketConfiguration={'LocationConstraint' : 'us-west-2'})
    #Upload a file, 'cardinal1.jpg' into the newly created Bucket
    #s3.Object('datacontui', 'cardinal1.jpg').put(Body=open('.\cardina1.jpg', 'rb'))
except:
    print("this may already exist")

#Test to see if I can add a picture of a cardinal
#s3.Object('datacontui', 'cardinal1.jpg').put(Body=open('C:\CS1660\AssignmentThree\cardinal1.jpg', 'rb'))

#Look at the newly created (or existing) datacontui bucket
bucket = s3.Bucket("datacontui")

#Enter AWS credentials to access the Dynamo DB resource
dyndb = boto3.resource('dynamodb',
    region_name='us-west-2',
    aws_access_key_id='<add your access key here>',
    aws_secret_access_key='<add your secret key here>'
)

#Try to create a new table called DataTable
try:
    table = dyndb.create_table(
        TableName='DataTable',
        KeySchema=[
            {
            'AttributeName': 'PartitionKey',
            'KeyType': 'HASH'
            },
            {
                'AttributeName': 'RowKey',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'PartitionKey',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'RowKey',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
except:
    table = dyndb.Table("DataTable") #if there is an exception, the table may already exist.   if so...

#The URL base to the S3 container object
urlbase = "https://s3-us-west-2.amazonaws.com/datacontui" #Link to my container that was created

#Open up the master experiment file, read all experimental data and add metadata
with open('C:\CS1660\AssignmentThree\experiments.csv', newline='') as csvfile:
    csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
    for item in csvf:
        body = open('C:\CS1660\AssignmentThree\\' + item[4], 'rb')
        s3.Object('datacontui', item[4]).put(Body=body)
        md = s3.Object('datacontui', item[4]).Acl().put(ACL='public-read')
        url = urlbase + item[4]
        metadata_item={'PartitionKey' : item[0], 'RowKey' : item[1], 'FlightNumber': item[3], 'Date' : item[2], 'OrderOfData' : item[5], 'url': url}
        table.put_item(Item = metadata_item)

#Query to get all data from table
exp_num = ['1', '2', '2', '3', '3'] #Allows for easy string appending for partition keys

for i in range(1,6):
    a = 'experiment'+ exp_num[i-1] #i.e experiment1, experiment2
    b = 'data' + str(i) #i.e data1, data2, data3
    response = table.get_item(
        Key = {
            'PartitionKey' : a,
            'RowKey': b
        }
    )
    print(response)
    print('------------------------------')
    print('------------------------------')
