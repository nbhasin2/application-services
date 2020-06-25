#!/usr/bin/env python3

# Purpose: Run cargo update and make a pull-request against main.
# Dependencies: None
# Usage: ./automation/cargo-update-pr.py

from shared import step_msg, fatal_err, run_cmd_checked, find_app_services_root, ensure_working_tree_clean

step_msg("Checking that the generated protobuf Rust files are up-to-date")
# ensure_working_tree_clean()
config_file_path = find_app_services_root() / "tools/protobuf_files.toml"
run_cmd_checked(["cargo", "run", "--bin", "protobuf-gen", config_file_path])

if run_cmd_checked(["git", "status", "--porcelain"], capture_output=True).stdout:
    run_cmd_checked(["git", "status"])
    fatal_err("""
The protobuf rust files are outdated.
You can fix this yourself by running cargo run --bin protobuf-gen <APP_SERVICES_ROOT>/tools/protobuf_files.toml
    """)
