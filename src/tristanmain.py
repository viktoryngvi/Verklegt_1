from LL.logical_wraper import LLWrapper
from UI.mainUI import UIMain

def main():
    ll = LLWrapper()
    ui = UIMain(ll)
    ui.run()

if __name__ == "__main__":
    main()

    