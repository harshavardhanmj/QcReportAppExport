import datetime
import xlwt
from datetime import timedelta
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.db.models import Q
from DisStatus.models import DailyStatusQC, DailyStatusAuto, ProjectQC, ProjectAuto, ProjectPq, DailyStatusPQ, UpcomingProj, graphData
from DisStatus.forms import SearchForm
import requests
from requests.auth import HTTPBasicAuth
import json
from dateutil import parser
from maindashboard.utils import render_to_pdf

class StatusView(ListView):
	template_name = "index.html"
	form_class = SearchForm
	
	def get_queryset(self):
		form = self.form_class(self.request.GET)
		if form.is_valid():
			if form.cleaned_data['date'] != None:
				return DailyStatusQC.objects.filter(LogDate=form.cleaned_data['date'])
			else:
				currentDate = datetime.datetime.now().date()
				return DailyStatusQC.objects.filter(LogDate=currentDate)
	
	def get_context_data(self, **kwargs):
		context = super(StatusView, self).get_context_data(**kwargs)
		#currentDate = datetime.datetime.now().date()
		form = self.form_class(self.request.GET)
		if form.is_valid():
			if form.cleaned_data['date'] != None:
				DisplayDate = form.cleaned_data['date']
				context['auto_list'] = DailyStatusAuto.objects.filter(LogDate=form.cleaned_data['date'])
				context['pq_list'] = DailyStatusPQ.objects.filter(LogDate=form.cleaned_data['date'])
				projectQcList = ProjectQC.objects.all().values('ProductName')
				statusQcList = DailyStatusQC.objects.filter(LogDate=form.cleaned_data['date']).values('ProductName')
				itr1 = 0
				itr2 = 0
				temp_dict = {}
				while itr1 < projectQcList.count():
					if projectQcList[itr1] not in statusQcList:
						temp_dict[itr2] = projectQcList[itr1]['ProductName']
						itr2 = itr2 + 1
					itr1 = itr1 + 1
				dateItr = 1
				itr1 = 0
				ds = []
				#print(temp_dict)
				while itr1 < itr2:
					#print(itr1)
					dateItr = 1
					#print(dateItr)
					while dateItr < 4:
						d = DisplayDate - timedelta(days=dateItr)
						qs = DailyStatusQC.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
						#print(qs)
						if qs:
							#print("exist")
							ds.append(DailyStatusQC.objects.get(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])))
							#print(ds)
							break
						dateItr = dateItr + 1
					itr1 = itr1 + 1
				context['object_list1'] = ds
				projectQcList = ProjectPq.objects.all().values('ProductName')
				statusQcList = DailyStatusPQ.objects.filter(LogDate=form.cleaned_data['date']).values('ProductName')
				itr1 = 0
				itr2 = 0
				temp_dict = {}
				while itr1 < projectQcList.count():
					if projectQcList[itr1] not in statusQcList:
						temp_dict[itr2] = projectQcList[itr1]['ProductName']
						itr2 = itr2 + 1
					itr1 = itr1 + 1
				dateItr = 1
				itr1 = 0
				ds = []
				while itr1 < itr2:
					#print(itr1)
					dateItr = 1
					while dateItr < 4:
						d = DisplayDate - timedelta(days=dateItr)
						qs = DailyStatusPQ.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
						#print(qs)
						if qs:
							#print("exist")
							ds.append(DailyStatusPQ.objects.get(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])))
							#print(ds)
							break
						dateItr = dateItr + 1
					itr1 = itr1 + 1
				context['pq_list1'] = ds
				projectQcList = ProjectAuto.objects.all().values('ProductName')
				statusQcList = DailyStatusAuto.objects.filter(LogDate=form.cleaned_data['date']).values('ProductName')
				itr1 = 0
				itr2 = 0
				temp_dict = {}
				while itr1 < projectQcList.count():
					if projectQcList[itr1] not in statusQcList:
						temp_dict[itr2] = projectQcList[itr1]['ProductName']
						itr2 = itr2 + 1
					itr1 = itr1 + 1
				dateItr = 1
				itr1 = 0
				ds = []
				while itr1 < itr2:
					#print(itr1)
					dateItr = 1
					while dateItr < 4:
						d = DisplayDate - timedelta(days=dateItr)
						qs = DailyStatusAuto.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
						#print(qs)
						if qs:
							#print("exist")
							ds.append(DailyStatusAuto.objects.get(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])))
							#print(ds)
							break
						dateItr = dateItr + 1
					itr1 = itr1 + 1
				context['auto_list1'] = ds
			else:
				currentDate = datetime.datetime.now().date()
				DisplayDate = currentDate
				context['auto_list'] = DailyStatusAuto.objects.filter(LogDate=currentDate)
				context['pq_list'] = DailyStatusPQ.objects.filter(LogDate=currentDate)
				projectQcList = ProjectQC.objects.all().values('ProductName')
				statusQcList = DailyStatusQC.objects.filter(LogDate=currentDate).values('ProductName')
				itr1 = 0
				itr2 = 0
				temp_dict = {}
				while itr1 < projectQcList.count():
					if projectQcList[itr1] not in statusQcList:
						temp_dict[itr2] = projectQcList[itr1]['ProductName']
						itr2 = itr2 + 1
					itr1 = itr1 + 1
				dateItr = 1
				itr1 = 0
				ds = []
				while itr1 < itr2:
					#print(itr1)
					dateItr = 1
					while dateItr < 4:
						d = DisplayDate - timedelta(days=dateItr)
						qs = DailyStatusQC.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
						#print(qs)
						if qs:
							#print("exist")
							ds.append(DailyStatusQC.objects.get(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])))
							#print(ds)
							break
						dateItr = dateItr + 1
					itr1 = itr1 + 1
				context['object_list1'] = ds
				projectQcList = ProjectPq.objects.all().values('ProductName')
				statusQcList = DailyStatusPQ.objects.filter(LogDate=currentDate).values('ProductName')
				itr1 = 0
				itr2 = 0
				temp_dict = {}
				while itr1 < projectQcList.count():
					if projectQcList[itr1] not in statusQcList:
						temp_dict[itr2] = projectQcList[itr1]['ProductName']
						itr2 = itr2 + 1
					itr1 = itr1 + 1
				dateItr = 1
				itr1 = 0
				ds = []
				while itr1 < itr2:
					#print(itr1)
					dateItr = 1
					while dateItr < 4:
						d = DisplayDate - timedelta(days=dateItr)
						qs = DailyStatusPQ.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
						#print(qs)
						if qs:
							#print("exist")
							ds.append(DailyStatusPQ.objects.get(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])))
							#print(ds)
							break
						dateItr = dateItr + 1
					itr1 = itr1 + 1
				context['pq_list1'] = ds
				projectQcList = ProjectAuto.objects.all().values('ProductName')
				statusQcList = DailyStatusAuto.objects.filter(LogDate=currentDate).values('ProductName')
				itr1 = 0
				itr2 = 0
				temp_dict = {}
				while itr1 < projectQcList.count():
					if projectQcList[itr1] not in statusQcList:
						temp_dict[itr2] = projectQcList[itr1]['ProductName']
						itr2 = itr2 + 1
					itr1 = itr1 + 1
				dateItr = 1
				itr1 = 0
				ds = []
				while itr1 < itr2:
					#print(itr1)
					dateItr = 1
					while dateItr < 4:
						d = DisplayDate - timedelta(days=dateItr)
						qs = DailyStatusAuto.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
						#print(qs)
						if qs:
							#print("exist")
							ds.append(DailyStatusAuto.objects.get(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])))
							#print(ds)
							break
						dateItr = dateItr + 1
					itr1 = itr1 + 1
				context['auto_list1'] = ds
		context['qcproject_list'] = ProjectQC.objects.all()
		context['autoproject_list'] = ProjectAuto.objects.all()
		context['pqproject_list'] = ProjectPq.objects.all()
		context['DisplayDate'] = DisplayDate
		context['upcoming'] = UpcomingProj.objects.all()
		return context

		
		
