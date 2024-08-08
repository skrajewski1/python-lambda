terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.61.0"
    }
  }
}
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "dev_instances" {
  ami           = "ami-01eccbf80522b562b"
  instance_type = "t2.micro"

  tags = {
    Name = "dev-server"
    env  = "dev"
  }
}
resource "aws_instance" "prod_instances" {
  ami           = "ami-01eccbf80522b562b"
  instance_type = "t2.micro"

  tags = {
    Name = "prod-server"
    env  = "prod"
  }
}

resource "aws_instance" "qa_instance" {
  ami           = "ami-01eccbf80522b562b"
  instance_type = "t2.micro"

  tags = {
    Name = "qa-server"
    env  = "qa"
  }
}          