Here are a few questions we may want to answer about this data:

What was the name of the first person to play the game?
jq -r '.[1].name' data.json

What was the name of the last person to play the game?
jq -r '.[-1].name' data.json

Who had the highest score?
jq -r 'sort_by(.score)[-1].name' data.json
jq -r 'max_by(.score).name' data.json

The names of everyone who played the game directly after Daniel?
jq -r 'to_entries | . as $list | .[] | select(.value.name == "Daniel") | $list[.key + 1].value.name' data.json