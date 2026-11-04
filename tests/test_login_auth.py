import pytest


@pytest.mark.AUTH
async def test_login_with_auth(browser_auth, logger_auth):
    print(f'\n------{__name__}------')

    browser_auth.get("https://myaccount.google.com/")
    assert browser_auth.title == "Cuenta de Google"
    await logger_auth.log(f'Page |{await browser_auth.title}| opened')