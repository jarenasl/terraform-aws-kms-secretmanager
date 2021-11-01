output "aws_kms_key_arn" {
  value       = aws_kms_key.my-kms.arn
  description = "ARN kms"
}

output "aws_kms_alias_name" {
  value       = aws_kms_alias.my-kms.name
  description = "Name alias kms"
}
