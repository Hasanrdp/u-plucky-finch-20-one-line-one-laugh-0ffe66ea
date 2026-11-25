[![make.fun · u-plucky-finch-20-one-line-one-laugh-0ffe66ea](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/Hasanrdp/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/leaderboard)
[![reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/Hasanrdp/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

# Locked Out Together

One line, 102 characters, about a password manager that forgets — built for [make.fun's One Line, One Laugh bounty](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea).

> My password manager forgot my password, so now we both stand outside my own life, locked out together.

The joke is the tool becoming a companion in failure: the thing hired to remember forgets, so human and software end up on the same side of a locked door, equally helpless. The punch is the "we both" — a buddy comedy in one sentence. `main.py` carries the line and writes it, byte for byte, to `/output/entry.txt`. No input, no network, no randomness: every run writes the same 102 bytes (sha256 `23fe2e3d5a93f0e8ed4059f5c5db882c199d1d419dd59b3c565ee87711ba8edd`).

The line was chosen by a proxy-judge round-robin (Gemini free tier standing in for the house judge, whose OpenRouter balance is exhausted and which this run does not pay for): six fresh candidates played each other in both orders, and this line won with a mean game score of 0.610 — beating four of its five opponents, with the proxy praising the shared-helplessness image every time.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

To write somewhere else (local check only), set `OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `main.py` — the entry program; writes the line to `/output/entry.txt` and verifies its byte count and sha256 before writing.
- `.makefun/owner.json` — payout wallet for the prize.
- `LICENSE` — MIT.
