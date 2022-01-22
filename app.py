from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/review',methods=['POST','GET']) # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","")

            imdb_url = "https://www.imdb.com/find?q=" + searchString
            uClient = uReq(imdb_url)
            imdbPage = uClient.read()
            uClient.close()
            imdb_html = bs(imdbPage, "html.parser")
            bigboxes = imdb_html.findAll("div", {"class": "findSection"})
            box = bigboxes[0]

            movie_url = "https://www.imdb.com" + box.table.tr.td.a['href']
            uClient = uReq(movie_url)
            moviePage = uClient.read()
            uClient.close()

            movieRes = requests.get(movie_url)
            movieRes.encoding = 'utf-8'
            movie_html = bs(movieRes.text, "html.parser")

            review_link = movie_url + 'reviews/?ref_=tt_ql_urv'

            reviewRes = requests.get(review_link)
            reviewRes.encoding = 'utf-8'
            review_html = bs(reviewRes.text, "html.parser")
            print(review_html)
            reviewboxes = review_html.find_all('div', {'class': 'lister-item-content'})

            filename = searchString + ".csv"
            fw = open(filename, "w")
            headers = "MOVIE NAME,REVIEW DATE,REVIEWER,RATING,TITLE,REVIEW \n"
            fw.write(headers)
            reviews = []
            for commentbox in reviewboxes:

                try:
                    #commentDate.encode(encoding='utf-8')
                    commentDate = commentbox.find('span',{'class' :'review-date'}).text

                except:
                    commentDate = 'No Comment Date'


                try:
                    #name.encode(encoding='utf-8')
                    name = commentbox.find('span',{'class':'display-name-link'}).text

                except:
                    name = 'No Name'

                try:
                    #rating.encode(encoding='utf-8')
                    rating = commentbox.div.span.span.text


                except:
                    rating = 'No Rating'

                try:
                    #commentHead.encode(encoding='utf-8')
                    commentHead = commentbox.a.text

                except:
                    commentHead = 'No Comment Heading'
                try:
                    #custComment.encode(encoding='utf-8')
                    custComment = commentbox.find('div',{'class':'text show-more__control'}).text

                except Exception as e:
                    print("Exception while creating dictionary: ",e)



                mydict = {"MOVIE NAME": searchString,"REVIEW DATE": commentDate , "REVIEWER": name, "RATING": rating, "TITLE": commentHead,
                          "REVIEW": custComment}
                reviews.append(mydict)
            return render_template('results.html', reviews=reviews[0:(len(reviews)-1)])
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')

    else:
        return render_template('index.html')

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True)
