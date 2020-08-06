
class getInOurTable():
    def getInOurTable(self,acoountId):
        table = (acoountId %10)+1
        result = 'wepoint_test.t_account_in_out_log_0%d' %table
    #    print(result)
        return result

if __name__ == '__main__':

    test = getInOurTable()
    print(test.getInOurTable(1348088757))
