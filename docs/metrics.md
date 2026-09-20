# About the snapshot

The profile SVG graphics are hosted in this repository in light and dark palettes. No remote fonts, analytics, scripts or third-party image services.

- **Public projects:** repositories owned by `bglglzd`, excluding forks, archived repositories and this profile repository.
- **Published releases:** non-draft GitHub releases in those repositories, including prereleases. This is not a claim of production readiness.
- **Projects with releases:** how many of those repositories have a published release.
- **Language mix:** summed GitHub language byte counts for their current default branches. This describes code mix, including contributions by others. It is not time spent, skill level, lines personally written, or a lifetime total.

The date is the snapshot's UTC date. The [raw snapshot](../assets/public-metrics.json) lists projects and counts. The workflow refreshes weekly and can be run manually. If GitHub's API fails, the last successful snapshot stays visible.

The generator uses public repository endpoints, explicitly filters private repositories and does not request profile contribution totals. No private project names, personal emails or local paths are included.

Reproduce with Python 3.11+ and an authenticated GitHub CLI:

```sh
python scripts/render_profile.py
```

Render the saved snapshot without API access:

```sh
python scripts/render_profile.py --offline
```

Sources: [GitHub language API](https://docs.github.com/en/rest/repos/repos#list-repository-languages), [GitHub releases API](https://docs.github.com/en/rest/releases/releases#list-releases).
