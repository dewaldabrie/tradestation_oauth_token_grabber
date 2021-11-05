eval `cat env.vars`;
export KEY=$KEY;
export SECRET=$SECRET;

if [ ! -d .venv ]; then
  python3 -m venv .venv
  .venv/bin/pip install flask requests
fi

REFRESH_TOKEN_FILE=refresh_token.txt
if test -f "$REFRESH_TOKEN_FILE"; then
  echo "Refreshing access token..."
  .venv/bin/python refresh_access_token.py;
else
  echo "Grabbing access and refresh tokens..."
  export FLASK_APP=flask_app;
  .venv/bin/python -m flask run --port 3000 &
  sleep 2;
  .venv/bin/python grab_all_tokens.py;
  pkill -P $$
fi