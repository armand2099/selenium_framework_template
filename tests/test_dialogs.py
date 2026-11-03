import pytest
from pages.dialogs_page import DialogsPage

DIALOGS_URL = "https://testpages.eviltester.com/pages/basics/alerts-javascript/"

@pytest.fixture(scope="function")
def dialogs_page(browser):
    browser.get(DIALOGS_URL)
    dialogs_page = DialogsPage(browser)
    return dialogs_page

@pytest.mark.DIAL
def test_alert(dialogs_page: DialogsPage, logger):
    assert dialogs_page.alert_text.text == ''
    dialogs_page.alert_button.click()
    dialogs_page.on_dialog()
    dialogs_page.wait.until(lambda driver: dialogs_page.alert_text.text != '')
    assert dialogs_page.alert_text.text =='You triggered and handled the alert dialog'
    logger.log("Alert Dialog")

@pytest.mark.DIAL
def test_confirm_accept(dialogs_page: DialogsPage, logger):
    assert dialogs_page.confirm_text.text ==''
    dialogs_page.confirm_button.click()
    dialogs_page.on_dialog()
    dialogs_page.wait.until(lambda driver: dialogs_page.confirm_text.text != '')
    assert dialogs_page.confirm_return.text == 'true'
    assert dialogs_page.confirm_text.text == 'You clicked OK, confirm returned true.'
    logger.log(f"Dialog: {dialogs_page.confirm_text.text} confirmed")

@pytest.mark.DIAL
def test_confirm_dismiss(dialogs_page: DialogsPage, logger):
    assert dialogs_page.confirm_text.text == ''
    dialogs_page.confirm_button.click()
    dialogs_page.on_dialog("",False)
    dialogs_page.wait.until(lambda driver: dialogs_page.confirm_text.text != '')
    assert dialogs_page.confirm_return.text == 'false'
    assert dialogs_page.confirm_text.text == 'You clicked Cancel, confirm returned false.'
    logger.log(f"Dialog: {dialogs_page.confirm_text.text} Dismissed")

@pytest.mark.DIAL
def test_accept_prompt_dialog(dialogs_page: DialogsPage, logger):
    assert dialogs_page.prompt_text.text == ''
    dialogs_page.promp_box_button.click()
    dialogs_page.on_dialog('Hello World!')
    dialogs_page.wait.until(lambda driver: dialogs_page.prompt_text.text != '')
    assert dialogs_page.prompt_text.text == "You clicked OK. 'prompt' returned Hello World!"
    assert dialogs_page.promp_return.text =='Hello World!'
    logger.log("Accept Prompt Dialog: " + dialogs_page.promp_return.text)

@pytest.mark.DIAL
def test_dismiss_prompt_dialog(dialogs_page: DialogsPage, logger):
    assert dialogs_page.prompt_text.text ==''
    dialogs_page.promp_box_button.click()
    dialogs_page.on_dialog("",False)
    dialogs_page.wait.until(lambda driver: dialogs_page.prompt_text.text != '')
    assert dialogs_page.prompt_text.text == "You clicked Cancel. 'prompt' returned null"
    assert dialogs_page.promp_return.text == ''
    logger.log(f"Dismiss Prompt Dialog: {dialogs_page.prompt_text.text}")