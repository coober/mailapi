from flask import request
from web import app
from web.sender import mailsender

@app.route('/mail', methods = ['POST'])
def mail():
    assert request.path =='/mail'
    assert request.method =='POST'
    
    content = request.form.getlist('content')
    g_content = content[0]  
    to = request.form.getlist('tos')
    g_to = []
    g_to.extend(to[0].split(','))
    subject = request.form.getlist('subject')
    g_subject = subject[0]
    try:
        a = mailsender(g_to, g_subject, g_content)
        a.sendmail()
	return 'True'
    except Exception, e:
        print str(e)
        return 'False'
    
