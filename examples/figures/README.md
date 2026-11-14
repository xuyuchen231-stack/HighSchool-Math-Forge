# Reproducible figure outputs

Run from the repository root:

```bash
python -m pip install -r requirements.txt
python scripts/plot_examples.py --out examples/figures
```

This generates each figure as vector PDF and raster PNG:

| Figure | Mathematical content |
| --- | --- |
| `parabola_tangent` | `f(x)=x^2-4x+7`, tangent at `x=1` is `y=-2x+6` (verified by derivative and contact) |
| `rational_asymptote` | `y=1/(x-1)`, branch-wise sampling, vertical asymptote `x=1` |
| `unit_circle` | Unit circle, `30°`, point `(√3/2,1/2)` |
| `binomial_pmf` | Exact theoretical binomial distribution `n=10, p=0.3` |

The GitHub Actions workflow `.github/workflows/verify.yml` regenerates the images and uploads them as downloadable workflow artifacts; generated binary images are intentionally not committed to Git to keep source history compact. The packaged ZIP includes PNG/PDF figure outputs.
