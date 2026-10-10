# Changelog

All notable changes to this plugin are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-10-10

### Added

- Books can now be exported to **multiple backup destinations**. The settings
  dialog gained a `+` button to add a destination and a `Remove` button on each
  one; every configured destination receives the export.
- Destinations are validated when added: only an existing directory that is not
  already in the list can be added.
- A destination that is not currently reachable - an external drive that is
  unplugged, or a cloud folder that is not mounted - is skipped with a message
  instead of aborting the run, so the remaining destinations still get exported.
- README with installation and usage instructions, and a LICENSE file.

### Changed

- Settings now store a list of destinations under `backup_destinations`. A
  single destination saved by version 1.0.0 is migrated automatically on first
  read, so existing configurations keep working without manual changes.
- Configured destination paths are shown in a read-only field, so a path can no
  longer be edited into an invalid one by accident. Use `Remove` and `+` to
  change a destination.
- The export dialog is titled "Export".

### Fixed

- "Export Books Now" did nothing unless *"Export new books each time Calibre is
  closed"* was also enabled. The manual button now always exports; the
  preference only governs the automatic export on shutdown.
- An export that failed partway through - for example because the drive was
  removed mid-run - no longer prevents the remaining destinations from being
  exported.

## [1.0.0] - 2025-10-26

### Added

- Initial release: export the Calibre library to a configured location, either
  on demand or automatically each time Calibre is closed.
