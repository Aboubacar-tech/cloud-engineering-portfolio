#!/bin/bash

echo "Starting disk stress test..."

dd if=/dev/zero of=/tmp/bigfile bs=1M count=500

echo "Disk stress completed. File created at /tmp/bigfile"