import allure
import data


@allure.feature("Проверяем функционал страницы создания рецептов")
class TestCreateRecipe:

    def test_authorized_user_creates_recipe_and_sees_card_with_correct_name(
            self, create_recipe_page, header_page, login_page, home_page):

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

        with allure.step("Нажимаем кнопку 'Создть рецепт'"):
            header_page.click_create_recipe_btn()

        with allure.step("Заполняем поле 'Название рецепта' в форме создания рецепта"):
            create_recipe_page.enter_recipe_name(data.recipe_name)

        with allure.step("Снимаем тэг 'Обед' в форме создания рецепта"):
            create_recipe_page.select_tag_lunch()

        with allure.step("Снимаем тэг 'Ужин' в форме создания рецепта"):
            create_recipe_page.select_tag_dinner()

        with allure.step("Вводим название 'Ингредиента' в форме создания рецепта"):
            create_recipe_page.enter_ingredient_name(data.recipe_ingredient_name)

        with allure.step(
                "Выбираем название ингредиента в выпадающем списке формы создания рецета"
        ):
            create_recipe_page.select_ingredient_from_dropdown(data.recipe_ingredient_name)

        with allure.step("Вводим количество ингредиента в граммах в форме создания рецепта"):
            create_recipe_page.enter_ingredient_amount(data.recipe_ingredient_amount)

        with allure.step("Нажимаем кнопку 'Добавить ингредиент' в форме создания рецепта"):
            create_recipe_page.click_add_ingredient_btn()

        with allure.step(
                "Заполняем поле 'Время приготоваления' в форме создания рецепта в минутах"
        ):
            create_recipe_page.enter_cooking_time(data.recipe_cooking_time)

        with allure.step(
                "Заполняем поле 'Время приготоваления' в форме создания рецепта в минутах"
        ):
            create_recipe_page.enter_description(data.recipe_description)

        with allure.step("Подгружаем изображение в форме создания рецепта"):
            create_recipe_page.upload_image(data.recipe_filename)

        with allure.step("Нажимамем кнопку 'Создать рецепт'"):
            create_recipe_page.click_create_recipe_btn()

        with allure.step("Переходим на главную страницу"):
            home_page.go_to_main_page_url()

        with allure.step("Проверяем, что карточка созданного рецепта отображается"):
            assert home_page.is_recipe_card_visible(data.recipe_name), (
                f"Карточка рецепта '{data.recipe_name}' не отображается"
            )

        with allure.step("Проверяем, что название в карточке совпадает с введённым"):
            card_name = home_page.get_recipe_card_name(data.recipe_name)
            assert card_name == data.recipe_name, (
                f"Название в карточке не совпадает: ожидалось '{data.recipe_name}', "
                f"получено '{card_name}'"
            )