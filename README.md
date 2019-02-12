# scan
To combine https://github.com/UKHomeOffice/repo-security-scanner\rules\gitrob.json
: [
  {
    "part": "filename",
    "type": "regex",
    "pattern": "\\A.*_rsa\\z",
    "caption": "Private SSH key",
    "description": null
  },
