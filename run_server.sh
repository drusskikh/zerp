#!/bin/bash

find zerp/ -name '*.pyc' -delete
find auth/ -name '*.pyc' -delete

./run_server.py