class GeneratePdf(View):
	def get(self, request, *args, **kwargs):
		currentPath = self.request.get_full_path()
		temp = currentPath.split("/")
		searchDate = temp[2].replace("%20", " ")
		searchDate = searchDate.replace(",", "")
		print(searchDate)
		searchDateObj = parser.parse(searchDate)
		#searchDateObj = datetime.datetime.strptime(searchDate, '%b %d %Y')
		#currentDate = datetime.datetime.now().date()
		currentDate = searchDateObj
		DisplayDate = searchDateObj
		auto_list = DailyStatusAuto.objects.filter(LogDate=currentDate)
		pq_list = DailyStatusPQ.objects.filter(LogDate=currentDate)
		object_list = DailyStatusQC.objects.filter(LogDate=currentDate)
		projectQcList = ProjectQC.objects.all().values('ProductName')
		statusQcList = DailyStatusQC.objects.filter(LogDate=currentDate).values('ProductName')
		itr1 = 0
		itr2 = 0
		temp_dict = {}
		while itr1 < projectQcList.count():
			if projectQcList[itr1] not in statusQcList:
				temp_dict[itr2] = projectQcList[itr1]['ProductName']
				itr2 = itr2 + 1
			itr1 = itr1 + 1
		dateItr = 1
		itr1 = 0
		ds = []
		while itr1 < itr2:
			#print(itr1)
			dateItr = 1
			while dateItr < 4:
				d = DisplayDate - timedelta(days=dateItr)
				qs = DailyStatusQC.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
				#print(qs)
				if qs:
					#print("exist")
					ds.append(DailyStatusQC.objects.get(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])))
					#print(ds)
					break
				dateItr = dateItr + 1
			itr1 = itr1 + 1
		object_list1 = ds
		projectQcList = ProjectPq.objects.all().values('ProductName')
		statusQcList = DailyStatusPQ.objects.filter(LogDate=currentDate).values('ProductName')
		itr1 = 0
		itr2 = 0
		temp_dict = {}
		while itr1 < projectQcList.count():
			if projectQcList[itr1] not in statusQcList:
				temp_dict[itr2] = projectQcList[itr1]['ProductName']
				itr2 = itr2 + 1
			itr1 = itr1 + 1
		dateItr = 1
		itr1 = 0
		ds = []
		while itr1 < itr2:
			#print(itr1)
			dateItr = 1
			while dateItr < 4:
				d = DisplayDate - timedelta(days=dateItr)
				qs = DailyStatusPQ.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
				#print(qs)
				if qs:
					#print("exist")
					ds.append(DailyStatusPQ.objects.get(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])))
					#print(ds)
					break
				dateItr = dateItr + 1
			itr1 = itr1 + 1
		pq_list1 = ds
		projectQcList = ProjectAuto.objects.all().values('ProductName')
		statusQcList = DailyStatusAuto.objects.filter(LogDate=currentDate).values('ProductName')
		itr1 = 0
		itr2 = 0
		temp_dict = {}
		while itr1 < projectQcList.count():
			if projectQcList[itr1] not in statusQcList:
				temp_dict[itr2] = projectQcList[itr1]['ProductName']
				itr2 = itr2 + 1
			itr1 = itr1 + 1
		dateItr = 1
		itr1 = 0
		ds = []
		while itr1 < itr2:
			#print(itr1)
			dateItr = 1
			while dateItr < 4:
				d = DisplayDate - timedelta(days=dateItr)
				qs = DailyStatusAuto.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
				#print(qs)
				if qs:
					#print("exist")
					ds.append(DailyStatusAuto.objects.get(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])))
					#print(ds)
					break
				dateItr = dateItr + 1
			itr1 = itr1 + 1
		auto_list1 = ds
		qcproject_list = ProjectQC.objects.all()
		autoproject_list = ProjectAuto.objects.all()
		pqproject_list = ProjectPq.objects.all()
		DisplayDate = DisplayDate
		upcoming = UpcomingProj.objects.all()
		data = {
		'auto_list' : auto_list,
		'pq_list' : pq_list,
		'object_list' : object_list,
		'object_list1' : object_list1,
		'pq_list1' : pq_list1,
		'auto_list1' : auto_list1,
		'qcproject_list' : qcproject_list,
		'autoproject_list' : autoproject_list,
		'pqproject_list' : pqproject_list,
		'DisplayDate' : searchDate
		}
		pdf = render_to_pdf('indexpdf.html', data)
		return HttpResponse(pdf, content_type='application/pdf')
		 
