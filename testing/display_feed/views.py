import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, HttpResponse


def index(request):
    url = "https://themeisle.com/blog/best-free-blogging-sites/"
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    heading = soup.find("h1").text
    one = soup.find("h3", id="Wix").text
    two = soup.find("h3", id="WordPress").text
    three = soup.find("h3", id="LinkedIn").text
    four = soup.find("h3", id="Weebly").text
    five = soup.find("h3", id="Medium").text
    six = soup.find("h3", id="Ghost").text
    seven = soup.find("h3", id="Blogger").text
    eight = soup.find("h3", id="Tumblr").text
    nine = soup.find("h3", id="Joomla").text

    news_item = {'heading': heading, 'one': one, 'two': two, 'three': three, 'four': four, 'five': five, 'six': six, 'seven': seven,
                 'eight': eight, 'nine': nine}
    return render(request, 'test/hello.html', news_item)

