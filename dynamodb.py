import boto3
from flask import current_app as app

def dynamodb_put_item(item_data):

    session = boto3.Session(
        aws_access_key_id=app.config["AWS_KEY"],
        aws_secret_access_key=app.config["AWS_SECRET"],
        aws_session_token=app.config["AWS_SESSION"]
    )

    dynamodb = session.resource("dynamodb")

    table = dynamodb.Table(app.config["DYNAMODB_TABLE"])

    return table.put_item(Item=item_data)


def dynamodb_scan():

    session = boto3.Session(
        aws_access_key_id=app.config["AWS_KEY"],
        aws_secret_access_key=app.config["AWS_SECRET"],
        aws_session_token=app.config["AWS_SESSION"]
	)

    dynamodb = session.resource("dynamodb")

    table = dynamodb.Table(app.config["DYNAMODB_TABLE"])

    return table.scan()