class DetailView(TemplateView):
	template_name = "details.html"
	
	def get_context_data(self, **kwargs):
		currentPath = self.request.get_full_path()
		temp = currentPath.split("/")
		proj = temp[2].replace("%20", " ")
		context = super(DetailView, self).get_context_data(**kwargs)
		context["project"] = proj
		totProj = proj.split(",")
		itr1 = 0
		issueCount = 0
		openIssues = 0
		resolvedIssues = 0
		closedIssues = 0
		defferedIssues = 0
		while itr1 < len(totProj):
			openMinorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", -) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status in (New, Open, "In Progress") AND priority = Minor ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			openMinorResponse = requests.get(openMinorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = openMinorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["openMinor"] = issueCount
		except:
			context["openMinor"] = "0"
		openIssues = openIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			openMajorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", -) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status in (New, Open, "In Progress") AND priority = Major ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			openMajorResponse = requests.get(openMajorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = openMajorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["openMajor"] = issueCount
		except:
			context["openMajor"] = "0"
		openIssues = openIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			openCriticalUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", -) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status in (New, Open, "In Progress") AND priority = Critical ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			openCriticalResponse = requests.get(openCriticalUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = openCriticalResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["openCritical"] = issueCount
		except:
			context["openCritical"] = "0"
		openIssues = openIssues + issueCount
		context["openIssues"] = openIssues
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			resolvedMinorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Verified, Fixed, "Won't Fix", "Cannot Reproduce") AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status = Resolved AND priority = Minor ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			resolvedMinorResponse = requests.get(resolvedMinorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = resolvedMinorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["resolvedMinor"] = issueCount
		except:
			context["resolvedMinor"] = "0"
		resolvedIssues = resolvedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			resolvedMajorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Verified, Fixed, "Won't Fix", "Cannot Reproduce") AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status = Resolved AND priority = Major ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			resolvedMajorResponse = requests.get(resolvedMajorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = resolvedMajorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["resolvedMajor"] = issueCount
		except:
			context["resolvedMajor"] = "0"
		resolvedIssues = resolvedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			resolvedCriticalUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Verified, Fixed, "Won't Fix", "Cannot Reproduce") AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status = Resolved AND priority = Critical ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			resolvedCriticalResponse = requests.get(resolvedCriticalUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = resolvedCriticalResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["resolvedCritical"] = issueCount
		except:
			context["resolvedCritical"] = "0"
		resolvedIssues = resolvedIssues + issueCount
		context["resolvedIssues"] = resolvedIssues
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			closedMinorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Re-Opened, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status = Closed AND priority = Minor ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			closedMinorResponse = requests.get(closedMinorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = closedMinorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["closedMinor"] = issueCount
			closed1 = issueCount
		except:
			context["closedMinor"] = "0"
			closed1 = "0"
		closedIssues = closedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			closedMajorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Re-Opened, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status = Closed AND priority = Major ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			closedMajorResponse = requests.get(closedMajorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = closedMajorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["closedMajor"] = issueCount
			closed2 = issueCount
		except:
			context["closedMajor"] = "0"
			closed2 = "0"
		closedIssues = closedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			closedCriticalUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Re-Opened, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND status = Closed AND priority = Critical ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			closedCriticalResponse = requests.get(closedCriticalUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = closedCriticalResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["closedCritical"] = issueCount
			closed3 = issueCount
		except:
			context["closedCritical"] = "0"
			closed3 = "0"
		closedIssues = closedIssues + issueCount
		context["closedIssues"] = closedIssues
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			deferredMinorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND priority = Minor ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			deferredMinorResponse = requests.get(deferredMinorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = deferredMinorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["deferredMinor"] = issueCount
		except:
			context["deferredMinor"] = "0"
		defferedIssues = defferedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			deferredMajorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND priority = Major ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			deferredMajorResponse = requests.get(deferredMajorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = deferredMajorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["deferredMajor"] = issueCount
		except:
			context["deferredMajor"] = "0"
		defferedIssues = defferedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			deferredCriticalUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin in (Automation, Testing) AND priority = Critical ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			deferredCriticalResponse = requests.get(deferredCriticalUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = deferredCriticalResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["deferredCritical"] = issueCount
		except:
			context["deferredCritical"] = "0"
		defferedIssues = defferedIssues + issueCount
		context["defferedIssues"] = defferedIssues
		if datetime.date.today().weekday() == 4:
			year = datetime.date.today().year
			month = (datetime.date.today().month) - 1
			date = datetime.date.today().day
			graphdate = "" + str(year) + ", " + str(month) + ", " + str(date)
			issueClo = int(closed1) + int(closed2) + int(closed3)
			projActive = ProjectQC.objects.get(ProductName__iexact=proj)
			if projActive.ProductStatus == "Active":
				projIssueLoggedObj = DailyStatusQC.objects.filter(ProductName__iexact=proj)
				if projIssueLoggedObj.exists():
					reqObj = projIssueLoggedObj.last()
					try:
						issue = reqObj.IssuesLogged
					except:
						issue = "0"
					if not graphData.objects.filter(Q(projectName_iexact=proj) & Q(plotDate_iexact=graphdate)):
						graphObj = graphData.objects.create(projectName = proj, plotDate = graphdate, issueLogged = issue, issueClosed = issueClo)
					else:
						qs = graphData.objects.get(Q(projectName_iexact=proj) & Q(plotDate_iexact=graphdate))
						if qs.issueClosed != issueClo:
							qs.issueClosed = issueClo
							qs.save();
						if qs.issueLogged != issue:
							qs.issueLogged = issue
							qs.save();
		context["plotDate"] = graphData.objects.filter(projectName__iexact=proj)
		return context

class PqDetailView(TemplateView):
	template_name = "detailspq.html"
	
	def get_context_data(self, **kwargs):
		currentPath = self.request.get_full_path()
		temp = currentPath.split("/")
		proj = temp[2].replace("%20", " ")
		context = super(PqDetailView, self).get_context_data(**kwargs)
		context["project"] = proj
		totProj = proj.split(",")
		itr1 = 0
		issueCount = 0
		openIssues = 0
		resolvedIssues = 0
		closedIssues = 0
		defferedIssues = 0
		while itr1 < len(totProj):
			openMinorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", -) AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation AND status in (New, Open, "In Progress") AND priority = Minor ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			openMinorResponse = requests.get(openMinorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = openMinorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["openMinor"] = issueCount
		except:
			context["openMinor"] = "0"
		openIssues = openIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			openMajorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", -) AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation AND status in (New, Open, "In Progress") AND priority = Major ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			openMajorResponse = requests.get(openMajorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = openMajorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["openMajor"] = issueCount
		except:
			context["openMajor"] = "0"
		openIssues = openIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			openCriticalUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", -) AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation AND status in (New, Open, "In Progress") AND priority = Critical ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			openCriticalResponse = requests.get(openCriticalUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = openCriticalResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["openCritical"] = issueCount
		except:
			context["openCritical"] = "0"
		openIssues = openIssues + issueCount
		context["openIssues"] = openIssues
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			resolvedMinorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Verified, Fixed, "Won't Fix") AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation AND status = Resolved AND priority = Minor ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			resolvedMinorResponse = requests.get(resolvedMinorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = resolvedMinorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["resolvedMinor"] = issueCount
		except:
			context["resolvedMinor"] = "0"
		resolvedIssues = resolvedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			resolvedMajorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Verified, Fixed, "Won't Fix") AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation AND status = Resolved AND priority = Major ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			resolvedMajorResponse = requests.get(resolvedMajorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = resolvedMajorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["resolvedMajor"] = issueCount
		except:
			context["resolvedMajor"] = "0"
		resolvedIssues = resolvedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			resolvedCriticalUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Verified, Fixed, "Won't Fix") AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation AND status = Resolved AND priority = Critical ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			resolvedCriticalResponse = requests.get(resolvedCriticalUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = resolvedCriticalResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["resolvedCritical"] = issueCount
		except:
			context["resolvedCritical"] = "0"
		resolvedIssues = resolvedIssues + issueCount
		context["resolvedIssues"] = resolvedIssues
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			closedMinorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Re-Opened, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation AND status = Closed AND priority = Minor ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			closedMinorResponse = requests.get(closedMinorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = closedMinorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["closedMinor"] = issueCount
		except:
			context["closedMinor"] = "0"
		closedIssues = closedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			closedMajorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Re-Opened, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation AND status = Closed AND priority = Major ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			closedMajorResponse = requests.get(closedMajorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = closedMajorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["closedMajor"] = issueCount
		except:
			context["closedMajor"] = "0"
		closedIssues = closedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			closedCriticalUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Unresolved, Done, Verified, Re-Opened, Triaged, Fixed, "Won't Fix", "Incomplete Info", "Cannot Reproduce", "Not Resolved", Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND Origin = Pre-Validation AND status = Closed AND priority = Critical ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			closedCriticalResponse = requests.get(closedCriticalUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = closedCriticalResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["closedCritical"] = issueCount
		except:
			context["closedCritical"] = "0"
		closedIssues = closedIssues + issueCount
		context["closedIssues"] = closedIssues
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			deferredMinorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation AND priority = Minor ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			deferredMinorResponse = requests.get(deferredMinorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = deferredMinorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["deferredMinor"] = issueCount
		except:
			context["deferredMinor"] = "0"
		defferedIssues = defferedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			deferredMajorUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation AND priority = Major ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			deferredMajorResponse = requests.get(deferredMajorUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = deferredMajorResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["deferredMajor"] = issueCount
		except:
			context["deferredMajor"] = "0"
		defferedIssues = defferedIssues + issueCount
		itr1 = 0
		issueCount = 0
		while itr1 < len(totProj):
			deferredCriticalUrl = '''http://192.168.103.83:8080/rest/api/2/search?jql=project = BUG_CL AND resolution in (Deferred) AND affectedVersion = "''' + totProj[itr1] + '''" AND "Defect Classification" in (Configuration, "Data Migration", Documentation, Functionality, Installation, Integration, Others, Performance, Security, "Test Data", Usability, "User Interface") AND Origin = Pre-Validation AND priority = Critical ORDER BY key DESC'''
			headers = {'Content-Type': 'application/json'}
			deferredCriticalResponse = requests.get(deferredCriticalUrl, headers=headers, auth=HTTPBasicAuth('test.pull.user', 'Password1'))
			geodata1 = deferredCriticalResponse.json()
			try:
				issueCount = issueCount + int(geodata1["total"]);
			except:
				issueCount = 0;
			itr1 = itr1 + 1
		try:
			context["deferredCritical"] = issueCount
		except:
			context["deferredCritical"] = "0"
		defferedIssues = defferedIssues + issueCount
		context["defferedIssues"] = defferedIssues
		return context
		
class GenerateExcel(View):
	def get(self, request, *args, **kwargs):
		response = HttpResponse(content_type='application/ms-excel')
		response['Content-Disposition'] = 'attachment; filename="ClinicalReport.xls"'
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet('QC')

		# Sheet header, first row
		row_num = 0
		font_style = xlwt.XFStyle()
		font_style.font.bold = True
		columns = ['Product Name', 'Current Status', 'Defects Logged', 'Plan Start date', 'Plan End Date', 'Remarks']
		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num], font_style)

		# Sheet body, remaining rows
		font_style = xlwt.XFStyle()
		currentPath = request.get_full_path()
		temp = currentPath.split("/")
		searchDate = temp[2].replace("%20", " ")
		searchDate = searchDate.replace(",", "")
		searchDateObj = parser.parse(searchDate)
		currentDate = searchDateObj
		DisplayDate = searchDateObj
		object_list = DailyStatusQC.objects.filter(LogDate=currentDate).values_list('ProductName', 'CurrentStatus', 'IssuesLogged')
		projectQcList = ProjectQC.objects.all().values('ProductName')
		statusQcList = DailyStatusQC.objects.filter(LogDate=currentDate).values('ProductName')
		itr1 = 0
		itr2 = 0
		temp_dict = {}
		while itr1 < projectQcList.count():
			if projectQcList[itr1] not in statusQcList:
				temp_dict[itr2] = projectQcList[itr1]['ProductName']
				itr2 = itr2 + 1
			itr1 = itr1 + 1
		dateItr = 1
		itr1 = 0
		ds = []
		while itr1 < itr2:
			#print(itr1)
			dateItr = 1
			while dateItr < 4:
				d = DisplayDate - timedelta(days=dateItr)
				qs = DailyStatusQC.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
				#print(qs)
				if qs:
					#print("exist")
					ds.append(DailyStatusQC.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])).values_list('ProductName', 'CurrentStatus', 'IssuesLogged'))
					#print(ds)
					break
				dateItr = dateItr + 1
			itr1 = itr1 + 1
		object_list1 = ds	
		rows1 = object_list
		rows2 = object_list1
		projectListQc = ProjectQC.objects.all().values_list('ProductName', 'PlanStartDate', 'PlanEndDate', 'Remarks', 'TempPlanStartDate', 'TempPlanEndDate')
		for row in rows1:
			row_num += 1
			for col_num in range(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)
				if col_num == 0:
					for obj in projectListQc:
						if row[col_num] == obj[0]:
							ws.write(row_num, col_num+3 , obj[1].strftime('%d/%m/%Y'), font_style)
							ws.write(row_num, col_num+4 , obj[2].strftime('%d/%m/%Y'), font_style)
							ws.write(row_num, col_num+5 , obj[3], font_style)
		
		for row in rows2:
			row_num += 1
			for col_num in range(len(row[0])):
				ws.write(row_num, col_num, row[0][col_num], font_style)
				if col_num == 0:
					for obj in projectListQc:
						if row[0][col_num] == obj[0]:
							ws.write(row_num, col_num+3 , obj[1].strftime('%d/%m/%Y'), font_style)
							ws.write(row_num, col_num+4 , obj[2].strftime('%d/%m/%Y'), font_style)
							ws.write(row_num, col_num+5 , obj[3], font_style)
		

		
		ws1 = wb.add_sheet('PQ')

		# Sheet header, first row
		row_num = 0
		font_style = xlwt.XFStyle()
		font_style.font.bold = True
		columns = ['Product Name', 'Current Status', 'Defects Logged', 'Plan Start date', 'Plan End Date', 'Remarks']
		for col_num in range(len(columns)):
			ws1.write(row_num, col_num, columns[col_num], font_style)

		# Sheet body, remaining rows
		font_style = xlwt.XFStyle()
		currentPath = request.get_full_path()
		temp = currentPath.split("/")
		searchDate = temp[2].replace("%20", " ")
		searchDate = searchDate.replace(",", "")
		searchDateObj = parser.parse(searchDate)
		currentDate = searchDateObj
		DisplayDate = searchDateObj
		pq_list = DailyStatusPQ.objects.filter(LogDate=currentDate).values_list('ProductName', 'CurrentStatus', 'IssuesLogged')
		projectPqList = ProjectPq.objects.all().values('ProductName')
		statusPqList = DailyStatusPQ.objects.filter(LogDate=currentDate).values('ProductName')
		itr1 = 0
		itr2 = 0
		temp_dict = {}
		while itr1 < projectPqList.count():
			if projectPqList[itr1] not in statusPqList:
				temp_dict[itr2] = projectPqList[itr1]['ProductName']
				itr2 = itr2 + 1
			itr1 = itr1 + 1
		dateItr = 1
		itr1 = 0
		ds = []
		while itr1 < itr2:
			#print(itr1)
			dateItr = 1
			while dateItr < 4:
				d = DisplayDate - timedelta(days=dateItr)
				qs = DailyStatusPQ.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
				#print(qs)
				if qs:
					#print("exist")
					ds.append(DailyStatusPQ.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])).values_list('ProductName', 'CurrentStatus', 'IssuesLogged'))
					#print(ds)
					break
				dateItr = dateItr + 1
			itr1 = itr1 + 1
		object_list1 = ds	
		rows1 = pq_list
		rows2 = object_list1
		projectListPq = ProjectPq.objects.all().values_list('ProductName', 'PlanStartDate', 'PlanEndDate', 'Remarks')
		for row in rows1:
			row_num += 1
			for col_num in range(len(row)):
				ws1.write(row_num, col_num, row[col_num], font_style)
				if col_num == 0:
					for obj in projectListPq:
						if row[col_num] == obj[0]:
							ws1.write(row_num, col_num+3 , obj[1].strftime('%d/%m/%Y'), font_style)
							ws1.write(row_num, col_num+4 , obj[2].strftime('%d/%m/%Y'), font_style)
							ws1.write(row_num, col_num+5 , obj[3], font_style)
		
		for row in rows2:
			row_num += 1
			for col_num in range(len(row[0])):
				ws1.write(row_num, col_num, row[0][col_num], font_style)
				if col_num == 0:
					for obj in projectListPq:
						if row[0][col_num] == obj[0]:
							ws1.write(row_num, col_num+3 , obj[1].strftime('%d/%m/%Y'), font_style)
							ws1.write(row_num, col_num+4 , obj[2].strftime('%d/%m/%Y'), font_style)
							ws1.write(row_num, col_num+5 , obj[3], font_style)

		
		
		
		ws = wb.add_sheet('Automation')

		# Sheet header, first row
		row_num = 0
		font_style = xlwt.XFStyle()
		font_style.font.bold = True
		columns = ['Product Name', 'Current Status', 'Total Planned Scenarios', 'Scenarios Covered', 'Scenarios In-Progress', 'Plan Start date', 'Plan End Date', 'Remarks']
		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num], font_style)

		# Sheet body, remaining rows
		font_style = xlwt.XFStyle()
		currentPath = request.get_full_path()
		temp = currentPath.split("/")
		searchDate = temp[2].replace("%20", " ")
		searchDate = searchDate.replace(",", "")
		searchDateObj = parser.parse(searchDate)
		currentDate = searchDateObj
		DisplayDate = searchDateObj
		object_list = DailyStatusAuto.objects.filter(LogDate=currentDate).values_list('ProductName', 'CurrentStatus', 'TotalScenarios', 'ScenariosCovered', 'ScenariosInprogress')
		projectAutoList = ProjectAuto.objects.all().values('ProductName')
		statusAutoList = DailyStatusAuto.objects.filter(LogDate=currentDate).values('ProductName')
		itr1 = 0
		itr2 = 0
		temp_dict = {}
		while itr1 < projectAutoList.count():
			if projectAutoList[itr1] not in statusAutoList:
				temp_dict[itr2] = projectAutoList[itr1]['ProductName']
				itr2 = itr2 + 1
			itr1 = itr1 + 1
		dateItr = 1
		itr1 = 0
		ds = []
		while itr1 < itr2:
			#print(itr1)
			dateItr = 1
			while dateItr < 4:
				d = DisplayDate - timedelta(days=dateItr)
				qs = DailyStatusAuto.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1]))
				#print(qs)
				if qs:
					#print("exist")
					ds.append(DailyStatusAuto.objects.filter(Q(LogDate=d) & Q(ProductName__iexact=temp_dict[itr1])).values_list('ProductName', 'CurrentStatus', 'TotalScenarios', 'ScenariosCovered', 'ScenariosInprogress'))
					#print(ds)
					break
				dateItr = dateItr + 1
			itr1 = itr1 + 1
		object_list1 = ds	
		rows1 = object_list
		rows2 = object_list1
		projectListAuto = ProjectAuto.objects.all().values_list('ProductName', 'PlanStartDate', 'PlanEndDate', 'Remarks')
		for row in rows1:
			row_num += 1
			for col_num in range(len(row)):
				ws.write(row_num, col_num, row[col_num], font_style)
				if col_num == 0:
					for obj in projectListAuto:
						if row[col_num] == obj[0]:
							ws.write(row_num, col_num+5 , obj[1].strftime('%d/%m/%Y'), font_style)
							ws.write(row_num, col_num+6 , obj[2].strftime('%d/%m/%Y'), font_style)
							ws.write(row_num, col_num+7 , obj[3], font_style)
		
		for row in rows2:
			row_num += 1
			for col_num in range(len(row[0])):
				ws.write(row_num, col_num, row[0][col_num], font_style)
				if col_num == 0:
					for obj in projectListAuto:
						if row[0][col_num] == obj[0]:
							ws.write(row_num, col_num+5 , obj[1].strftime('%d/%m/%Y'), font_style)
							ws.write(row_num, col_num+6 , obj[2].strftime('%d/%m/%Y'), font_style)
							ws.write(row_num, col_num+7 , obj[3], font_style)
		
		
		
		wb.save(response)
		return response