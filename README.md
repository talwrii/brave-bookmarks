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

# About me
I am @readwithai. I make tools related to reading and research sometimes usings [Obsidian](https://readwithai.substack.com/p/what-exactly-is-obsidian
).

If you found this repository interesting you might like to:
1. Check out this [page of similar useful command-line tools](https://readwithai.substack.com/p/my-productivity-tools)
2. Have a look at [my command-line snippet tool, zshnip](https://github.com/facetframer/zshnip)
3. Follow me on [X](https//x.com/readwithai) where I post about this sort of thing.

You could also look at my [blog](https://readwithai.substack.com/) where I write about reading and research.

![readwithai logo](logo.png)
