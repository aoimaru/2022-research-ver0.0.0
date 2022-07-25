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
    (https://github.com/aoimaru/2022-research-ver0.0.0/blob/main/data/top_cases/tmp/GPG_KEY_ver0.0.1/top_10/min_count/sg-0.size-100.min_count-10.window-5.run-1.csv)

    *** result_1 ***
    set -ex  
        && for key in     
            94AE36675C464D64BAFA68DD7434390BDBE9B9C5     
            ******  
            8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600   
            ; do     
                gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-key "$key" ||     
                gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" ||
                gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ;   
            done
```

```bash
    "cases": [
        ["SC-APT-GET-UPDATE"],
        ["SC-APT-GET-INSTALL", "SC-APT-GET-F-YES"],
        ["SC-APT-GET-INSTALL", "SC-APT-GET-F-NO-INSTALL-RECOMMENDS"],
        ["SC-APT-GET-INSTALL", "SC-APT-GET-PACKAGES", "SC-APT-GET-PACKAGE:TK-DEV"],
        ["SC-RM", "SC-RM-F-RECURSIVE"],
        ["SC-RM", "SC-RM-F-FORCE"],
        ["SC-RM", "SC-RM-PATHS", "SC-RM-PATH", "BASH-CONCAT", "BASH-LITERAL", "ABS-MAYBE-PATH"],
        ["SC-RM", "SC-RM-PATHS", "SC-RM-PATH", "BASH-CONCAT", "BASH-LITERAL", "ABS-APT-LISTS"],
        ["SC-RM", "SC-RM-PATHS", "SC-RM-PATH", "BASH-CONCAT", "BASH-LITERAL", "ABS-PATH-VAR"],
        ["SC-RM", "SC-RM-PATHS", "SC-RM-PATH", "BASH-CONCAT", "BASH-LITERAL", "ABS-PATH-ABSOLUTE"],
        ["SC-RM", "SC-RM-PATHS", "SC-RM-PATH", "BASH-CONCAT", "BASH-GLOB", "ABS-GLOB-STAR"]
    ]

    "original"
    ->  RUN apt-get update && 
            apt-get install -y \
                $PHPIZE_DEPS \
                ca-certificates \
                curl \
                xz-utils \
            --no-install-recommends && 
            rm -r /var/lib/apt/lists/*

    "result"
    (https://github.com/aoimaru/2022-research-ver0.0.0/blob/main/data/top_cases/tmp/GPG_KEY_ver0.0.1/top_10/min_count/sg-0.size-100.min_count-10.window-5.run-1.csv)

    *** result_1 ***
    RUN apt update && 
        apt install -y cmake g++ && 
        rm -rf /var/lib/apt/lists/*

    *** result_2 ***
    RUN set -x && 
        apk add --update --no-cache ffmpeg && 
        rm -rf /var/cache/apk/* /tmp/*
    
```