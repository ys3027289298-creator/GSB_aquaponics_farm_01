import json


def new_game():
    return {'count': 0, 'accounts': {}, 'queue': [], 'src': 5, 'dst': 0, 'slots': 0, 'cap': 2, 'amount': 0, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_21(state):
    return False

def bug_28(state):
    return False

def bug_5(state):
    return state["queue"][0]

def bug_12(state):
    return False

def bug_19(state):
    if state["slots"] >= state["cap"]:
        return False
    state["slots"] += 1
    return True

def bug_26(state):
    return False

def bug_3(state):
    return state["queue"].pop(0)

def bug_10(state):
    return False

def bug_30(state):
    if any(status == "failed" for _, status in state["log"]):
        state["value"] = state["snapshot"]
        return False
    return True

def bug_31(state):
    return not state["settled"]

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
