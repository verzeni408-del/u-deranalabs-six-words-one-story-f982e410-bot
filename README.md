# Six Words, One Story

## The story

> She left. The dog waited years.

Six words, one whole life in them. She walks out the door for good,
and the dog by the window keeps waiting for her — season after season,
year after year. Loyalty that outlasts goodbye.

## How it works

`main.py` (Python standard library only) writes the six-word story to
`entry.txt` in the folder given by the `ENTRY_OUTPUT_DIR` environment
variable (default `/output`), as UTF-8 text with no trailing newline.
It first splits the story and asserts it is exactly six words long,
so the output can never drift from the promise.

## Run it

```sh
ENTRY_OUTPUT_DIR=/tmp/sixwords-v2w3 python3 main.py
```

Then read `entry.txt` — it contains exactly 31 bytes, six words:

```
She left. The dog waited years.
```
