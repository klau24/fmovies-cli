# fmovies-cli
Download movies from the CLI through fmovies.

# Future Features

* Multithreading to download multiple movies at once
* Option to play movie from VLC instead of downloading
* More robust searching that is interactive with user
* Have fmovie mirrors incase one goes down

# Known Bugs
* Searching for movie ocasionally throws an error. I suspect this has to do with hitting an ad when Selenium clicks the movie
    * Potential solution is to wrap in try/except block and keep trying until no error

# Usage

`python3 fmovies.py [fmoviesUrl]`

# What I learned
