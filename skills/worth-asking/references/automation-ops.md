# Automation ops

Read this only when operating or debugging the scheduled Worth Asking automation. A one-off transcript review does not need it.

Run `skills/worth-asking/scripts/load_config.py` first.

- If `mode` is `generic`, or `mode` is `error`, stop. Scheduled posting is not configured. Do not invent a client list, a channel, a home path, or a repository. Tell the user to copy `config.example.yaml` to `config.local.yaml`.
- If `mode` is `configured`, use `scheduled_clients`, `slack_channels`, and `paths` from the loader. `manual_clients` may name extra clients. That is intentional. Do not post for a client who is only on the manual list.

The automation file at `paths.automation_toml` is the source of truth for schedule and tooling when the file exists. Do not describe the job as a cloud run unless that file says so. A past connector error is not stored here, because that note goes stale. Re-check access on this run. Report the current failure. Do not treat not-found or an empty listing as proof a folder is empty, and do not widen the search to unrelated locations.

## What is not bundled

This package does not include the prepare script, the state script, the one-transcript diagnostic, the voice file, or the report contract. Those paths come from config. The sibling skills `meeting-prep`, `gem-miner`, and `humanizing` are also optional and may be absent.

If a configured path does not exist, or a sibling skill is not installed, skip that step and continue. A missing optional file is not a source failure. Do not block the clients you can still read. If the report contract is missing, say so and use the manual output format from SKILL.md rather than inventing a second contract.

## Source rules

Debrief in connected Airtable supplies meeting metadata and durable record IDs. Complete transcripts may come from Debrief or from a verified matching Drive file. When Debrief text is missing or incomplete, try Drive recovery before declaring a source failure. Read [Drive transcript recovery](google-drive-transcripts.md) for matching and completeness.

Connected calendar is a coverage check only. Compare completed meetings for `scheduled_clients` with Debrief so a missing transcript cannot disappear quietly. Calendar metadata never generates findings.

Use a 14-day recovery window by meeting date, inclusive from today minus 13 days through today. Record eligible Debrief IDs in the ledger at `paths.state_json` when that file exists. Unposted IDs stay pending until Slack confirms delivery, even after they leave the window. Successfully posted meetings from the last seven days are comparison context. Do not add clients who are not on `scheduled_clients`. Do not glob local folders, use modified time as the conversation date, or treat meeting-prep output as a transcript. An unresolved source failure is a failed client result, not an empty radar. Continue unaffected clients. A malformed ledger blocks all posting.

## How a run fires

1. The scheduler fires. Confirm the times in `paths.automation_toml` rather than assuming a clock.
2. Compare 14 days of calendar events for `scheduled_clients` with Debrief. A missing transcript triggers Drive recovery. Only an unresolved gap produces a deduplicated source-gap notice. A prior source-exception report suppresses a duplicate.
3. Inventory 14 days of approved Debrief metadata and add eligible IDs to the pending ledger.
4. Search each configured Slack channel for pending record IDs. Mark confirmed existing posts as processed.
5. Pending records that are absent from Slack get one client report. Meetings posted in the last seven days stay comparison context.
6. Fetch each transcript by record ID. Recover missing or truncated text from a verified Drive file. Read the complete file before analysis. One unresolved client does not block the others.
7. Post through the connected Slack tool to a channel listed in `slack_channels` for that client. If `slack_channels` is empty, do not guess a channel. Report that delivery is not configured and leave the records pending.
8. Move a record from pending to processed only after a successful send. Failed clients stay pending with no age cutoff.

## Operate cheatsheet

Substitute paths from the loaded config. Skip a row when its path is missing.

| Action | Command |
|---|---|
| Inspect the active contract | `sed -n '1,260p' "<paths.automation_toml>"` |
| Inspect pending and processed IDs | `python3 "<paths.state_script>" show` |
| Run one non-posting diagnostic | `python3 "<paths.run_one_script>" --record-id <rec...> --client "<a scheduled client>"` |
| Trigger the repository fallback manually | `gh workflow run "<paths.workflow_file>" --repo "<paths.report_contract_repo>"` |

The report contract, when present, is `paths.report_contract_path` inside `paths.report_contract_repo`. Do not duplicate or override its source labels, evidence rules, voice rules, empty-radar form, or next-move constraints. The manual format in SKILL.md is the contract for runs outside the scheduled job.

## Slack check

On a Slack failure, confirm the connected installation matches `slack_workspace_name` and `slack_workspace_id`, that the destination is one of `slack_channels`, and that `slack_send_message` returned a message link or identifier. Do not invent a workspace id. The scheduled path does not use `SLACK_BOT_TOKEN`. A generated report without a successful connected-tool response is a failed delivery and stays retryable.
