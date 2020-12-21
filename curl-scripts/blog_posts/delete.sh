#!/bin/bash

curl "http://localhost:8000/blog_posts/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
