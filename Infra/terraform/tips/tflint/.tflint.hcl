config {
}

# ref. https://github.com/terraform-linters/tflint-ruleset-google
plugin "google" {
  enabled = true
  version = "0.27.1"
  source  = "github.com/terraform-linters/tflint-ruleset-google"
}

# resource名はスネークケース表記にする必要がある
rule "terraform_naming_convention" {
  enabled = true
}

# コメントは#を使う(//は使わない)
rule "terraform_comment_syntax" {
  enabled = true
}

# variableブロックやoutputブロックはvariables.tfやoutputs.tfに定義する必要がある
rule "terraform_standard_module_structure" {
  enabled = true
}

# プロバイダのバージョン記載を必須とする
rule "terraform_required_version" {
  enabled = true
}
