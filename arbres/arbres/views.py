from django.shortcuts import render
from django import forms
from django.utils.translation import ugettext as _
from bs4 import BeautifulSoup
from django.shortcuts import redirect
import http.cookies
import urllib.request
import requests
import mysql.connector
import json

def welcome_page(request):
	return render(request, 'welcome_page.html')

def catalog(request):
	cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='arbres')
	cursor = cnx.cursor()
	text = '''SELECT * FROM tree'''
	cursor.execute(text)
	trees_row = cursor.fetchall()
	trees = []
	for i in trees_row:
		row = {}
		row['name'] = i[1]
		row['type'] = i[2]
		text = '''SELECT icon FROM types
				  WHERE id = {}'''.format(str(row['type']))
		cursor.execute(text)
		row['type'] = cursor.fetchall()[0][0]
		row['height'] = str(i[3])
		row['photo'] = str(i[4])
		row['place'] = str(i[5])
		trees.append(row)
	cnx.close()
	print(trees[0]['photo'])
	return render(request, 'catalog.html', {'trees': trees})

def arbre(name, request):
	return()	