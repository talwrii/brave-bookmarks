# Brave Bookmarks
This is a command-line script to query Brave's bookmark. It was written on linux but can be quickly adapted for other systems.

# Alternative's and prior work
There are other some other command-line tools to search browser bookmarks from the command-line. Many of these do not support Brave but instead support a combination of Firefox and Chrome. Brave is based on chromium and appears to keep bookmarks in the same format so these could likely be adapted to Brave. However, this task is quite simple and I wanted something that worked with Brave without modification or indeed *any* configuration.

[browser bookmark manager](https://github.com/crunchtime-ali/browser-bookmark-manager) by  Frisch is a command line tool to search browsers with Firefox or Chrome.

[pbm](https://github.com/westurner/pbm) is a bookmark search tool for chrome.

Firefox, Chrome and Brave all have quite easily accessible bookmark data. Chrome and Brave's format is simpler as they provide human readable JSON. Firefox provides and `sqlite` database. For more programmatic use cases, you might prefer to read these files directly.

# Install
This package is written in Python, you can use [pipx]() to install it.

```
pipx install brave-bookmarks
```

# Usage

```
bravemarks
```

Will list the names of all bookmarks

```
bravemark $name
```

Will show the url of the bookmark named `$name`.
