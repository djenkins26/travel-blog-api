#!/bin/bash

curl "http://localhost:8000/blog_posts/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "blog": {
      "country_name": "'"${COUNTRY_NAME}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
