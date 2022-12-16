#!/bin/bash
docker run -d \
    -p 5001:5000 \
    --name genlac \
    genlac_dash_ninez_spanish:latest