terraform {
  backend "gcs" {
    bucket = "XXXX"
    prefix = "remote_state"
  }
}
