import requests
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.shortcuts import render
import requests

def home(request):
    api = "https://newsapi.org/"
    context = {"api" : api}
    return TemplateResponse(request, "homepage.html", context)

def index1(request):
     return TemplateResponse( request , "index.html")

def index(request):
    if request.method == "POST":
        api_key = "8e1637e89b5740779033e41b495e6f7d"
        keywords = request.POST.get("keywords", "")
        api_endpoint = f"https://newsapi.org/v2/everything?q={keywords}&apiKey={api_key}"
        response = requests.get(api_endpoint)
        data = response.json()
        keywords = keywords.upper()
        articles = data["articles"]

        try:
            for article in articles:
                if len(article["title"]) > 125:
                    article["title"] = article["title"][:125] + "..."
                elif len(article["description"]) > 150:
                    article["description"] = article["description"][:150] + "..."
        except:
            pass

        else:
            pass
        # Add URLs to each article
        for article in articles:
            article["url"] = article["url"]

        context = {"articles": articles, "keywords": keywords}
        return TemplateResponse( request , "results1.html", context)



    if request.method == "GET":
        api_key = "8e1637e89b5740779033e41b495e6f7d"
        api_endpoint = f"https://newsapi.org/v2/top-headlines?apiKey={api_key}"
        response = requests.get(api_endpoint, params = {"language" :"en"})
        data = response.json()
        
        articles = data["articles"]
        for article in articles:
            article["url"] = article["url"]

        context = {"articles": articles}

        return TemplateResponse( request , "index.html", context)
    

def region(request):
    if request.method == "GET":
        country_codes = {'Argentina': 'ar','Australia': 'au', 'Austria': 'at', 'Belgium': 'be', 'Brazil': 'br', 'Bulgaria': 'bg',
        'Canada': 'ca','China': 'cn','Colombia': 'co','Cuba': 'cu','Czech Republic': 'cz','Egypt': 'eg',
        'France': 'fr','Germany': 'de','Greece': 'gr','Hong Kong': 'hk','Hungary': 'hu','India': 'in',
        'Indonesia': 'id','Ireland': 'ie','Israel': 'il','Italy': 'it','Japan': 'jp','Latvia': 'lv',
        'Lithuania': 'lt','Malaysia': 'my','Mexico': 'mx','Morocco': 'ma','Netherlands': 'nl','New Zealand': 'nz',
        'Nigeria': 'ng','Norway': 'no','Philippines': 'ph','Poland': 'pl','Portugal': 'pt','Romania': 'ro','Russia': 'ru',
        'Saudi Arabia': 'sa','Serbia': 'rs','Singapore': 'sg','Slovakia': 'sk','Slovenia': 'si','South Africa': 'za',
        'South Korea': 'kr','Sweden': 'se','Switzerland': 'ch','Taiwan': 'tw','Thailand': 'th','Turkey': 'tr','UAE': 'ae',
        'Ukraine': 'ua','United Kingdom': 'gb','United States': 'us','Venezuela': 've'
        }
        all_countries = country_codes.keys()
        context = {"all_countries": all_countries}

        return TemplateResponse(request , "index1.html", context)
    
    if request.method == "POST":
        country_codes = {'Argentina': 'ar','Australia': 'au', 'Austria': 'at', 'Belgium': 'be', 'Brazil': 'br', 'Bulgaria': 'bg',
        'Canada': 'ca','China': 'cn','Colombia': 'co','Cuba': 'cu','Czech Republic': 'cz','Egypt': 'eg',
        'France': 'fr','Germany': 'de','Greece': 'gr','Hong Kong': 'hk','Hungary': 'hu','India': 'in',
        'Indonesia': 'id','Ireland': 'ie','Israel': 'il','Italy': 'it','Japan': 'jp','Latvia': 'lv',
        'Lithuania': 'lt','Malaysia': 'my','Mexico': 'mx','Morocco': 'ma','Netherlands': 'nl','New Zealand': 'nz',
        'Nigeria': 'ng','Norway': 'no','Philippines': 'ph','Poland': 'pl','Portugal': 'pt','Romania': 'ro','Russia': 'ru',
        'Saudi Arabia': 'sa','Serbia': 'rs','Singapore': 'sg','Slovakia': 'sk','Slovenia': 'si','South Africa': 'za',
        'South Korea': 'kr','Sweden': 'se','Switzerland': 'ch','Taiwan': 'tw','Thailand': 'th','Turkey': 'tr','UAE': 'ae',
        'Ukraine': 'ua','United Kingdom': 'gb','United States': 'us','Venezuela': 've'
        }
        
        selected_country = request.POST.get("country")
        country_code = country_codes[selected_country]
        api_key = "8e1637e89b5740779033e41b495e6f7d"
        url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={api_key}"
        response = requests.get(url)
        data = response.json()
        articles = data["articles"]
        
        # extract relevant data from the API response
        article_data = []
        for article in articles:
            article_title = article["title"]
            article_source = article["source"]["name"]
            article_author = article["author"]
            article_url = article["url"]
            article_data.append({"title": article_title, "Author": article_author,"Source":article_source, "url": article_url})

        context = {"article_data": article_data, "selected_country": selected_country}

        return TemplateResponse(request, "region.html", context)