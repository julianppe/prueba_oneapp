#!/bin/bash
docker run -d \
    -p 5001:5000 \
    --name genlac_graphics \
    genlac_graphics:latest