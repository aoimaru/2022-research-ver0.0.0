```bash
    "case": [
        ["SC-GPG", "SC-GPG-F-BATCH"],
        ["SC-GPG", "SC-GPG-KEYSERVER", "BASH-LITERAL", "ABS-PROBABLY-URL"],
        ["SC-GPG", "SC-GPG-KEYSERVER", "BASH-LITERAL", "ABS-URL-HA-POOL"],
        ["SC-GPG", "SC-GPG-KEYSERVER", "BASH-LITERAL", "ABS-URL-POOL"]
    ]

    "original"
    -> gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY"
```