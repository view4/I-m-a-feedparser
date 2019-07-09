from bottle import static_file, template, run, route, get
import feedparser
import json

feed=feedparser.parse("http://feeds.wired.com/wired/index")
food=[]
for element in feed["entries"]:
    object={
        "title":element["title"],
        "link":element['link']
    }
    food.append(object)
print(food)

@route("/")
def index():
    return static_file("index.html", root='')

@route('/get_feeds')
def default():
    return json.dumps(food)

@get('/js/<filename:re:.*\.js>')
def stylesheets(filename):
    return static_file(filename, root='js')

def main():
    run(host='localhost', port=8000)


if __name__ == '__main__':
    main()



