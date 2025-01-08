

output "terraform_remote_state_output_all" {
  value = {
    # module1
    module_1_output = data.terraform_remote_state.module1.outputs.module1_value
    # module2
    module_2_output = data.terraform_remote_state.module2.outputs.module2_value
  }
}
