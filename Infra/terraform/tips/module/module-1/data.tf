
variable "bucket" {
  type = string
}

data "terraform_remote_state" "module1" {
  backend = "gcs"

  config = {
    bucket = var.bucket
    prefix = "module1"
  }
}

output "module1_value" {
  value = "module1_value"
}

