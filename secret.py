import spotipy.util as util
import tweepy

def spotifyToken():
    username = ""
    clientID = ""
    clientSecret = ""
    redirect_url = "http://yangciou.com/" # defined in Spotify Developer App
    scope = "user-read-currently-playing"
            ## what information it's getting
            ## https://developer.spotify.com/documentation/general/guides/scopes/
    return util.prompt_for_user_token(username, scope, clientID, clientSecret, redirect_url)

def twitterAuthentication():
    apiKey = ""
    apiSecretKey = ""
    accessToken = ""
    accessTokenSecret = ""
    auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
    auth.set_access_token(accessToken, accessTokenSecret)
    return auth
