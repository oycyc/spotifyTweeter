Spotify Status Tweeter
======================

Spotify Status Tweeter is a Python script that tweets the status of your Spotify account every hour, including the song name, album (if any), artist, as well as an attached URL link to the song track. 

## How to use

Simply download the source code and make sure that the required packages are installed from pip. Input your credentials in the `secret.py` file, these can be created from the Twitter and Spotify Developer portals. Then, run `tweetSpotifySong.py` and it should work -- if you are playing a song, it will tweet that along with the song information, if not, it'll tweet that you're not listening to Spotify at the moment.

## Heroku

I run these files on Heroku, so I use their [scheduler add on](https://devcenter.heroku.com/articles/scheduler) to reduce my dyno hours (significantly). If you want to run this on your own machine, you can remove the comments from the scheduling code (sleep, schedule).

## Example

An example of this script in use is [BenjaTheWorst's Twitter account](https://twitter.com/to_spotify) -- the code in use is different, it only tweets if he is listening or not.
