"""
Test runner for the UI layer with MockLL
Run this to manually test the create_tournament flow
"""
import sys
sys.path.insert(0, 'src')


from UI.mainUI import UImain
from LL.logical_wraper import LLWrapper

def create_ll():
    try:
        return LLWrapper()
    except Exception as e:
        print("Warning: could not create LLWrapper:", e)
        return None

def main():
    ll = create_ll()
    ui = UImain(ll_wrapper=ll)
    ui.run()

if __name__ == "__main__":
    main()