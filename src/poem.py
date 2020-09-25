from flask import flash, Flask, redirect, render_template, url_for, session, request, send_file, after_this_request
import xlwt
import string
#import sys
#print(sys.path)
#sys.path.append('C:\\Users\\IBM_ADMIN\\AppData\\Local\\Programs\\Python\\Python35')
#import textstat
from textstat.textstat import textstat
import cProfile

app = Flask(__name__)

def f():
 print("hello")
 book = xlwt.Workbook()
 worksheet = book.add_sheet('ReadabilityScore')
 worksheet.write(0, 0, "Gen_sent")
 worksheet.write(0, 1, "flesch_reading_ease")
 worksheet.write(0, 2, "flesch_kincaid_grade")
 worksheet.write(0, 3, "dale_chall_readability_score")
 worksheet.write(0, 4, "gunning_fog")

 f = open('abc.txt') #, encoding='utf-8')
 row=1
 for line in iter(f):
        #print("i am in row : ",row)
        #print "Tagline :", line
        worksheet.write(row,0,line)
        #print("no of words= ",len(line.split()))
        #line1 = line.lstrip('0123456789.- ,')
        #print "flesch_reading_ease = ",textstat.flesch_reading_ease(line)
        fre = textstat.flesch_reading_ease(line)
        worksheet.write(row,1,fre)
        #print "smog_index = ",textstat.smog_index(line)
        smog = textstat.smog_index(line)
        #print "flesch_kincaid_grade = ",textstat.flesch_kincaid_grade(line)
        fkg = textstat.flesch_kincaid_grade(line)
        worksheet.write(row,2,fkg)
        #print "dale_chall_readability_score = ", textstat.dale_chall_readability_score(line)
        dcr = textstat.dale_chall_readability_score(line)
        worksheet.write(row,3,dcr)
        #print "gunning_fog = ",textstat.gunning_fog(line)
        gf = textstat.gunning_fog(line)
        worksheet.write(row,4,gf)
        row+=1
 book.save('Readability_Scores.xls')
#cProfile.run('f()')

if __name__ == "__main__":
    app.run(host='9.199.145.51',port=9090,debug=True)

@app.route('/login')
def login():
    print("im heree1e")
    print("im hereee")
    return render_template('login.html')