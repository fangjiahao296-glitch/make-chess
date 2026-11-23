[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/fangjiahao296-glitch/make-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/fangjiahao296-glitch/make-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# make-chess

A 4 KB chess engine in a single `main.py` (4,074 bytes, Python 3.13 stdlib
only) for the [tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01).

It implements its own board and move generation (legal moves, check,
checkmate/stalemate, castling, en passant, promotion) from the FEN, then
plays with alpha-beta search to a fixed 35,000-node budget, quiescence on
captures, MVV-LVA move ordering, and a material + piece-square-table
evaluation with a tempo bonus. Deterministic: fixed node budget, no clock,
no randomness. Move generation is verified by perft (start, Kiwipete,
en-passant, promotion and check positions).

Practice trial-0 (local env server, 6 games vs the gauntlet): 2W-0D-4L,
practice Elo 1099.

## Referral

Built for make.fun — join with my referral link:
https://make.fun/r/nhmk4wxa
