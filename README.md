# Brave Bookmarks
@readwithai - [X](https://x.com/readwithai) - [blog](https://readwithai.substack.com/) - [machine-aided reading]()

This is a command-line script to query Brave's bookmark. It was written on linux but can be quickly adapted for other systems.

# Alternative's and prior work
There are other some other command-line tools to search browser bookmarks from the command-line. Many of these do not support Brave but instead support a combination of Firefox and Chrome. Brave is based on chromium and appears to keep bookmarks in the same format so these could likely be adapted to Brave. However, this task is quite simple and I wanted something that worked with Brave without modification or indeed *any* configuration.

[browser bookmark manager](https://github.com/crunchtime-ali/browser-bookmark-manager) by  Frisch is a command line tool to search browsers with Firefox or Chrome.

[pbm](https://github.com/westurner/pbm) is a bookmark search tool for chrome.

Firefox, Chrome and Brave all have quite easily accessible bookmark data. Chrome and Brave's format is simpler as they provide human readable JSON. Firefox provides and `sqlite` database. For more programmatic use cases, you might prefer to read these files directly.

# Install
This package is written in Python, you can use [pipx](https://github.com/pypa/pipx) to install it.

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


You can use this script as is, but if you access bookmarks a lot you might like to add a little automation. I use my [zshnip snippet framework](https://github.com/facetframer/zshnip) together with [fzf](https://github.com/junegunn/fzf) and [xclip](https://github.com/astrand/xclip) to make some useful snippets to make using these commands even more convenient. These features are not merged into the program because they would both be brittle and different users likely want different automations. Users might like to combine these with command-line shell scripts, shell aliases, or GUI keyboard shortcuts (potentially together with a GUI fuzzy selector- like [rofi](https://github.com/adi1090x/rofi))

I use the following [zshnip](https://github.com/facetframer/zshnip) snippets.

```
bmz -> bravemarks | fzf
bmg -> bravemarks | grep
bmzcli -> bravemarks | fzf | xargs bravemark | xclip -selection clipboard -i
```

# Missing features
* Support for mac or windows
* Ability to filter to tag
* Profiles

I will likely implement these if and when I need them. I am open to patches for these (as in I will merge them within days and rerelease).

# Support
If you found this piece of software useful you can donate ($2 maybe) to [my ko-fi]( https://ko-fi.com/c/409f19e716).

This will incentivize me to respond to feature requests for this project and create [similar command-line tools](https://readwithai.substack.com/p/my-productivity-tools).

# About me
I am @readwithai. I make tools related to reading and research sometimes usings [Obsidian](https://readwithai.substack.com/p/what-exactly-is-obsidian
).

If you found this repository interesting you might like to:
1. Check out this [page of similar useful command-line tools](https://readwithai.substack.com/p/my-productivity-tools)
2. Have a look at [my command-line snippet tool, zshnip](https://github.com/facetframer/zshnip)
3. Follow me on [X](https//x.com/readwithai) where I post about this sort of thing.

You could also look at my [blog](https://readwithai.substack.com/) where I write about reading and research; or check out the [machine-aided reading subreddit](https://www.reddit.com/r/machineAidedReading/)

![readwithai logo](logo.png)
