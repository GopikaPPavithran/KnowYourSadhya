from app import db

class item(db.Model):
    id=db.Column('id',db.Integer,primary_key=True)
    item=db.Column(db.String(20))
    desc=db.Column(db.String())
    url=db.Column(db.String())
    def __init__(self,item,desc,url):
        self.item=item
        self.desc=desc
        self.url=url

class districts(db.Model):
    id=db.Column('id',db.Integer,primary_key=True)
    dname=db.Column(db.String(20))
    itemid=db.Column(db.Integer,db.ForeignKey(item.id))
    def __init__(self,dname,itemid):
        self.dname=dname
        self.itemid=itemid
