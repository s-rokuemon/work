resource "random_id" "default" {
  byte_length = 8
}

resource "google_storage_bucket" "default" {
  name     = "${random_id.default.hex}-example-bucket"
  location = "ASIA"
  project  = var.project

  storage_class = "MULTI_REGIONAL"
  versioning {
    enabled = true
  }
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}
