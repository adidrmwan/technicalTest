Feature: Simple CRUD Request for Httpbin URL

Background:
	Given I Set REST API httpbin url

Scenario: POST Dynamic Data Delay
  Given I Set POST api endpoint for "12"
  When I Set HEADER request content type as "application/json." 
    And I Send a POST HTTP request 
  Then I receive valid HTTP response code 200
    And I Expect That Response BODY "POST" is non-empty 

Scenario: GET Image
  Given I Set GET api endpoint
  When  I Set HEADER request content type as "image/jpeg"
    And Send GET HTTP request
  Then I receive valid HTTP response code 200 for "GET" 
	  And I Expect That Response BODY "GET" is non-empty

Scenario: PUT Anything
  Given I Set PUT api endpoint
  When  I Set HEADER request content type as "application/json." 
	  And   Send PUT HTTP request
  Then I receive valid HTTP response code 200 for "PUT" 
	  And   I Expect That Response BODY "PUT" is non-empty

Scenario: DELETE Dynamic Data Delay
  Given I Set DELETE api endpoint for "121"
  When  I Set HEADER request content type as "application/json." 
    And I Send DELETE HTTP request
  Then  I receive valid HTTP response code 200 for "DELETE" 
    And  I Expect That Response BODY "DELETE" is non-empty