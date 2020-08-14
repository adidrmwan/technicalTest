Feature: Register as New User on Fabelio Website

    Scenario: Register Page Should Be Displayed
        Given I Launch Chrome Browser
        When I Open Fabelio Homepage
            And I Move to Login Modal
            And I Click Register Link
        Then I Expect That the Register Title is "Buat Akun Baru"

    Scenario: Failed Register Using Blank Data
        Given I Launch Chrome Browser
        When I Open Fabelio Homepage
            And I Move to Login Modal
            And I Click Register Link
            And I Set Null Value to the All Input Field
            And I Click on the Buat Akun Button
        Then I Expect That Warning Message Should Be Displayed
    
    Scenario: Failed Register Invalid Email
        Given I Launch Chrome Browser
        When I Open Fabelio Homepage
            And I Move to Login Modal
            And I Click Register Link
            And I Set Invalid Value for Email Field
            And I Click Aggrement Checkbox
            And I Click on the Buat Akun Button
        Then I Expect That Warning Message on Email Field Should Be Displayed
    
    Scenario: Failed Register Invalid Password
        Given I Launch Chrome Browser
        When I Open Fabelio Homepage
            And I Move to Login Modal
            And I Click Register Link
            And I Set Invalid Value for Password Field
            And I Click Aggrement Checkbox
            And I Click on the Buat Akun Button
        Then I Expect That Warning Message on Password Field Should Be Displayed
    
    Scenario: Failed Register Not Click Checkbox
        Given I Launch Chrome Browser
        When I Open Fabelio Homepage
            And I Move to Login Modal
            And I Click Register Link
            And I Set Valid Value For Each Field
            And I Click on the Buat Akun Button
        Then I Expect That Warning Message on Checkbox Should Be Displayed
    