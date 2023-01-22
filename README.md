# fmovies-cli
Download movies from the CLI through fmovies.
![image](https://user-images.githubusercontent.com/49251143/213901019-32fef584-4668-443a-b34d-bfe7cad526f6.png)


# Future Features
* Setup a python env
* Multithreading to download multiple movies at once
* Option to play movie from VLC instead of downloading
* More robust searching that is interactive with user
* Have fmovie mirrors incase one goes down

# Known Bugs
* Searching for movie ocasionally throws an error. I suspect this has to do with hitting an ad when Selenium clicks the movie
    * Potential solution is to wrap in try/except block and keep trying until no error

# Usage

Current usage: `python3 fmovies.py [fmoviesUrl]` 
Future usage: `python3 fmovies.py [options] -url [fmoviesUrl]`

## Options (Coming soon...)
```
-h, -help                                          Prints this help text
-o                                                 Name of output file
-vcl                                               Play from VCL
-sub                                               Boolean flag for movie subtitles. English only.
-headless                                          Boolean flag for Selenium
-b                                                 Show .m3u8 link
```

# Requirements
 - python3
 - selenium
 - youtube_dl
 - google chrome

# What I learned
