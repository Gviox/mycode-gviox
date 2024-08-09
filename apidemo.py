import request

baseurl = "https://aux1-00e0c795-7986-4a2c-8053-bdc270b1e23a.live.alta3.com/horoscope/"

sign = input("what's your sign?\n>")
url = baseurl + sign

response = request.get(url)

response = response.json()

print(response["lucky_color"])

print(response)
 
