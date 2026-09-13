# AAOI — Dead Simple Research card package

One folder = one ticker. Everything shareable for AAOI lives here, and every
file is standalone (CSS and images are embedded), so the folder can be copied
anywhere as-is.

## Files

- `card.html` — interactive click-to-flip card. The live artifact for the website.
- `card_data.json` — structured data (score, tier, thesis, valuation, performance vs the S&P 500).
- `card_front.png` / `card_back.png` — full-resolution card images for social.
- `card_front_web.png` / `card_back_web.png` — downsampled previews for the website grid.
- `README.md` — this file.

## Use on the website (deadsimple.money)

Copy this whole folder into the site repo at `public/cards/AAOI/`, then:

- Embed or link `card.html` as the live card artifact.
- Read `card_data.json` for any custom layout (status, Dead Simple Score, alpha vs S&P).

## Keeping it current

The performance block (current return / S&P return / alpha) is a snapshot taken
when this package was generated (`performance.mode = "live"`). To refresh it,
re-run `python make_media.py 20260913_153851` and re-upload this folder.

When the position is closed (`python card_lifecycle.py close AAOI`), the
numbers freeze at the close (`performance.mode = "frozen"`) and no longer change.

Status: Watchlist | Dead Simple Score: 83/100 | Schema v1
