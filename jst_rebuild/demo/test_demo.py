import  unittest
import HTMLTestRunner


class Test_demo2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('这是所有case的前置条件01')

    @classmethod
    def tearDownClass(cls):
        print('这是所有case的后置条件01')

    def setUp(self):
        print('这是每条case的前置条件01')

    def tearDown(self):
        print('这是每条case的后置条件01')

    def testThird_01(self):  # 测试用例的命名必须以test开头，否则不予执行
        print('01: 第三条case')

    def testFirst_01(self):
        print('01: 第一条case')

    @unittest.skip('不执行这条case')  # 跳过这条case
    def testSecond_01(self):
        print('01: 第二条case')

    def testFourth_01(self):
        print('01: 第四条case')



if __name__  == '__main__':
    #装载测试用例
  #  test_case = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)

    # 使用测试套件并打包测试用例
 #   suit = unittest.TestSuite()
 #   suit.addTest(TestStringMethods('testFirst_01'))
 #   suit.addTest(TestStringMethods('testThird_01'))
    #运行测试套件，并返回结果
    #生成测试报告
#    filepath = 'D:/测试/测试结果.html'
    test_result2 = unittest.TextTestRunner(stream=None,verbosity=2)
    unittest.main()
  ##  test_result2.run(suit)


   # with  open(filepath, 'wb',encoding='utf-8') as file:
   #     test_result = HTMLTestRunner.HTMLTestRunner(stream=file,title='test_report',verbosity=2)
    #    test_result.run(suit)

