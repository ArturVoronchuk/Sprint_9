import allure

import data
import urls


@allure.feature("Проверяем функционал страницы авторизации")
class TestLogin:

    @allure.title(
        "Проверяем, что успшная авторизация редиректит пользователя "
        "на страницу с рецептами, а так же что при успешной авторизации "
        "отображается кнопка 'Выход'"
    )
    def test_successful_login_redirect_on_main_page(
            self,
            header_page,
            login_page
    ):

        with allure.step("Открываем главную страницу"):
            header_page.go_to_url(urls.RECIPES_URL)

        with allure.step(
                "Нажимаем кноку 'Войти' в хедере для редиректа на форму авторизации"
        ):
            header_page.click_to_header_login_btn()

        with allure.step("Заполняем поле 'Электронная почта' в форме авторизации"):
            login_page.enter_email(data.test_username)

        with allure.step("Заполняем поле 'Пароль' в форме авторизации"):
            login_page.enter_password(data.test_password)

        with allure.step("Нажимаем кнопку 'Войти' в форме авторизации"):
            login_page.click_login_button()

        with allure.step("Ждём появления кнопки 'Выход' в хедере"):
            header_page.wait_logout_btn_visible(timeout=15)

        with allure.step("Проверяем, что сработал редирект на страницу с рецептами (главная страница)"):
            assert login_page.get_current_url() == urls.RECIPES_URL, (
                f"Ожидался URL: {urls.RECIPES_URL}, "
                f"но открыт: {login_page.get_current_url()}"
            )
        with allure.step("Проверяем, что кнопка 'Выход' появилась в хедере"):
            assert header_page.is_logout_btn_visible() , (
                "Кнопка 'Выход' не отображается в хэдере"
            )
