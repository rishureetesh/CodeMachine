import threading

def thread_test():
    print("Thread Execution cycle!!, ",threading.current_thread().name)

object_one = threading.Thread(target=thread_test,name="Thread One", daemon=True)
object_two = threading.Thread(target=thread_test,name="Thread Two", daemon=True)
object_one.start()
object_two.start()