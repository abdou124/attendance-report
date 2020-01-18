from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from Trainer import extractNumber
import csv
import glob,os
from django.conf import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from xlsxwriter.workbook import Workbook


fromaddr = "example@gmail.com"
toaddrs = "touazi.abdelhak@gmail.com"
psw = ""


def home(request):


    return render(request,"myapp/myapp.html")


def Form(request):
    return render(request,"myapp/form.html")

def list_Student(request):


    return render(request,"myapp/student.html")

def Upload(request):
    #print()
    files = glob.glob(settings.MEDIA_ROOT+"//*")
    for f in files:
     os.remove(f)
    for count,x in enumerate(request.FILES.getlist("files")):
        def process(f):
            with open(settings.MEDIA_ROOT+"//chat_"+str(count)+".txt", "wb+") as destination:
                  for chunk in f.chunks():
                      destination.write(chunk)
        process(x)
    sessions=extractNumber.extract(settings.MEDIA_ROOT)

    generate_report(sessions,request.POST['class'])
    send_email(fromaddr,psw,request.POST['email'],request.POST['nombre'])
    return HttpResponse("Files Uploaded")


def generate_report(sessions,tt):
    arr = ["student Name"]
    arr.extend(list(sessions.keys()))
    fil= open('attendence_report.csv', 'w')
    filewriter = csv.writer(fil, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(arr)
    all_student=Student.objects.all().filter(batch__batch__contains=tt)
    student_details=[]
    for student in all_student:
        student_details=[student.name]
        for k,v in sessions.items():
            if [student.phone] in v:
                student_details.append("present")
            else :
                student_details.append("absent")
        filewriter.writerow(student_details)
    fil.close()

    workbook = Workbook(settings.MEDIA_ROOT+"//attendence_report"+ '.xlsx')
    worksheet = workbook.add_worksheet()
    success = workbook.add_format({'bold': True, 'font_color': 'green'})
    failed = workbook.add_format({'bold': True, 'font_color': 'red'})
    with open(settings.MEDIA_ROOT+"//attendence_report.csv", 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                 if   (col=="absent"):
                      worksheet.write(r//2, c, col,failed)
                 elif  (col=="present"):
                      worksheet.write(r//2, c, col,success)
                 else:
                     worksheet.write(r//2, c, col)
    workbook.close()


def send_email(fromaddr,psw,toaddr,nm):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Attendance report"
    body = "Hi "+nm+" please find in attachement the requested report "
    msg.attach(MIMEText(body, 'plain'))
    filename = "attendence_report.xlsx"
    attachment = open(settings.MEDIA_ROOT+"//attendence_report.xlsx", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, psw)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
    attachment.close()
