#!/bin/bash

curl "http://localhost:8000/blog_posts/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "blog": {
      "place": "'"${PLACE}"'",
      "description": "'"${DESCRIPTION}"'"
    }
  }'

echo
