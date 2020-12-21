#!/bin/bash

curl "http://localhost:8000/blog_posts/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "blog": {
      "country_name": "'"${COUNTRY_NAME}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
