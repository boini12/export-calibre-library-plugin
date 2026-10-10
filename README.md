<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/boini12/calibre_automatic_sync_to_external_harddrive">
    <img src="images/icon.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Automatic Export Calibre Books</h3>

  <p align="center">
    A Calibre plugin that exports your library to one or more backup destinations — manually, or automatically every time Calibre closes.
    <br />
    <a href="#usage"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/boini12/calibre_automatic_sync_to_external_harddrive/releases/latest">Download Plugin</a>
    &middot;
    <a href="https://github.com/boini12/calibre_automatic_sync_to_external_harddrive/issues/new?labels=bug">Report Bug</a>
    &middot;
    <a href="https://github.com/boini12/calibre_automatic_sync_to_external_harddrive/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running-from-source">Running From Source</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#export-structure">Export Structure</a></li>
        <li><a href="#notes">Notes</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Calibre keeps your library in one place, which is fine until that place is the only copy. This plugin keeps date-stamped copies of the library on as many destinations as you like — an external hard drive, a NAS mount, a cloud-synced folder — and does it on its own every time you close Calibre.

Exports are incremental: once a backup exists at a destination, only books that are not in it yet get copied, so a routine export after adding a single book costs a single book's worth of copying. Destinations that are not currently reachable, such as an external drive that is unplugged, are skipped rather than failing the export for every other destination.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Features

* **Toolbar button for configuration and manual exports** — the plugin adds a button to the Calibre toolbar that opens a small dialog with *Configure Backup Settings* and *Export Books Now*.
* **Multiple backup destinations** — add as many destinations as you want in the settings with the `+` button, and remove them again with *Remove*. A path is only accepted once it actually exists on disk.
* **Automatic export on close** — with *Export new books each time Calibre is closed* enabled, the export runs whenever Calibre shuts down.
* **Incremental exports** — if a previous backup exists at a destination, it is re-stamped with today's date and only new books are copied. If none exists, the whole library is exported.
* **Unreachable destinations are skipped** — a disconnected drive or an unreadable mount point is reported and passed over, and the remaining destinations still get their export.
* **Cross-platform** — macOS, Linux and Windows.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python]][Python-url]
* [![Qt][Qt]][Qt-url]
* [![Calibre][Calibre]][Calibre-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* [Calibre](https://calibre-ebook.com/download) 0.7.53 or newer
* Enough free space at every backup destination to hold a copy of the library

### Installation

1. Download `export_calibre_books_plugin.zip` from the [latest release](https://github.com/boini12/calibre_automatic_sync_to_external_harddrive/releases/latest).
2. Add the plugin to Calibre, either through *Preferences → Plugins → Load plugin from file*, or from a terminal
   ```sh
   calibre-customize -a export_calibre_books_plugin.zip
   ```
3. Restart Calibre.
4. Open the plugin's toolbar button, click *Configure Backup Settings* and add at least one backup destination.

### Running From Source

1. Clone the repo
   ```sh
   git clone https://github.com/boini12/calibre_automatic_sync_to_external_harddrive.git
   ```
2. Make sure Calibre is installed and its command line tools are on your `PATH`.
3. Start Calibre in debug mode from the root folder of the repository, which loads the plugin from the working copy and prints its output to the terminal
   ```sh
   calibre-debug -g
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

1. Click the plugin's **toolbar icon** to open the export dialog.
2. Choose **Configure Backup Settings**.
3. Add one or more **backup destinations** with the `+` button. Type or paste the path, then click *Add* — the button stays disabled until the path exists.
4. Enable **Export new books each time Calibre is closed**.
5. Close Calibre to let the export run, or use **Export Books Now** in the dialog to run it immediately.

### Export Structure

Each export lives in a date-stamped folder at every destination:

```text
<destination_path>/
└── calibre_backup_2026-10-10/
    ├── Author Name/
    │   ├── Book Title/
    │   │   ├── book.epub
    │   │   ├── cover.jpg
    │   │   └── metadata.opf
    │   └── Another Book/
    └── Another Author/
```

On the next export the existing folder is renamed to the current date and only new books are added to it, so a destination holds one backup folder that carries the date it was last written.

### Notes

* **Export Books Now** always runs, no matter how *Export new books each time Calibre is closed* is set — that checkbox only controls the export on shutdown.
* Automatic export triggers on a regular Calibre shutdown, not if Calibre crashes.
* Progress and skipped destinations are printed to Calibre's output, which is visible when it was started with `calibre-debug -g`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/boini12/calibre_automatic_sync_to_external_harddrive/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=boini12/calibre_automatic_sync_to_external_harddrive" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

boini12 - [@boini12](https://github.com/boini12)

Project Link: [https://github.com/boini12/calibre_automatic_sync_to_external_harddrive](https://github.com/boini12/calibre_automatic_sync_to_external_harddrive)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Calibre Plugin Development Documentation](https://manual.calibre-ebook.com/creating_plugins.html)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Img Shields](https://shields.io)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/boini12/calibre_automatic_sync_to_external_harddrive.svg?style=for-the-badge
[contributors-url]: https://github.com/boini12/calibre_automatic_sync_to_external_harddrive/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/boini12/calibre_automatic_sync_to_external_harddrive.svg?style=for-the-badge
[forks-url]: https://github.com/boini12/calibre_automatic_sync_to_external_harddrive/network/members
[stars-shield]: https://img.shields.io/github/stars/boini12/calibre_automatic_sync_to_external_harddrive.svg?style=for-the-badge
[stars-url]: https://github.com/boini12/calibre_automatic_sync_to_external_harddrive/stargazers
[issues-shield]: https://img.shields.io/github/issues/boini12/calibre_automatic_sync_to_external_harddrive.svg?style=for-the-badge
[issues-url]: https://github.com/boini12/calibre_automatic_sync_to_external_harddrive/issues
[license-shield]: https://img.shields.io/github/license/boini12/calibre_automatic_sync_to_external_harddrive.svg?style=for-the-badge
[license-url]: https://github.com/boini12/calibre_automatic_sync_to_external_harddrive/blob/main/LICENSE.txt
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Qt]: https://img.shields.io/badge/Qt-41CD52?style=for-the-badge&logo=qt&logoColor=white
[Qt-url]: https://www.qt.io/
[Calibre]: https://img.shields.io/badge/Calibre-4B4B4B?style=for-the-badge&logo=calibre&logoColor=white
[Calibre-url]: https://calibre-ebook.com/
