#!/bin/bash -x
pip install copr
cat << EOF > copr.conf
[copr-cli]
login = $LOGIN
username = huakim
token = $TOKEN
copr_url = https://copr.fedorainfracloud.org
# expiration date: 2025-09-16
EOF
python3 main.py
