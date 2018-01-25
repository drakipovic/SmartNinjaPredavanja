from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

csv_emails = open("emails.csv", "w")

url = 'https://scrapebook22.appspot.com/'

response = urlopen(url).read()

soup = BeautifulSoup(response)

for link in soup.findAll('a'):

    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_response = urlopen(person_url).read()

        person_soup = BeautifulSoup(person_response)
        name = person_soup.findAll('h1')[1].string

        person_details = person_soup.findAll('li')

        gender = person_details[0].span.string
        age = person_details[1].string[5:]
        city = person_details[2].span.string

        email = person_soup.find("span", attrs={"class": "email"}).string
        csv_emails.write("{},{},{},{},{}\n".format(name, gender, age, email, city))


csv_emails.close()