import phonenumbers
from phonenumbers import geocoder

phone_number = "+1XXXXXXXXXX"  # replace XXXXXXXXXX with the target phone number
phone_number_object = phonenumbers.parse(phone_number)
print(geocoder.description_for_number(phone_number_object, "en"))