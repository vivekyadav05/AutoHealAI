terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "artifacts" {
  bucket = "${var.project_name}-artifacts-${var.environment}"
}

resource "aws_cloudwatch_log_group" "app_logs" {
  name              = "/autohealai/${var.environment}"
  retention_in_days = 14
}
