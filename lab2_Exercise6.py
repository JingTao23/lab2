# print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

print("display_main_menu")
print("Enter some number s separated by commas (e.g. 5,67)")

def display_main_menu():
    print("display_main_menu")


    def get_user_input():
        print("get_user_input")
        inputstr = input()
        print("Raw Input = " + inputstr)

        # split the input string in to segments of strings using comma as spliter
        splitlist = inputstr.split(",")
        print("After splitting = ",splitlist)

        #next step is to convert each shirt string in the list into float
        floatlist = [] # define an empty list of float numbers
        for x in splitlist:
            floatnum = float(x) #Convert string into float
            floatlist.append(floatnum) # Add the float number to the float list
            return floatlist
        print("FLoat list")


        def calc_average(input_list):
            print("calc_average")


            def find_min_max(input_list):
                print("find_min_max")


                def sort_temperature(input_list):
                    print("sort_temperature")
                    

                    def calc_median_temperature(input_list):
                        print("calc_median_temperature")
                        cnt = len(input_list)

                        if cnt % 2 is 1:
                            median = input_list[(cnt-1)//2]
                        else:
                            median = (input_list[cnt//2] + input_list[cnt//2-1])/2
                            print("Median = ", median)

                        def main():
                            print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
                            display_main_menu()
                            floatlist = get_user_input()


                            if __name__ == "__main__":
                                main()




                    
