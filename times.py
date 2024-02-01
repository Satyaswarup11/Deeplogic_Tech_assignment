from flask import Flask, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/getTimeStories')
def six_stories():
    try:
        response = requests.get("https://time.com")
        if response.status_code == 200:
            html_content = response.text
            matches = re.search(r'<div class="partial latest-stories" data-module_name="Latest Stories">(.*?)</div>',html_content, re.DOTALL)
            if matches:
                div=matches.group(1)
                pattern = r'<li class="latest-stories__item">\s*<a href="([^"]+)">\s*<h3 class="latest-stories__item-headline">(.*?)</h3>\s*</a>'
                six_stories = re.findall(pattern, div)[:6] #For getting latest six stories
                stories=[]
                for link, title in six_stories:
                    stories.append({"title": title.strip(), "link": "https://time.com" + link}) 
                return jsonify(stories)
            else:return []
        else:
            return jsonify({"error": f"Failed to fetch Time.com content. Status code: {response.status_code}"})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
