import boto3
import base64


def create(name, secret_value):
    """
    Creates a new secret. The secret value can be a string or bytes.
    """
    secrets_client = boto3.client('secretsmanager')
    kwargs = {"Name": name}
    if isinstance(secret_value, str):
        kwargs["SecretString"] = secret_value
    elif isinstance(secret_value, bytes):
        kwargs["SecretBinary"] = secret_value
    response = secrets_client.create_secret(**kwargs)
    return response

if __name__ == '__main__':
    session = boto3.session.Session()

    kms = session.client('kms')

    encrypted_password = 'AQICAHgss0dICyf7WUVEAjPjc+1ZAEr9eqBHeekDscWTPEdtsQF0iwz7Vk6XZsBgrXAxpw7/AAAAbjBsBgkqhkiG9w0BBwagXzBdAgEAMFgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM06+anHiZy4ud900SAgEQgCsNvr0rYNCWsrgCJPV8JvLEG3eDChq0+tywuPI7uzmtGie7w8IdAFQsokFM'
    binary_data = base64.b64decode(encrypted_password)
    meta = kms.decrypt(CiphertextBlob=binary_data)
    plaintext = meta[u'Plaintext']

    password_value="kantox-dev-password"
    print(create(password_value, plaintext.decode()))
    #print(plaintext.decode())
