TradeStation Oauth Token Grabber
--------------------------------

This is a non-official tool for getting your API refresh-token to do automated
trading via the TradeStation API.

Since TS uses OAuth, it can be tricky to obtain these tokens sine you need a 
web service running to listen for the callback from tradestation.

To obtain your token, update `get_refresh_token.sh` with your API-KEY and SECRET.
Run the script with `./get_refresh_token.sh` (on Unix system). 

Your refresh token will be saved under `access_token.txt`.