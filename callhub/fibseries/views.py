from django.shortcuts import render
import timeit
from rest_framework import status
from rest_framework.response import Response
import json
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(["POST"])
def fib(num):


	s = 1
	s1 = 1
	try:
		start = timeit.timeit()
		n = json.loads(num.body)
		for i in range(n):
			if i == 0:
				c = s
			elif i == 1:
				c = s1
			else:
				c = s1 + s
				s = s1
				s1 = c
		end = timeit.timeit()
		total_time = end - start
		return Response({'Nth number':c,'Time':total_time})
	except Exception as x:
		return Response('Please enter positive number')
	




