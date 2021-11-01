provider "aws" {
  region = "eu-west-3"
}

resource "aws_kms_key" "my-kms" {
  description             = "kantox-kms"
  deletion_window_in_days = 10
}

resource "aws_kms_alias" "my-kms" {
  name          = "alias/kantox-kms"
  target_key_id = aws_kms_key.my-kms.key_id
}