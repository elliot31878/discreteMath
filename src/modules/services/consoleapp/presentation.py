from  ..toolsManager.toolsManager import ConcentrateHandlers


class Presentation:

    def __init__(self):
        super(Presentation, self).__init__()
        self.con_handler = ConcentrateHandlers()

    def show_elements(self):
        while 1:

                operation: str = input(""" 
                Please enter your operation \n
                 @: Zarb Dekarti \n 
                 -> : A -> B | B -> A \n 
                 0 : Zarb Manteghi Chand Matrix \n
                 V: Join Matrix \n ,
                 ^: Meet Matrix \n , 
                 [] : Sakhet matrix 1-0 ba majmaoe va zoje moratab \n
                 W: WarShall \n ,
                 Q : Use this character to exit
                """)
                if operation == '@':
                    collection_count: int = int(input("Please enter number your collection: "))
                    __arrays = []
                    for count in range(0, collection_count):
                        collection: str = input("Please enter your collection and splits with slash like 1_2_3... : ")
                        __arrays.append([])
                        if collection.__contains__("_"):
                            for item in collection.split("_"):
                                __arrays[count].append(item)
                            print(f"{count} : your collections {__arrays} ")
                    print(self.con_handler.notification(message={"arrays": __arrays}, to=f"{operation}"))

                elif operation == "->":
                    __arrays = []
                    for count in range(0, 2):
                        collection: str = input(" Please enter  your collection A -> B and splits with slash like 1_2_3... : ")
                        __arrays.append([])
                        if collection.__contains__("_"):
                            for item in collection.split("_"):
                                __arrays[count].append(item)
                            print(f"{count} : your collections {__arrays} ")
                    print(self.con_handler.notification(message={"arrays": __arrays}, to=f"{operation}"))

                elif operation == "0":
                    __arrays = []
                    collection: str = input("Please enter Enter your collection, and splits with slash  like 1_2_3... : ")
                    if collection.__contains__("_"):
                        for item in collection.split("_"):
                            __arrays.append(int(item))
                        print(f"your collections {__arrays} ")

                    matrix = self.con_handler.notification(message={"arrays": __arrays}, to=f"[]")
                    print(matrix)
                    multiMatrix: int = int(input("Please enter the matrix multiplication repetition value ? "))
                    array_matrix= []
                    for i in range(0, multiMatrix):
                        array_matrix.append(matrix)

                    print(self.con_handler.notification(message={"arrays": array_matrix}, to=f"{operation}"))

                elif operation == "[]":
                    __arrays = []
                    collection: str = input("Enter your collection and splits with slash  like 1_2_3... : ")
                    if collection.__contains__("_"):
                        for item in collection.split("_"):
                            __arrays.append(int(item))
                        print(f"your collections {__arrays} ")
                    print(self.con_handler.notification(message={"arrays": __arrays}, to=f"{operation}"))
                elif operation.lower() == "w":
                    __arrays = []
                    collection: str = input("Enter your collection and splits with slash  like 1_2_3... : ")
                    if collection.__contains__("_"):
                        for item in collection.split("_"):
                            __arrays.append(int(item))
                        print(f"your collections {__arrays} ")
                    result = self.con_handler.notification(message={"arrays": __arrays}, to=f"[]")
                    print(self.con_handler.notification(message={"arrays": result}, to=f"{operation.lower()}"))
                elif operation.lower() == "v":
                    __arrays = []
                    result = []
                    for count in range(0, 2):
                        collection: str = input("Enter your collection and splits with slash  like 1_2_3... : ")
                        if collection.__contains__("_"):
                            for item in collection.split("_"):
                                __arrays.append(int(item))
                        result.append(self.con_handler.notification(message={"arrays": __arrays}, to=f"[]"))

                    print(self.con_handler.notification(message={"arrays": result}, to=f"{operation.lower()}"))

                elif operation.lower() == "^":
                    __arrays = []
                    result = []
                    for count in range(0, 2):
                        collection: str = input("Enter your collection and splits with slash  like 1_2_3... : ")
                        if collection.__contains__("_"):
                            for item in collection.split("_"):
                                __arrays.append(int(item))
                        result.append(self.con_handler.notification(message={"arrays": __arrays}, to=f"[]"))

                    print(self.con_handler.notification(message={"arrays": result}, to=f"{operation.lower()}"))

                elif operation.lower() == "q":
                    break
                else:
                    print("You entered the wrong symbol")


