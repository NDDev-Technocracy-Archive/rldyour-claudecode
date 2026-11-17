# GitHub Actions workflows

This public source uses standard GitHub-hosted runners. The authoritative
shared CI selection is [validate.yml](validate.yml); all shared callers select
one full SHA and release-version comment from
NDDev-Technocracy-OpenNetwork/nddev-ci. The source consistency test rejects
mixed or malformed selections and retired-provider reuse. Actual release and
native compatibility qualification remain CI/updater results, not a prose copy.

## Required source and native validation

- validate.yml retains official CLI marketplace/plugin validation, source/schema,
  contract, ownership, routing, hook and instruction checks.
- pytest.yml retains the current unit-only selection.
- cross-platform.yml retains Ubuntu, Windows and macOS metadata smoke.
- security.yml retains CodeQL, dependency review and its existing public
  supply-chain report.

The new shared source/merge-stop calls operate beside these native obligations.
`just check` runs offline workflow/command checks; `just verify` adds the
retained complete-history source scan. These commands do not run an agent,
install a plugin, start a session or call a provider.

## Independent reporting and release

security-daily.yml supplies the shared daily report. Existing CLI/dependency
drift schedules remain advisory; they do not replace required source/native
validation. release.yml retains its existing tag/manual publication contract.
Source maintenance creates no release tag or installed-runtime adoption.

Existing native job permissions, egress restrictions, fixture boundaries,
runtime pins and source scopes are preserved. Qualify the actual current
required source/security/native contexts before ordinary automatic integration;
retained failed/cancelled attempts are evidence, not current success.
