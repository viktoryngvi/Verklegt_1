from LL.logical_wraper import LLWrapper
from UI.mainUI import UImain

def main():
    print("============================================")
    print("      TOURNAMENT SYSTEM — TEST RUN          ")
    print("============================================")

    # Initialize Logic Layer Wrapper (LL + DL)
    ll_wrapper = LLWrapper()

    # Initialize full UI system
    ui = UImain(ll_wrapper)

    # Start the UI state machine
    ui.run()

    print("\nProgram exited successfully.")

if __name__ == "__main__":
    main()
