import threading
import time
import msvcrt


def gently_stop_program():
    def my_print():
        global flag
        flag = False
        print("Нажми Enter, чтобы остановить закрытие программы")
        while not flag:
            key = msvcrt.getwch()
            if ord(key) == 13:
                flag = True

    def timer():
        global flag
        print()
        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)
            if flag:
                break

    t1 = threading.Thread(target=my_print, daemon=True)
    t2 = threading.Thread(target=timer)

    t1.start()
    t2.start()

    t2.join()

    if flag:
        input("Нажми Enter, чтобы закрыть программу.")

    print("\nКонец работы программы")
    time.sleep(2)
