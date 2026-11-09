#!/bin/bash
set -e

PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
python3 "$PROJECT_DIR"/main.py
