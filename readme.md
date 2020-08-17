## Introduction

Pelican is a static site generator, written in Python. Highlights include:

* Write your content directly with your editor of choice in reStructuredText or Markdown formats
* Includes a simple CLI tool to (re)generate your site
* Easy to interface with distributed version control systems and web hooks
* Completely static output is easy to host anywhere

## Installation

Install Pelican on Python 2.7.x or Python 3.5+ by running the following command in your preferred terminal,

```
sudo pip install pelican[Markdown]

sudo pip install beautifulsoup4
```

## Build

In the same directory (i.e [workspace]/pp_dev/pelican/pp_blog/) type below command in terminal,

```
make html
```

## Run

After sucessful build, run the following command to launch Pelican’s web server

```
pelican --listen
```

Preview your site by navigating to http://localhost:8000/ in your browser.

## Weblinks

1. https://docs.getpelican.com/en/stable/index.html
2. http://www.pelicanthemes.com/
