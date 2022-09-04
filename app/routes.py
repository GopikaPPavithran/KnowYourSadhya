from flask import Flask, request, flash, url_for, redirect, render_template 
from app import app
from app import db

@app.route('/',methods = ['GET', 'POST'])
def home():
    return render_template('map.html')