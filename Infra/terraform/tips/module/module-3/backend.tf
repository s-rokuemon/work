terraform {
  backend "gcs" {
    bucket = "XXXX"
    prefix = "module3"
  }
}
