# Console Weather App |  [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Get%20over%20170%20free%20design%20blocks%20based%20on%20Bootstrap%204&url=https://www.froala.com/design-blocks&via=froala&hashtags=bootstrap,design,templates,blocks,developers)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Degamisu/Console-Weather-App) ![GitHub commits since latest release](https://img.shields.io/github/commits-since/Degamisu/Console-Weather-App/latest)
 ![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Degamisu/Console-Weather-App) ![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/Degamisu/Console-Weather-App/total) [![Build and Release](https://github.com/Degamisu/Console-Weather-App/actions/workflows/build_and_release.yml/badge.svg?branch=master)](https://github.com/Degamisu/Console-Weather-App/actions/workflows/build_and_release.yml) ![GitHub closed issues](https://img.shields.io/github/issues-closed/Degamisu/console-weather-app) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Degamisu/Console-Weather-App)


## Live Viewers

![Viewers](https://img.shields.io/github/watchers/degamisu/console-weather-app)

---
<div>
<p align="center">
  <img src="/CWA-2-transparent.png"/>
</p>
</div>

> Console Weather Logo subject to copyright. © Degamisu, Emi Yamashita.

## About

This app is a console-based weather app. You can choose between 2 options for location. You can **Specify** the location, or you can automatically find the location based off of **GPS tracking**. This is a very fast and reliable service that is being updated frequently.

## Important Information

The Legacy version of CWA is available [here](https://github.com/Degamisu/Console-Weather-App/tree/b6d01375763cd0d073334d68de05902801dd546b). It has the following:

- Stable application
- Normal integrated `print()` functions
- Accurate weather statements
- There is **no** city select. You will get an error: `City Select is not implemented yet, CWA will now quit`
- There is **no** [autoinstall](autoinstall.bash). You will have to build/run this _manually_

---

This app contains a `secret` code to function properly. In some parts of the code, a variable named `{GH_TOKEN}` is created. However, if you use Codespaces, you must provide your own `secret` code for the scripts to work. (eg, [build_and_release.yml - Github Actions](build_and_release.yml))

---

There is a wiki! you can find this in the `wiki` tab. The tab includes:

- Directory Graph
- Error Codes
- Information
- Dependencies

## Security

> [!NOTE]
> For more details in security, go to [SECURITY](SECURITY.md)

Privacy is a top concern for users, especially when it comes to applications that involve location tracking. Rest assured, the Console Weather App prioritizes user privacy and follows these principles:

- **No Personal Information Collection:** The app does not collect any personal information or location data beyond what is necessary for gathering weather information.

- **Local Console Usage:** Your location is used solely within the console environment to fetch real-time weather data. It is not transmitted or stored externally.

- **Broad Location Data:** The app only accesses broad location information, ensuring that no specific details are leaked.

It's important to note that the safety of the app depends on its usage and commitment to the official repository. If you ever fork the project, please review the code to ensure its safety.

Still unsure? You may check the code for yourself. Any comments and concerns can be in the `Discussions` tab or `Issues` tab. Any vulnerabilities that arise may go into the `Issues` tab. 


## Sources

This app gets its weather data with:

- Geocoder
- [Open Metro API](https://api.open-meteo.com/v1/forecastP|)

Making this app very fast and reliable.

## Installation (with source AutoInstall)

To make it easier to build, I created a script that does all the building for you. The file is called [AutoInstall](autoinstall.bash). This makes the build process faster, but there are a few disadvantages

- Deletes the Build process source code (generated automatically)
- One set path.

## Installation (with source)

> [!NOTE]
> - This currently only works on Ubuntu Linux. This may change.
> - Git must be installed. Install it with [this](InstallGit.bash)
> - This is good if you want to _keep_ the build artifacts and mess with a few files.

<details>
<summary>Download Source Code</summary>

To install the source code, run this command in any terminal:

```bash
mkdir Console-Weather-App-Source && cd Console-Weather-App-Source && gh repo clone Degamisu/Console-Weather-App && cd Console-Weather-App
```
This should download the source
</details>
<details>
<summary>Install Dependencies</summary>
This is the install command to install necissary dependencies.

```bash
pip install -r requirements.txt
```

**THIS IS CRUCIAL** to the installation of CWA.
</details>

---
**The next part can be done in 2 ways**

<details>
<summary>Build the executable</summary>

__This requires `pyinstaller` to build, which is installed under the `Install Dependencies` dropdown__

---

To build, run this into your bash console
```bash
pyinstaller --onefile main.py
```

</details>
<details>
<summary>Run directly</summary>
This is the easiest way through, skipping the building part. However, it would be harder to transport.


---

**Python**
```bash
cd dist && python main.py
```

**Python3**
```bash
cd dist && python3 ./main.py
```

</details>

---

This section is optional.

<details>
<summary>Cleanup</summary>

To clean up build artifacts (under /build), run this script:

```bash
rm -r build
```
</details>

---

## Contributing

Have an idea for CWA? Contributing will be open soon. For now, you can open issues!

---

## Additions

| Filename | Added             |
| ------- | ------------------ |
| SECURITY.md | ✔️ |
| CONTRIBUTING.md  | :x:                |
| README.md | ✔️|
| LICENCE.md | ✔️ |
| CODE_OF_CONDUCT.md | ✔️ |

---

**Is this readme missing something? If so, shoot a pull request! I will review it ASAP!**

© 2024 Degamisu | All Rights Reserved | [README](README.md) Created by **Emi Yamashita**
