from flask import Flask, request, jsonify, request, send_from_directory
import db

app = Flask(__name__)

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/afspraak', methods=['POST'])
def afspraak_invoegen():
    data = request.json
    db.execute_sql("INSERT INTO afspraak(naam, email, tijdstip) VALUES ('{}','{}','{}')".format(data['naam'], data['email'], data['tijdstip']))
    return jsonify({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/afspraken', methods=['GET'])
def vraag_afspraken_op():
    dbafspraken = db.execute_sql('SELECT * FROM afspraak ORDER BY tijdstip')

    afspraken = []
    for afspraak in dbafspraken:
        afspraken.append(
            {'naam':afspraak['naam'] , 'tijdstip': afspraak['tijdstip'] }
        )
    
    return jsonify(afspraken), 200, {'ContentType': 'application/json'}


app.run()