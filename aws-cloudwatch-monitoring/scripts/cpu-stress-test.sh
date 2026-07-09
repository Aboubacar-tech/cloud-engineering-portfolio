#!/bin/bash

echo "Starting CPU stress test..."

yes > /dev/null &
yes > /dev/null &

echo "CPU stress started. PIDs: $(pgrep yes)"