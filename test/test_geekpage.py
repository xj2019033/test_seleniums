import pytest
import sys





class TestGeekPage:

    def setup(self):
        sys.path.append("D:\\xing\\test_selenium")
        from src.geek_page import GeekPage
        self.geek=GeekPage()

    def teardown(self):
        self.geek.quit()

    def test_login(self):
        self.geek.login()

    def test_login1(self):
        self.geek.login()

    def test_login2(self):
        self.geek.login()

    def test_login3(self):
        self.geek.login()

# if __name__=="__main__":
#
#     #pytest.main(['-s','-v','-n=3','test_geekpage.py'])
#     pytest.main(['-s', '-v','--workers=1', '--tests-per-worker=4'])
