from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\Python39/geckodriver.exe"

        # Coloque o caminho para o seu geckodriver dentro das "" acima.
        # Recomendo que baixe ele e já o mova, para dentro do diretório Python
        # Link download do geckodriver: https://github.com/mozilla/geckodriver/releases
        # Link download Firefox https://www.mozilla.org/pt-BR/firefox/new/
        )
        self.driver.maximize_window()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_nas_fotos_com_a_hashtag(
            "morenailuminada"
        )  # Altere aqui para a hashtag que você deseja usar.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def comente_nas_fotos_com_a_hashtag(self, hashtag):
        links_de_posts = []
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(
            1, 5
        ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        for link in pic_hrefs:
            try:
                if link.index("/p/") != -1:
                    links_de_posts.append(link)
            except:
                pass

        for pic_href in links_de_posts:
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                comments = [
                    "Inspirador!",
                    "Top de linha!",
                    "Inspirador sua postagem!",
                    "Que conteúdo bacana você tem!",
                    "Que legal!🤩",
                    "Você não merece um elogio, merece um caminhão de enaltecimentos.😍",
                    "Linda de todos os jeitos, ângulos… Me choco com essa beleza até do avesso.😛",
                    "Deus criou o mundo para todos, mas a beleza ele guardou só para você, né?😲",
                    "Quando Deus te desenhou, ele tinha acabado de se formar em Artes plásticas, não é possível tanta beleza.😍",
                    "Tão linda que parece um strogonoff.😋",
                    "Quase fiz carinho na tela do celular.😄",
                    "Você tem um band-aid? Eu acabei de me machucar caindo de amores por você.😱",
                    "Você não é a sétima maravilha do mundo, é a oitava.❤",
                    "Avisa quando for postar foto de novo que eu tenho que preparar meu coração primeiro.😍",
                    "Parece ator de Hollywood, nasceu para as câmeras.📷",
                    "Se ser perfeita fosse crime, eu ligava pra polícia ir agora pra te prender.😂",
                    "Passou na fila da beleza duas vezes, né?💖",
                    "Tem tudo para dominar o mundo com essa foto.🌍",
                    "Se é assim em foto, imagina ao vivo.😍",
                    "Cadê a localização do museu? Estou diante de uma obra de arte.👏",
                ]  # Remova esses comentários e insira os seus comentários aqui
                element=driver.find_element_by_class_name("_9AhH0")
                actions=ActionChains(driver)
                actions.double_click(element).perform()
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 5))
                self.type_like_a_person(
                    random.choice(comments), comment_input_box)
                time.sleep(random.randint(3, 5))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(random.randint(3, 5))
            except Exception as e:
                print(e)
                time.sleep(5)

# Entre com o usuário e senha aqui
boot = InstagramBot("seuusuario", "suasenha")
boot.login()