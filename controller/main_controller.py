import os
import shutil
from flask import Flask, render_template, url_for, request, redirect, flash, abort
from flask_login import login_required, login_user
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from cfg import app, manager, db
from models.LoginForm import LoginForm
from models.brief import User, Brief
from flask import send_from_directory


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        print(request.form)
        text1 = request.form['text1']
        text2 = request.form['text2']
        text3 = request.form['text3']
        text4 = request.form['text4']
        text5 = request.form['text5']
        text6 = request.form['text6']
        text9 = request.form['text9']
        text10 = request.form['text10']
        text11 = request.form['text11']
        text12 = request.form['text12']
        text14 = request.form['text14']
        text16 = request.form['text16']
        text17 = request.form['text17']
        text18 = request.form['text18']
        text21 = request.form['text21']
        text23 = request.form['text23']
        text24 = request.form['text24']
        text25 = request.form['text25']
        text26 = request.form['text26']
        prod = False
        if 'prod' in request.form:
            prod = True
        posl = False
        if 'posl' in request.form:
            posl = True
        rek = False
        if 'rek' in request.form:
            rek = True
        pokr = False
        if 'pokr' in request.form:
            pokr = True
        seo = False
        if 'seo' in request.form:
            seo = True
        rebr = False
        if 'rebr' in request.form:
            rebr = True

        korp = False
        if 'korp' in request.form:
            korp = True
        yask = False
        if 'yask' in request.form:
            yask = True
        poz = False
        if 'poz' in request.form:
            poz = True
        zobr = False
        if 'zobr' in request.form:
            zobr = True
        dinam = False
        if 'dinam' in request.form:
            dinam = True
        stat = False
        if 'stat' in request.form:
            stat = True
        mini = False
        if 'mini' in request.form:
            mini = True
        funk = False
        if 'funk' in request.form:
            funk = True
        feedb = False
        if 'feedb' in request.form:
            feedb = True
        pop = False
        if 'pop' in request.form:
            pop = True
        nov = False
        if 'nov' in request.form:
            nov = True
        faq = False
        if 'faq' in request.form:
            faq = True
        analit = False
        if 'analit' in request.form:
            analit = True
        crm = False
        if 'crm' in request.form:
            crm = True
        mon = False
        if 'mon' in request.form:
            mon = True
        napov = False
        if request.form['napov'] == 'True':
            napov = True
        dom = False
        if request.form['dom'] == 'True':
            dom = True

        file = ''
        if request.files['image'].filename:
            file = request.files['image']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file = filename
        try:
            db.session.add(Brief(text1=text1, text2=text2, text3=text3, text4=text4, text5=text5, prod=prod, posl=posl,
                                 rek=rek, pokr=pokr, seo=seo, rebr=rebr, text9=text9, text10=text10, text11=text11,
                                 text12=text12,
                                 brand=file, text14=text14, korp=korp, yask=yask, poz=poz, zobr=zobr,
                                 dinam=dinam,
                                 stat=stat, mini=mini, funk=funk, text16=text16, text17=text17, text18=text18,
                                 feedb=feedb,
                                 pop=pop, nov=nov, faq=faq, analit=analit, crm=crm, mon=mon, napov=napov,
                                 text21=text21, dom=dom, text23=text23, text24=text24, text25=text25,
                                 text26=text26))
            db.session.commit()
        except:
            return render_template("index.html")
        return redirect('/ty')


@app.route('/ty')
def ty():
    return render_template("success.html")


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        if form.login.data and form.password.data:
            user = User.query.filter_by(login=form.login.data).first()

            if user and user.password == str(form.password.data):
                login_user(user)

                next_page = request.args.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('/')
            else:
                flash('Помилка у введених даних')
                return render_template('login.html', form=form)
        else:
            flash('Поля повинні бути заповненими')
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)


@app.route('/admin')
@login_required
def admin_page():
    brifs = Brief.query.all()
    return render_template("brief.html", count=0, brifs=brifs)


