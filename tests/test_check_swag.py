from pages.swag_labs import SwagLabs

def test_check_icon(browser):

    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_icon()
    assert swag_labs_page.is_name_field_present()
    assert swag_labs_page.is_password_field_present()