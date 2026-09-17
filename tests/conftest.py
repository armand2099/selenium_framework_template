import pytest
import pytest_html
import selenium.webdriver


@pytest.fixture(scope="session")
def browser():

    # Initialize the web driver instance
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument('haded')
    b = selenium.webdriver.Chrome(options=opts)

    # Make its calls wait up 10 seconds for elements to appear
    b.implicitly_wait(10)

    # Maximise Chrome window
    b.maximize_window()

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()