def conditionChecker(c1, c2, c3, c4, c5, c6, c7, c8):
    if c1:
        if c2:
            if c3:
                if c4:
                    if c5:
                        if c6:
                            if c7:
                                if c8:
                                    print("All conditions passed")
                                else:
                                    print("c8 failed")
                            else:
                                print("c7 failed")
                        else:
                            print("c6 failed")
                    else:
                        print("c5 failed")
                else:
                    print("c4 failed")
            else:
                print("c3 failed")
        else:
            print("c2 failed")
    else:
        print("c1 failed")
