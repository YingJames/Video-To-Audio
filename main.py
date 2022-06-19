from lib2to3.pytree import convert
import yt_convert

def choice():
    answer = input("""What would you like to do?
[1] Convert a Youtube video into audio
[2] Quit

Answer with the number associated with a choice: """)

    return answer


def main():
    answer = choice()
    if (answer == '1'):
        yt_convert.convert_video()

    elif (answer == '2'):
        print("Have a nice day!")

main()