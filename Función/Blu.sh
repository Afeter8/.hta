#!/bin/bash
while true
do
    python3 generador_codex_global.py
    python3 verificador_hash.py
    sleep 3600
done
