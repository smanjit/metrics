from flask import Flask, render_template, flash, redirect, request, url_for, send_file, session
import xlwt
import string
#import sys
#print(sys.path)
#sys.path.append('C:\\Users\\IBM_ADMIN\\AppData\\Local\\Programs\\Python\\Python35')
#import textstat
from textstat.textstat import textstat
import cProfile

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('generateMetrics'))

@app.route('/generateMetrics', methods=["GET","POST"])
def generateMetrics():
	if request.method == "POST":
	    line = request.form['poem']
	    session['line'] = line	    
        #print("i am in row : ",row)
        #print "Tagline :", line
	    #print("no of words= ",len(line.split()))
	    #line1 = line.lstrip('0123456789.- ,')
	    #print "flesch_reading_ease = ",textstat.flesch_reading_ease(line)
	    fre = textstat.flesch_reading_ease(line)
	    session['fre'] = fre
	    #print "smog_index = ",textstat.smog_index(line)
	    smog = textstat.smog_index(line)
	    session['smog'] = smog
	    #print "flesch_kincaid_grade = ",textstat.flesch_kincaid_grade(line)
	    fkg = textstat.flesch_kincaid_grade(line)
	    session['fkg'] = fkg
	    #print "dale_chall_readability_score = ", textstat.dale_chall_readability_score(line)
	    dcr = textstat.dale_chall_readability_score(line)
	    session['dcr'] = dcr
	    #print "gunning_fog = ",textstat.gunning_fog(line)
	    gf = textstat.gunning_fog(line)
	    session['gf'] = gf
	    metrics = True
	    return render_template('generateMetrics.html',metrics=metrics, line=line, fre=fre, smog=smog, fkg=fkg, dcr=dcr,gf=gf)
	return render_template('generateMetrics.html')

@app.route('/download', methods=["GET","POST"])
def download():
	if request.method == "POST":
	    book = xlwt.Workbook()
	    worksheet = book.add_sheet('ReadabilityScore')
	    worksheet.write(0, 0, "Gen_sent")
	    worksheet.write(0, 1, "flesch_reading_ease")
	    worksheet.write(0, 2, "flesch_kincaid_grade")
	    worksheet.write(0, 3, "dale_chall_readability_score")
	    worksheet.write(0, 4, "gunning_fog")
	    row=1
	    worksheet.write(row,0,session['line'])
	    worksheet.write(row,1,session['fre'])
	    worksheet.write(row,2,session['fkg'])
	    worksheet.write(row,3,session['dcr'])
	    worksheet.write(row,4,session['gf'])
	    book.save('Readability_Scores.xls')
	    return send_file("Readability_Scores.xls",as_attachment='Readability_Scores.xls')

@app.route('/compareContents', methods=["GET","POST"])
def compareContents():
	if request.method == "POST":
	    line = request.form['poem']
	    poem1 = request.form['poem1']
		#---------Metrics comparison logic goes here. keep them in session attributes-----------------------#

	    session['line'] = line	    
        #print("i am in row : ",row)
        #print "Tagline :", line
	    #print("no of words= ",len(line.split()))
	    #line1 = line.lstrip('0123456789.- ,')
	    #print "flesch_reading_ease = ",textstat.flesch_reading_ease(line)
	    fre = textstat.flesch_reading_ease(line)
	    session['fre'] = fre
	    #print "smog_index = ",textstat.smog_index(line)
	    smog = textstat.smog_index(line)
	    session['smog'] = smog
	    #print "flesch_kincaid_grade = ",textstat.flesch_kincaid_grade(line)
	    fkg = textstat.flesch_kincaid_grade(line)
	    session['fkg'] = fkg
	    #print "dale_chall_readability_score = ", textstat.dale_chall_readability_score(line)
	    dcr = textstat.dale_chall_readability_score(line)
	    session['dcr'] = dcr
	    #print "gunning_fog = ",textstat.gunning_fog(line)
	    gf = textstat.gunning_fog(line)
	    session['gf'] = gf
	    metrics = True
	    return render_template('compareContents.html',metrics=metrics, line=line, fre=fre, smog=smog, fkg=fkg, dcr=dcr,gf=gf)
	return render_template('compareContents.html')

@app.route('/downloadMetrics', methods=["GET","POST"])
def downloadMetrics():
	if request.method == "POST":
	    book = xlwt.Workbook()
	    worksheet = book.add_sheet('ReadabilityScore')
	    worksheet.write(0, 0, "Gen_sent")
	    worksheet.write(0, 1, "flesch_reading_ease")
	    worksheet.write(0, 2, "flesch_kincaid_grade")
	    worksheet.write(0, 3, "dale_chall_readability_score")
	    worksheet.write(0, 4, "gunning_fog")
	    row=1
	    worksheet.write(row,0,session['line'])
	    worksheet.write(row,1,session['fre'])
	    worksheet.write(row,2,session['fkg'])
	    worksheet.write(row,3,session['dcr'])
	    worksheet.write(row,4,session['gf'])
	    book.save('Comparison_Scores.xls')
	    return send_file("Comparison_Scores.xls",as_attachment='Comparison_Scores.xls')

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host='0.0.0.0',port=5005,debug=True)