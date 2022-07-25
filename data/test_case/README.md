```bash
    "case": [
        ["SC-GPG", "SC-GPG-F-BATCH"],
        ["SC-GPG", "SC-GPG-KEYSERVER", "BASH-LITERAL", "ABS-PROBABLY-URL"],
        ["SC-GPG", "SC-GPG-KEYSERVER", "BASH-LITERAL", "ABS-URL-HA-POOL"],
        ["SC-GPG", "SC-GPG-KEYSERVER", "BASH-LITERAL", "ABS-URL-POOL"]
    ]

    "original"
    -> gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY"

    "result"
    https://github.com/aoimaru/2022-research-ver0.0.0/blob/main/data/top_cases/tmp/GPG_KEY_ver0.0.1/top_10/min_count/sg-0.size-100.min_count-10.window-5.run-1.csv


```