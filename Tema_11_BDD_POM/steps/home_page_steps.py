from behave import *

@given('Home Page I am on herokuap homepage')
def step_impl(context):
    context.home_page_object.navigate_to_home_page()


#@when('Home Page I want to complete username as "{username}" and password as "{password}"')
@when('Home Page I want to complete username as "{username}" and password as "{password}"')
def step_impl(context,username,password):
    context.home_page_object.complete_username_password(username,password)


@then('Home Page I should be able to login')
def step_impl(context):
    context.home_page_object.click_login_button()
