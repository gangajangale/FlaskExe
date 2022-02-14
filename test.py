from flask import Flask, render_template, request, jsonify, json
import psycopg2
import psycopg2.extras

app = Flask(__name__)

conn = psycopg2.connect(database="country_db",
                        user='postgres', password='admin',
                        host='127.0.0.1', port='5432'
                        )
cr = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
conn.autocommit = True

#sql1 = '''CREATE TABLE Country_db65 (id int NOT NULL,Country varchar(200),Alpha2_code char(30),Alpha3_code char(30),
 #Numeric_code int,Latitude float,Longitude float);'''
#cr.execute(sql1)

sql2 = '''copy Country_db65(id,Country,Alpha2_code,Alpha3_code,Numeric_code,Latitude,Longitude)
FROM 'D://countries.csv'
DELIMITER ','
CSV HEADER;'''

cr.execute(sql2)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({
        'message': 'Welcome'
    })

@app.route('/country_db', methods=['GET'])
def country():
    cr.execute('select * from country_db3 limit 10')
    country = cr.fetchall()
    countries = []
    for row in country:
        countries.append(dict(row))
    return jsonify(countries)


@app.route('/country_db_startwitha', methods=['GET'])
def country_db_startwitha():
    cr.execute("select * from country_db65 where id=2 and country like 'A%' ")
    country= cr.fetchall()
    countries = []
    for row in country:
        countries.append(dict(row))
    return jsonify(countries)


@app.route('/country_db_id/<id>', methods=['GET'])
def country_db_id(id):
    #args = request.args
    #country = request.args.get('country')
    cr.execute("select * from country_db65  where id=%s",[id])
    country = cr.fetchall()
    countries = []
    for row in country:
     countries.append(dict(row))
    return jsonify(countries)

#    return jsonify(tb)


if __name__ == '__main__':
    app.run(debug=True)