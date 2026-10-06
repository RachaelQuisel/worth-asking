#!/usr/bin/env python3
"""Load private Worth Asking settings, or report generic mode when they are absent."""

import json
import os
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - the skill documents this failure
    yaml = None

SCRIPT = Path(__file__).resolve()
SKILL_DIR = SCRIPT.parents[1]
PLUGIN_ROOT = SCRIPT.parents[3]

SCALAR_KEYS = (
    "operator_name",
    "work_email",
    "drive_folder_id",
    "drive_folder_url",
    "slack_workspace_name",
    "slack_workspace_id",
)
LIST_KEYS = (
    "slack_channels",
    "manual_clients",
    "scheduled_clients",
    "optional_skills",
    "pattern_notes",
)

GENERIC_BEHAVIOR = (
    "No private config was found. Review only a transcript the user pasted "
    "or a file path they named in this conversation. Do not assume client names, "
    "accounts, channels, or home-folder paths. Do not search Drive, post to Slack, "
    "or run scheduled automation. Apply the generic lenses and return the questions "
    "in the conversation. config.example.yaml is a template of fake placeholders, "
    "not a client list."
)

CONFIGURED_BEHAVIOR = (
    "Use only the clients, accounts, channels, and paths in this config. "
    "manual_clients is the local review list. scheduled_clients is the automation allowlist. "
    "If manual_clients includes a client who is not in scheduled_clients, that difference is intentional: "
    "do not auto-post for the extra client. "
    "Optional scripts, the voice file, the report contract, and optional_skills are not bundled. "
    "If one is missing, skip that step and continue. "
    "If pattern_notes is empty, use the generic lenses only and do not invent personal history. "
    "Do not invent clients, emails, folder ids, channel ids, or home paths. "
    "Do not treat config.example.yaml as runtime data."
)


def candidate_paths():
    paths = []
    if len(sys.argv) > 1:
        paths.append(Path(sys.argv[1]).expanduser())
    env = os.environ.get("WORTH_ASKING_CONFIG")
    if env:
        paths.append(Path(env).expanduser())
    paths.extend(
        [
            Path.cwd() / "config.local.yaml",
            PLUGIN_ROOT / "config.local.yaml",
            SKILL_DIR / "config.local.yaml",
            Path.home() / ".config" / "worth-asking" / "config.local.yaml",
        ]
    )
    return paths


def empty_payload(mode, behavior, config_path=None):
    payload = {
        "mode": mode,
        "config_path": str(config_path) if config_path else None,
        "behavior": behavior,
        "warnings": [],
    }
    for key in SCALAR_KEYS:
        payload[key] = None
    for key in LIST_KEYS:
        payload[key] = []
    payload["paths"] = {}
    return payload


def emit(payload):
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


def main():
    found = next((path for path in candidate_paths() if path.is_file()), None)
    if found is None:
        emit(empty_payload("generic", GENERIC_BEHAVIOR))
        return 0

    if yaml is None:
        payload = empty_payload(
            "error",
            "PyYAML is not installed, so the private config could not be read. Do not guess clients or accounts.",
            found,
        )
        emit(payload)
        return 2

    try:
        loaded = yaml.safe_load(found.read_text())
    except yaml.YAMLError as exc:
        payload = empty_payload(
            "error",
            "The private config could not be parsed. Fix the file before running. Do not guess clients or accounts.",
            found,
        )
        mark = getattr(exc, "problem_mark", None)
        if mark is not None:
            payload["line"] = mark.line + 1
        emit(payload)
        return 2

    if loaded is None:
        loaded = {}
    if not isinstance(loaded, dict):
        payload = empty_payload(
            "error",
            "The private config must be a mapping. Do not guess clients or accounts.",
            found,
        )
        emit(payload)
        return 2

    warnings = []
    payload = empty_payload("configured", CONFIGURED_BEHAVIOR, found)
    for key in SCALAR_KEYS:
        if key not in loaded or loaded[key] is None:
            continue
        if isinstance(loaded[key], str):
            payload[key] = loaded[key]
        else:
            warnings.append(f"Ignored {key} because it is not text.")
    for key in LIST_KEYS:
        if key not in loaded or loaded[key] is None:
            continue
        if isinstance(loaded[key], list):
            payload[key] = loaded[key]
        else:
            warnings.append(f"Ignored {key} because it is not a list.")
    if "paths" in loaded and loaded["paths"] is not None:
        if isinstance(loaded["paths"], dict):
            payload["paths"] = {
                str(key): value
                for key, value in loaded["paths"].items()
                if not str(key).startswith("_")
            }
        else:
            warnings.append("Ignored paths because it is not a mapping.")
    payload["warnings"] = warnings
    emit(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
