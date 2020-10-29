class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:

    def __init__(self, kind):
        self.kind = kind


class EventSet:
    def __init__(self, kind):
        self.kind = kind


class NullHandler:

    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):

    def handle(self, obj, event):
        print('Обработчик int')
        if type(event) == EventGet:
            if event.kind == int:
                return obj.integer_field
            else:
                print("Передаю обработку дальше\n")
                return super().handle(obj, event)

        elif type(event) == EventSet:
            if type(event.kind) == int:
                obj.integer_field = event.kind
            else:
                print("Передаю обработку дальше\n")
                super().handle(obj, event)



class FloatHandler(NullHandler):

    def handle(self, obj, event):
        print('Обработчик float')
        if type(event) == EventGet:
            if event.kind == float:
                return obj.float_field
            else:
                print("Передаю обработку дальше\n")
                return super().handle(obj, event)

        elif type(event) == EventSet:
            if type(event.kind) == float:
                obj.float_field = event.kind
            else:
                print("Передаю обработку дальше\n")
                super().handle(obj, event)


class StrHandler(NullHandler):

    def handle(self, obj, event):
        print('Обработчик str')
        if type(event) == EventGet:
            if event.kind == str:
                return obj.string_field
            else:
                print("Передаю обработку дальше\n")
                return super().handle(obj, event)

        elif type(event) == EventSet:
            if type(event.kind) == str:
                obj.string_field = event.kind
            else:
                print("Передаю обработку дальше\n")
                super().handle(obj, event)


# obj = SomeObject()
# obj.integer_field = 63
# obj.float_field = 14.5
# obj.string_field = 'sybwol'
#
# chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
#
# f = chain.handle(obj, EventGet(float))
# print(f)
# s = chain.handle(obj, EventGet(str))
# print(s)
# print('--------------')
# chain.handle(obj, EventSet('СТРОКА!!!!'))
# print('!!!!!!!!!!!!')
# s = chain.handle(obj, EventGet(str))
# print(s)