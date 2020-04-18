import connexion
import math
import random
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from entry import Entry

DB_ENGINE = create_engine('sqlite:///images.sqlite')
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)


def get_image():
    pic_id = math.floor(random.random() * 1000 + 1)
    url = "https://i.picsum.photos/id/" + str(pic_id) + "/200/300.jpg"
    return url, 200


def save_image(image):
    print(image)
    image = Entry(image["image"])

    session = DB_SESSION()
    session.add(image)
    session.commit()
    session.close()
    return 200


def get_all():
    results_list = []
    session = DB_SESSION()
    results = session.query(Entry).all()
    for item in results:
        results_list.append(item.get_url())

    print(results_list)
    session.close()
    return results_list


app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yaml")
CORS(app.app)
app.app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == "__main__":
    app.run(port=8090)