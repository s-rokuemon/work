variable "bucket" {
  type = string
}

# module-1の出力値を取得
data "terraform_remote_state" "module1" {
  backend = "gcs"
  config = {
    prefix = "module1"
    bucket = var.bucket
  }
}

# module-2の出力値を取得
data "terraform_remote_state" "module2" {
  backend = "gcs"
  config = {
    prefix = "module2"
    bucket = var.bucket
  }
}
