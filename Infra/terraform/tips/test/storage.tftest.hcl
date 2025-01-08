run "check_gcs_object_name" {
  command = plan

  assert {
    condition     = google_storage_bucket.test_bucket.name == "example-bucket"
    error_message = "Object name is not example-bucket"
  }
}

run "check_bucket_location" {
  command = plan

  assert {
    condition     = google_storage_bucket.test_bucket.location == "ASIA-NORTHEAST1"
    error_message = "Bucket location is not ASIA-NORTHEAST1"
  }
}
