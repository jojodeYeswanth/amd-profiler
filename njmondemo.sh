#!/bin/bash


njmon -s 5 -c $1 -m ./wrapper -f workloadProfiler.json
