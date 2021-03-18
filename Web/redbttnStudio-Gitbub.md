---
layout: post
author: "SeungJun Lee"
title:  "Redbttn Studio Development"
subtitle: "Development of a website using a Django library"
type: "WEB DEV."
projects: true
text: true
ridi: true
portfolio: true
post-header: true
header-img: "img/card.jpg"
main-img: "img/redbttn-home.jpg"
role-title: "Full Stack Dev."
role-specific: "Web Design, CORS Streaming, Python Crawling, AWS"
team: "All by myself"
platforms: "Web"
date: "May 2018 - Dec 2018"
order: 1
---


# Redbttn Studio Homepage
The website development of Red Button Studios in Sinsa-dong, Gangnam-gu, Korea.

Instagram: [@redbttnseoul](https://www.instagram.com/redbttnseoul/)



## Project interests
### Front-end

#### HLS Streaming
- Need real-time video streaming technology to match the self-video studio concept
- AWS CloudFront for simultaneous streaming to multiple connectors
- Video JS
#### Instagram Grid Style
- Real-time synchronized Instagram feed layout
#### Optimized for mobile(android & ios) and web
- CSS for devices which has multiple resolutions
- Video format with Android and iOS support

### Back-end
#### Crawling Bot
- Develop a crawling bot for real-time Instagram feed synchronization
- Modularize each function like a bot e.g. Log in, Crawling, Terminate
#### Server
- AWS EC2, Ubuntu 18.04
- Crontab(crawling bot with real-time scheduling)




## Dependency
- Python: 3.7.7
- Django: 2.2.5
- chromedriver: 79.0.3945


## Installing
{% highlight bash %}
pip3 install -r requirement.txt
{% endhighlight %}

to run parser.py:
- download chromedriver, unzip, move to  `HOME_PATH/chromedriver` (mac os / linux)


create a secret.json file with variables:

{% highlight bash %}
SECRET_KEY = 'secret_key_in_settings.py'
username = 'instagram_username'
password = 'instagram_password'
{% endhighlight %}

## Run
to make instagram database using crawling:
{% highlight bash %}
python3 parser.py
{% endhighlight %}
to run server:
{% highlight bash %}
python3 manage.py runserver
{% endhighlight %}


## Video
{%include youtube-video.html id="QO9K61NkzuA" %}


- [PC Version](https://youtu.be/w9NuSj_xY1o)
- [Mobile Version](https://youtu.be/pgPuoi7n1Uc)


## Skill
<p align="left">
    <img alt="python" src="https://img.shields.io/badge/Python- -black"/>
    <img alt="python-3.7.7" src="https://img.shields.io/badge/CSS-%20-blue"/>
    <img alt="" src="https://img.shields.io/badge/HTML-%20-orange"/>
    <img alt="javascript" src="https://img.shields.io/badge/JavaScript-%20-yellow"/>
    <img alt="JQuery" src="https://img.shields.io/badge/JQuery- -blue"/>
    <img alt="hls" src="https://img.shields.io/badge/HLS-%20-red"/>
    <img alt="videojs" src="https://img.shields.io/badge/VideoJS-%20-yellowgreen"/>
    <img alt="sqlite3" src="https://img.shields.io/badge/sqlite3- -blue"/>
    <img alt="selenuum" src="https://img.shields.io/badge/selenuum- -black"/>
    <img alt="beautifulsoup4" src="https://img.shields.io/badge/beautifulsoup4- -green"/>
    <img alt="AWS" src="https://img.shields.io/badge/AWS-%20-orange"/>
</p>


## Notion
https://www.notion.so/Back-end-fc842cd3273a4e10b82a9e7d550826ae

The notes include concerns about technical issues and solutions to the development of the homepage.

## Reference
- VideoJS

    https://videojs.github.io/videojs-contrib-hls/

-  Web Scraping Instagram with Selenium | by Mariyasha | Analytics Vidhya | Medium:

    https://medium.com/analytics-vidhya/web-scraping-instagram-with-selenium-b6b1f27b885
- Automate TINDER with Python tutorial:

    https://github.com/aj-4/tinder-swipe-bot

- Django  Project Deploy - 1. AWS

    https://nachwon.github.io/django-deploy-1-aws/

- SalesMore :: Amazon AWS :: Configuring HLS Streaming with Cloudfront

    https://salesmore.tistory.com/851

- Building Video Streaming Services (AWS s3/cloudFront, HLS, video.js) | Dev. Nam Lab.

    http://lab.naminsik.com/3960
