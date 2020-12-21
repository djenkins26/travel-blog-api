#!/bin/bash

curl "http://localhost:8000/blog_posts/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
