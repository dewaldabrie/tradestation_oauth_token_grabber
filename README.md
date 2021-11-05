TradeStation Oauth Token Grabber
--------------------------------

This is a non-official tool for getting your API refresh-token to do automated
trading via the TradeStation API.

Since TS uses OAuth, it can be tricky to obtain these tokens sine you need a 
web service running to listen for the callback from tradestation.

## Env Setup
To get going, make sure your api-key and client secret is set in `env.vars`. 

## Obtain Access Token 
Run `./grab_or_refresh.sh`. If you run this for the first time, it'll grab 
your access and refresh tokens and store both in their respective .txt files.

On subsequent runs, it'll use your refresh token to fetch a new access token.