
class StringProcessor:

    def __init__(self):
        pass

    # @staticmethod
    # def reverse_and_merge(original_string):
    #
    #     result_string = original_string[-1]
    #
    #     index = len(original_string) - 2
    #     while index >= 0:
    #         if result_string[-1] != original_string[index]:
    #             result_string += original_string[index]
    #
    #         index -= 1
    #
    #     return result_string


    # @staticmethod
    # def reverse_and_merge(original_string):
    #
    #     if not original_string or len(original_string) < 2:
    #         return original_string
    #
    #     result_string = original_string[-1]
    #
    #     index = len(original_string) - 2
    #     while index > 0:
    #         if result_string[-1] != original_string[index]:
    #             result_string += original_string[index]
    #
    #         index -= 1
    #
    #     return result_string


    @staticmethod
    def reverse_and_merge(original_string):

        if not original_string or len(original_string) < 2:
            return original_string

        result_string = original_string[-1]

        index = len(original_string) - 2
        while index >= 0:
            if result_string[-1] != original_string[index]:
                result_string += original_string[index]

            index -= 1

        return result_string


if __name__ == '__main__':

    myString = 'aabbbcca'
    print(myString)
    # print(string_processor.reverse_and_merge(original_string))
    print(StringProcessor.reverse_and_merge(myString))