@app.route('/brief/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id=0):
    brief = Brief.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('update.html', brief=brief)
    else:
        text1 = request.form['text1']
        text2 = request.form['text2']
        text3 = request.form['text3']
        text4 = request.form['text4']
        text5 = request.form['text5']
        text6 = request.form['text6']
        text9 = request.form['text9']
        text10 = request.form['text10']
        text11 = request.form['text11']
        text12 = request.form['text12']
        text14 = request.form['text14']
        text16 = request.form['text16']
        text17 = request.form['text17']
        text18 = request.form['text18']
        text21 = request.form['text21']
        text23 = request.form['text23']
        text24 = request.form['text24']
        text25 = request.form['text25']
        text26 = request.form['text26']
        prod = False
        if 'prod' in request.form:
            prod = True
        posl = False
        if 'posl' in request.form:
            posl = True
        rek = False
        if 'rek' in request.form:
            rek = True
        pokr = False
        if 'pokr' in request.form:
            pokr = True
        seo = False
        if 'seo' in request.form:
            seo = True
        rebr = False
        if 'rebr' in request.form:
            rebr = True
        korp = False
        if 'korp' in request.form:
            korp = True
        yask = False
        if 'yask' in request.form:
            yask = True
        poz = False
        if 'poz' in request.form:
            poz = True
        zobr = False
        if 'zobr' in request.form:
            zobr = True
        dinam = False
        if 'dinam' in request.form:
            dinam = True
        stat = False
        if 'stat' in request.form:
            stat = True
        mini = False
        if 'mini' in request.form:
            mini = True
        funk = False
        if 'funk' in request.form:
            funk = True
        feedb = False
        if 'feedb' in request.form:
            feedb = True
        pop = False
        if 'pop' in request.form:
            pop = True
        nov = False
        if 'nov' in request.form:
            nov = True
        faq = False
        if 'faq' in request.form:
            faq = True
        analit = False
        if 'analit' in request.form:
            analit = True
        crm = False
        if 'crm' in request.form:
            crm = True
        mon = False
        if 'mon' in request.form:
            mon = True
        napov = False
        if request.form['napov'] == 'True':
            napov = True
        dom = False
        if request.form['dom'] == 'True':
            dom = True

        file = ''
        if request.files:
            if request.files['image'].filename:
                file = request.files['image']
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                file = filename
        else:
            file = brief.brand
        try:
            brief.text1 = text1
            brief.text2 = text2
            brief.text3 = text3
            brief.text4 = text4
            brief.text5 = text5
            brief.prod = prod
            brief.posl = posl
            brief.rek = rek
            brief.pokr = pokr
            brief.seo = seo
            brief.rebr = rebr
            brief.text9 = text9
            brief.text10 = text10
            brief.text11 = text11
            brief.text12 = text12
            brief.brand = file
            brief.text14 = text14
            brief.korp = korp
            brief.yask = yask
            brief.poz = poz
            brief.zobr = zobr
            brief.dinam = dinam
            brief.stat = stat
            brief.mini = mini
            brief.funk = funk
            brief.text16 = text16
            brief.text17 = text17
            brief.text18 = text18
            brief.feedb = feedb
            brief.pop = pop
            brief.nov = nov
            brief.faq = faq
            brief.analit = analit
            brief.crm = crm
            brief.mon = mon
            brief.napov = napov
            brief.text21 = text21
            brief.dom = dom
            brief.text23 = text23
            brief.text24 = text24
            brief.text25 = text25
            brief.text26 = text26
            db.session.commit()
        except:
             return render_template("update.html")
        return redirect('/admin')


@app.route('/brief/<int:id>/send')
@login_required
def send(id=0):
    brief = Brief.query.filter_by(id=id).first()
    return send_from_directory(app.config["UPLOAD_FOLDER"], brief.brand)


@app.route('/delete/<int:id>')
@login_required
def delete(id=0):
    brief = Brief.query.get(id)
    try:
        db.session.delete(brief)
        db.session.commit()
        os.remove(os.path.join('static', 'files', brief.brand))
    except:
        return redirect('/brief/' + str(brief.id))
    return redirect('/admin')

@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
