from flask import Flask, request, flash, url_for, redirect, render_template 
from app import app
from app import db
from app.database import item,districts

def additems(iname,desc,url):
    items=item.query.all()
    for i in items:
        if i.item==iname:
            print(i.desc)
            i.desc=desc
            i.url=url
            # db.session.add(i)
            db.session.commit()
            return
    it=item(iname,desc,url)
    db.session.add(it)
    db.session.commit()

def adddistrict(dst,itmid):
    # i=item.query.filter_by(id=itm).first()
    d=districts(dst,itmid)
    db.session.add(d)
    db.session.commit()

def cleardistrict(cname):
    d=districts.query.filter_by(dname=cname).all()
    for x in d:
        print(x)
        db.session.delete(x)
    db.session.commit()
    
@app.route('/additem',methods = ['GET','POST'])
def addlist():
    if request.method=='POST':
        itemname=request.form.get('itemname')
        desc=request.form.get('desc')
        url=request.form.get('url')
        additems(itemname,desc,url)
        items=item.query.all()
        return render_template('listitem.html',items=items)
    return render_template('listitem.html')

@app.route('/adddistrict',methods=['POST','GET'])
def adddist(): 
    # cleardistrict("Alp")  
    items=item.query.all()
    if request.method=='POST':
        cname=request.form.get('city')
        print("City "+ str(cname))
        selitems=request.form.getlist("sel_items")
        for s in selitems:
            d=districts.query.filter_by(dname=cname,itemid=s).first()
            if d is None:
                adddistrict(cname,s)
        return redirect(url_for('home'))
    return render_template('listdist.html',dist=dis,items=items)


# real stuff begins here

dis=['Tvm','Klm','Ptn','Alp','Idk','Ktm','Ekm','Tsr','Pkd','Mlp','Kzd','Ksd','Wnd','Knr']
@app.route('/',methods = ['GET', 'POST'])
def home():
    if request.method=='POST':
        return redirect(url_for("list"))
    return render_template('map.html')

def getdname(name):
    if name=="Tvm":
        return "Trivandrum"
    elif name=="Klm":
        return "Kollam"
    elif name=="Ptn":
        return "Pathanamthitta"
    elif name=="Alp":
        return "Alappuzha"
    elif name=="Idk":
        return "Idukki"
    elif name=="Ekm":
        return "Ernakulam"
    elif name=="Tsr":
        return "Trissur"
    elif name=="Pkd":
        return "Palakkad"
    elif name=="Mlp":
        return "Malappuram"
    elif name=="Ksd":
        return "Kasargode"
    elif name=="Kzd":
        return "Kozhikode"
    elif name=="Wnd":
        return "Wayanad"
    elif name=="Knr":
        return "Kannur"
    elif name=="Ktm":
        return "Kottayam"
@app.route('/list',methods=['GET','POST'])
def list():
    items=[]
    dst=""
    dstn=""
    if request.method=='POST':
        dst=request.form.get('dis')
        itmid=districts.query.filter_by(dname=dst)
        # items=[]
        dstn=getdname(dst)
        for i in itmid:
            iid=item.query.filter_by(id=i.itemid).first()
            print(iid)
            items.append(iid)
        return render_template('pg2.html',items=items,dst=dstn)
    return render_template('pg2.html',items=items,dst=dstn)