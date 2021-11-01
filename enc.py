import boto3
import base64

if __name__ == '__main__':
    session = boto3.session.Session()

    kms = session.client('kms')

    key_id = 'alias/kantox-kms'
    stuff = kms.encrypt(KeyId=key_id, Plaintext='HB3NGUvfDB2Xekx3')
    binary_encrypted = stuff[u'CiphertextBlob']
    encrypted_password = base64.b64encode(binary_encrypted)
    print(encrypted_password.decode())
