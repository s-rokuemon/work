
variable "bucket" {
  type = string
}

data "terraform_remote_state" "env" {
  backend = "gcs"
  config = {
    prefix = "remote_state"
    bucket = var.bucket
  }
}

# 出力確認
output "module1_value_from_module3" {
  value = data.terraform_remote_state.env.outputs.terraform_remote_state_output_all.module_1_output
}
output "module2_value_from_module3" {
  value = data.terraform_remote_state.env.outputs.terraform_remote_state_output_all.module_2_output
}


