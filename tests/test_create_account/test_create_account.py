import allure
import urls

@allure.feature("Проверяем функционал создания аккаунта")
class TestCreateAccount:

    @allure.title(
        "Проверяем, что успешное создания аккаунта редиректит "
        "на страницу авторизации с отображением формы авторизации"
    )
    def test_successfully_account_create_redirect_on_signin_form(
            self,
            home_page,
            header_page,
            create_account_page,
            login_page,
            generate_user_payload
    ):
        first_name, last_name, user_name, email, password = generate_user_payload

        with allure.step("Переходим по url на главную страницу"):
            home_page.go_to_main_page_url()

        with allure.step("Нажимаем кнопку 'Создать аккаунт' в хедере"):
            header_page.click_to_header_create_account_btn()

        with allure.step("Заполняем форму создания аккауннта поле 'Имя'"):
            create_account_page.enter_first_name(first_name)

        with allure.step("Заполняем форму создания аккауннта поле 'Фамилия'"):
            create_account_page.enter_last_name(last_name)

        with allure.step("Заполняем форму создания аккауннта поле 'Имя пользователя'"):
            create_account_page.enter_username(user_name)

        with allure.step("Заполняем форму создания аккауннта поле 'Адрес электронной почты'"):
            create_account_page.enter_email(email)

        with allure.step("Заполняем форму создания аккауннта поле 'Пароль'"):
            create_account_page.enter_password(password)

        with allure.step("Нажимаем кнопку 'Создать аккаунт' в форме регистрации"):
            create_account_page.click_to_signup_btn()

        with allure.step("Ждём появления формы авторизации"):
            login_page.wait_login_form_visible(timeout=15)

        with allure.step("Проверяем, что после успешной регистрации сработал редирект"):
            assert create_account_page.get_current_url() == urls.SIGNIN_URL, (
                f"Ожидался URL: {urls.SIGNIN_URL}, "
                f"но открыт: {create_account_page.get_current_url()}"
            )

        with allure.step("Проверяем, что форма авторизации отображается"):
            assert login_page.is_login_form_visible(), (
                "Форма авторизации не отображается"
            )
