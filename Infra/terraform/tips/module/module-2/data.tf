variable "bucket" {
  type = string
}

data "terraform_remote_state" "module2" {
  backend = "gcs"

  config = {
    bucket = var.bucket
    prefix = "module2"
  }
}

output "module2_value" {
  value = "module2_value"
}
