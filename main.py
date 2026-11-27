# One sentence about the best meal ever had, written for the make.fun judge.
import os

SENTENCE = "My grandmother's chicken soup, eaten straight from the pot at midnight after the power cut, rain hammering the tin roof while the steam fogged my glasses."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()
