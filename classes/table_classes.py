#from tests import db.  Need to add on delete set nulls. 
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True, nullable=False)
	password = db.Column(db.String(100), unique=False, nullable=False)

	def __repr__(self):
		return '<username = %r, password= %r>' % (self.username, self.password)

class households(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(500), unique=True, nullable=False)

	def __repr__(self):
		return '<id = %r, name= %r>' % (self.id, self.name)

class fee_structure(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(500), unique=True, nullable=False)
	frequency=db.Column(db.String(100), unique=False, nullable=False)
	collection=db.Column(db.String(100), unique=False, nullable=False)
	structure=db.Column(db.String(100), unique=False, nullable=False)
	valuation_method=db.Column(db.String(100), unique=False, nullable=False)

	def __repr__(self):
		return '<id = %r, name= %r>' % (self.id, self.name)

class accounts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	account_number=db.Column(db.Integer, unique=True, nullable=False)
	name = db.Column(db.String(500), unique=False, nullable=True)
	custodian = db.Column(db.String(100), unique=False, nullable=True)
	opening_date = db.Column(db.Date(), unique=False, nullable=True)
	balance=db.Column(db.Numeric(), unique=False, nullable=True)
	household_id= db.Column(db.Integer, db.ForeignKey('households.id', ondelete='SET NULL'), nullable=True)
	fee_id= db.Column(db.Integer, db.ForeignKey('fee_structure.id', ondelete='SET NULL'), nullable=True)


	def __repr__(self):
		return '<id = %r, name = %r, account_number= %r>' % (self.id, self.name, self.account_number)