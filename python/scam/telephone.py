import phonenumbers
from phonenumbers import geocoder
ch_number = phonenumbers.parse("7733549676", "GB")
out = geocoder.description_for_number(ch_number, "en")
print(out)
