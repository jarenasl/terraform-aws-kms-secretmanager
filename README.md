# terraform-aws-kms-secretmanager
Terraform code in order to user KMS for encrypt data and send to SecretManager

<summary>
This is a simple config to encrypt password and send to kms, kms will decrypt and send to secret manager for it will be used for any application.
</summary>

<h4>Skeleton:</h4>
<pre>
├── README.md
├── des.py
├── enc.py
├── kms
│   ├── main.tf
│   └── outputs.tf
└── requirements.txt
</pre>

<h4>Pre-requisites:</h4>
<h5>Terraform / AWSCli / Python3</h5>
 <ul>
  STEP 1:
 <ol>
  <li> Terraform v0.13.0 </li>
  <li> provider registry.terraform.io/hashicorp/aws v3.2.0 </li>
  <li> Python3 </li> 
 </ol>
  STEP 2:
   <ol>
   <li>  ADD AWS credentials in ~/.aws/config </li>
  Example:
    <p>
    [default]
    aws_access_key_id = Access key 
    aws_secret_access_key = Secret_key 
    </p>
    </li>
  </ol>
 </ul>

<h3> Init </h3>
<p> - deploy kms:  cd kms && terraform init </p>
<p> - deploy kms:  cd kms && terraform plan </p>
<p> - deploy kms:  cd kms && terraform apply </p>
<p> - encrypt:  use enc.py in order to encrypt a password using a kms alias </p>
<p> - decrypt:  use dec.py in order to decrypt the password and send to secret manager. </p>

<h3> Terraform </h3>
<p> - terraform plan -> validate code</p>
<p> - terraform apply -> deploy infrastructure code</p>
<p> - terraform destroy -> destroy infrastructure code</p>

<h3> Improvement </h3>
<p> - XXXXXX </p>

<h3> SecretManager </h3>
<p> - From Task definition on ECS, you have the posibility to call the value and insert the value as environment variable </p>
<p> (*) The value for the secret name in the task definition must match the name you specified for the secret name when the secret was created. </p>
<pre>{
        "secrets": [
        {
             "valueFrom": "arn:aws:secretsmanager:region:aws_account_id:secret:username_value-u9bH6K",
             "name": "password_value"
        }
        ]
}</pre>
<p>More info: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data-tutorial.html </P>
