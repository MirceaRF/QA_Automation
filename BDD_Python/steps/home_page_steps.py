from behave import *

@given('I am on Ebay home page')
def step_impl(context):
    context.home_page_object.navigate_to_home_page()


@when('I search an item')
def step_impl(context):
    context.home_page_object.set_product_search()
    context.home_page_object.click_search_button()

@then('I have at least 2 results returned')
def step_impl(context):
    context.home_page_object.check_search_results()
