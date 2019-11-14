from flask import Flask
from flask import request
from flask import render_template
import os
app = Flask(__name__)

@app.route('/')
def root():
  vards = request.args.get('vards', default = 'pasaule', type = str)
  return render_template('sveikaPasaule.html', vards = vards)

#visi attēli ievietoti mapē static, apakšmapē pictures
@app.route('/bildes')
def visasBildes():
  pictures = os.listdir('static/pictures/') 
  return render_template("home.html", pictures=pictures)

@app.route('/bilde/<bildesID>')
def bilde(bildesID):
  return render_template('bilde.html', bildesID = bildesID)

@app.route('/komentari/<komentaraID>')
def komentars(komentaraID):
  atrastaisKomentars = ""
  try:
    fp = open('komentari.txt')
    line = fp.readline()
    cnt = 0
    while line:
      print("cnt: {}, komentaraID: {}".format(cnt, komentaraID))
      if cnt == int(komentaraID):
        print("Line {}: {}".format(cnt, line.strip()))
        atrastaisKomentars = line
      line = fp.readline()
      cnt += 1
  finally:
    fp.close()
  return render_template('komentars.html', komentars = atrastaisKomentars)

@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run()
