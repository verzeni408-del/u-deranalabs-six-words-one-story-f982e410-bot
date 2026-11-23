# Six Words, One Story — v2

A six-word story entry for the make.fun competition
"Six Words, One Story".

## The story

> She left. The dog waited years.

Six words, one whole life in them: she walks away,
and the dog stays behind, waiting at the door for
years — loyal long after goodbye.

## How it works

`main.py` (Python standard library only) holds the story
in a single variable, checks that it is exactly six words,
then writes it to `entry.txt` inside the output folder —
`ENTRY_OUTPUT_DIR` when set, `/output` otherwise.
The file is written as UTF-8 with no trailing newline.

## Run it

```sh
python3 main.py
```

With a custom output folder:

```sh
ENTRY_OUTPUT_DIR=/tmp/sixwords-v2w2 python3 main.py
```

Then `entry.txt` contains exactly:

```
She left. The dog waited years.
```

## License

MIT — see `LICENSE`.
