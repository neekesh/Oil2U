
from .models import Invoice, Order
from datetime import date
from datetime import datetime, timedelta
import firebase_admin
from firebase_admin import credentials, auth
import os

cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred,
                              {
                                  'databaseURL': 'https://oil2u-c25aa-default-rtdb.asia-southeast1.firebasedatabase.app/'
                              })

from firebase_admin import db

def change_fb_data(email):
    ref = db.reference("/notifications")
    data ={
        "email" : email,
        "show": True
    }
    ref.set(data)
    


def add_date(date, days ):
    date = datetime.strptime(date, '%Y-%m-%d')

    # Add 5 days to the start_date
    modified_start_date = date + timedelta(days=days)
    return modified_start_date.strftime('%Y-%m-%d')


def ScheduledDelivery():
    orders = Order.objects.filter(next_date = date.today())
    for order in orders:
        invoice = Invoice(
            order = order,
            user= order.user,
            payment_type = 'scheduled'
        )
        invoice.save()
        order.status= "pending"
        match order.frequency:
            case "weekly":
                order.next_date= add_date(order.next_date, 7)

            case "fortnight":
                order.next_date= add_date(order.next_date, 15)

        order.save()
    print("scheduled delivery completed")


