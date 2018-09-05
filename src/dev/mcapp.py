#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#
#app = Flask(__name__)
#
#@app.route("/")
#def home():
#    return "Hi!"
#
#@app.route('/welcome_series')
#def welcome_series_trigger():
#    pass
#
#class Config:
#    POSTGRES = {'user': 'acarrasco',
#                'pw': 'EmbraceHorseTuba2019()',
#                'db': 'dev',
#                'host': 'redshift.switchjoin.orgs.civis.io',
#                'port': '5432',
#            }
#    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
#    SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#app.config.from_object(Config)
#db = SQLAlchemy(app)
#print(db.select('a'))
#
#import sqlalchemy as sa
#import sqlalchemy_redshift
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Column, Integer, String, create_engine
#from sqlalchemy.orm import sessionmaker
#
POSTGRES = {'user': 'acarrasco',
            'pw': 'EmbraceHorseTuba2019()',
            'db': 'dev',
            'host': 'redshift.switchjoin.orgs.civis.io',
            'port': '5432',
        }

SQLALCHEMY_DATABASE_URI = 'redshift://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
print(SQLALCHEMY_DATABASE_URI)
#SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)#, connect_args={'sslmode' : 'prefer'})
#Base = declarative_base()
#
#class User(Base):
#     __tablename__ = 'public.users'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#
#     def __repr__(self):
#        return "<User(name='%s')>" % (self.name)
#
#user = User(id=1, name='a')
#Session = sessionmaker(bind=engine)
#session = Session()
#Base.metadata.create_all(engine)
#session.flush()
#session.commit()
#session.close()
#session.add(user)
#our_user = session.query(User).all()
#print(our_user)
#session.flush()
#session.commit()
#session.close()