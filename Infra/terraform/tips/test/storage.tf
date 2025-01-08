
resource "google_storage_bucket" "test_bucket" {
  name     = "example-bucket-2"
  location = "ASIA"
  project  = var.project

  storage_class = "MULTI_REGIONAL"
  versioning {
    enabled = true
  }
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}
