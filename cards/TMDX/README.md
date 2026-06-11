# TMDX — Dead Simple Research card package

One folder = one ticker. Everything shareable for TMDX lives here, and every
file is standalone (CSS and images are embedded), so the folder can be copied
anywhere as-is.

## Files

- `card.html` — interactive click-to-flip card. The live artifact for the website.
- `card_data.json` — structured data (score, tier, thesis, valuation, performance vs the S&P 500).
- `card_front.png` / `card_back.png` — full-resolution card images for social.
- `card_front_web.png` / `card_back_web.png` — downsampled previews for the website grid.
- `youtube_thumbnail.jpg` — 16:9 thumbnail (JPEG, under YouTube's 2 MB limit).
- `substack_header.png` — 2:1 header.
- `x_post.md` — X/socials post draft.
- `video_talking_points.md` — short-video talking points.
- `README.md` — this file.

## Use on social

Post `card_front.png` / `card_back.png`, `youtube_thumbnail.jpg`,
`substack_header.png`, and the text drafts directly.

## Use on the website (deadsimple.money)

Copy this whole folder into the site repo at `public/cards/TMDX/`, then:

- Embed or link `card.html` as the live card artifact.
- Read `card_data.json` for any custom layout (status, Dead Simple Score, alpha vs S&P).

## Keeping it current

The performance block (current return / S&P return / alpha) is a snapshot taken
when this package was generated (`performance.mode = "live"`). To refresh it,
re-run `python make_media.py 20260611_180826` and re-upload this folder.

When the position is closed (`python card_lifecycle.py close TMDX`), the
numbers freeze at the close (`performance.mode = "frozen"`) and no longer change.

Status: Watchlist | Dead Simple Score: 90/100 | Schema v1
