__author__ = 'Ran'
from app import db
from app.DB_account import Account
from flask_login import current_user

def purchase():
    money = int(Account.query.filter_by(id = current_user.id).first().money) - 5
    db.session.query(Account).filter(Account.id == current_user.id).update({Account.money:int(money)})
    db.session.commit()