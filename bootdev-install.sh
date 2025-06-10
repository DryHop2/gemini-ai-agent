#!/bin/bash
set -e

# Install Go via Webi (non-interactive)
curl -sS https://webi.sh/golang | bash

# Add Go to PATH for this session
export PATH="/root/.local/opt/go/bin:/root/go/bin:$PATH"

# Install BootDev CLI
go install github.com/bootdotdev/bootdev@latest
