from behave import *
import requests

api_endpoints = {}
request_headers = {}
response_codes ={}
response_texts={}
request_bodies = {}
api_url=None

@given(u'I Set REST API httpbin url')
def step_impl(context):
    global api_url
    api_url = 'http://httpbin.org'

# START POST Scenario
@given(u'I Set POST api endpoint for "{id}"')
def step_impl(context,id):
    api_endpoints['POST_URL'] = api_url + '/delay/'+id

@when(u'I Set HEADER request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    request_headers['Content-Type'] = header_content_type

@when(u'I Send a POST HTTP request')
def step_impl(context):
    response = requests.post(url=api_endpoints['POST_URL'], headers=request_headers)
    response_texts['POST']=response.text
    statuscode = response.status_code
    response_codes['POST'] = statuscode

@then(u'I receive valid HTTP response code 200')
def step_impl(context):
    assert response_codes['POST'] is 200

@then(u'I Expect That Response BODY "{request_name}" is non-empty')
def step_impl(context,request_name):
    assert response_texts[request_name] is not None

# END POST Scenario

# START GET Scenario
@given(u'I Set GET api endpoint')
def step_impl(context):
    api_endpoints['GET_URL'] = api_url+'/image/jpeg'

@when(u'Send GET HTTP request')
def step_impl(context):
    response = requests.get(url=api_endpoints['GET_URL'], headers=request_headers)
    response_texts['GET']=response.text
    statuscode = response.status_code
    response_codes['GET'] = statuscode

@then(u'I receive valid HTTP response code 200 for "{request_name}"')
def step_impl(context,request_name):
    assert response_codes[request_name] is 200
#END GET Scenario

#START PUT Scenario
@given(u'I Set PUT api endpoint')
def step_impl(context):
    api_endpoints['PUT_URL'] = api_url + '/anything'

@when(u'Send PUT HTTP request')
def step_impl(context):
    response = requests.put(url=api_endpoints['PUT_URL'], headers=request_headers)
    response_texts['PUT'] = response.text
    statuscode = response.status_code
    response_codes['PUT'] = statuscode

#END PUT

# #START DELETE
@given(u'I Set DELETE api endpoint for "{id}"')
def step_impl(context,id):
    api_endpoints['DELETE_URL'] = api_url + '/delay/'+id

@when(u'I Send DELETE HTTP request')
def step_impl(context):
    response = requests.delete(url=api_endpoints['DELETE_URL'])
    response_texts['DELETE'] = response.text
    statuscode = response.status_code
    response_codes['DELETE'] = statuscode

#END DELETE