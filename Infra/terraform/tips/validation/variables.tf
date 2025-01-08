variable "environment" {
  validation {
    condition     = contains(["dev", "prod"], var.environment)
    error_message = "The environment must be dev, stg or prod."
  }
}
