import unicodedata
import re

def slugify(value: str, allow_unicode=False) -> str:
    
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize("NFKC", value)
    else:
        value = (
            unicodedata.normalize("NFKD", value)
            .encode("ascii", "ignore")
            .decode("ascii")
        )
    
    return re.sub(r"[-\s/]+", "-", value).strip("-_")

test = "Hi/ my name   isJoe"
print(slugify(test))