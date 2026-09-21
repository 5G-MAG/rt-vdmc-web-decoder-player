<p align="center">
  <img src=".github/banner.svg" width="100%" alt="Reference Tools · Immersive Media: MPEG V-DMC Web Decoder and Player">
</p>

<p align="center">
  {{One sentence: what it decodes, where it plays it, and which specification it implements.}}
</p>

<p align="center">
  <img alt="Status: experimental"
    src="https://img.shields.io/badge/Status-Experimental-c0392b">
  <a href="https://github.com/5G-MAG/rt-vdmc-web-decoder-player/releases"><img alt="Version"
    src="https://img.shields.io/github/v/release/5G-MAG/rt-vdmc-web-decoder-player?label=Version&sort=semver"></a>
  <a href="LICENSE"><img alt="License: 5G-MAG Public License v1.0"
    src="https://img.shields.io/badge/License-5G--MAG%20PL%20v1.0-blue"></a>
</p>

<p align="center">
  <a href="https://www.5g-mag.com/reference-tools/vdmc">Project page</a> &nbsp;&middot;&nbsp;
  <a href="https://github.com/5G-MAG/rt-vdmc-web-decoder-player/issues">Issues</a> &nbsp;&middot;&nbsp;
  <a href="https://www.5g-mag.com/contributing">Contributing</a>
</p>

---

## At a glance

|  |  |
|---|---|
| **Implements** | {{ISO/IEC 23090-29, Video-based dynamic mesh coding (V-DMC). Confirm the edition and year before the first code lands}} |
| **Part of** | Immersive Media |

## Introduction

{{What this repository is, in two or three sentences: what a V-DMC bitstream is, what this decodes
and renders, and where it runs. rt-v3c-unity-player and rt-v3c-decoder-plugin target Windows and
Android through Unity, so say what a web target adds. Say what is out of scope here.}}

## Specification

{{Record the document, edition and year this is built against before the first code lands, as a
version rather than a release name.}}

Clause-by-clause coverage, and what is still absent, is recorded on the project page rather than
here: <https://www.5g-mag.com/reference-tools/vdmc>

This is the repository's initial commit, so no decoder or player code has landed yet. The sections
below are the skeleton every 5G-MAG reference tool uses, with `{{...}}` marking what the first code
fills in.

## Install dependencies

```bash
{{the toolchain the build needs}}
```

## Downloading

```bash
cd ~
git clone https://github.com/5G-MAG/rt-vdmc-web-decoder-player.git
```

## Building

```bash
{{build commands}}
```

## Installing

```bash
{{install commands}}
```

## Running

```bash
{{how to serve the player locally, and the URL it comes up on}}
```

## Configuration

{{Configuration file locations, the options an operator sets, and their defaults.}}

## Development

{{Branch model, how to run the tests, and how many cases the suite has.}}

## Contributing

Contributions are welcome. How to raise an issue, fork the repository and open a pull request, and
the Contributor License Agreement required before code can be merged, are described at
<https://www.5g-mag.com/contributing>.

## License

Distributed under the 5G-MAG Public License v1.0. See [LICENSE](LICENSE).
