import json


def new_game():
    return {'count': 0, 'accounts': {}, 'queue': [], 'src': 5, 'dst': 0, 'slots': 0, 'cap': 2, 'amount': 0, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_21(state):
    return state["slots"] >= state["cap"]

def bug_28(state):
    return state["value"] < 0

def bug_5(state):
    return state["queue"][0]

def bug_12(state):
    if state["src"] >= 10:
        state["src"] -= 10
        state["dst"] += 10
        return True
    return False

def bug_19(state):
    return state["slots"] < state["cap"]

def bug_26(state):
    start, end = state.get("window", (0, 0))
    return 0 <= start < end

def bug_3(state):
    return state["queue"].pop(0)

def bug_10(state):
    if state["amount"] + (-5) < 0:
        return False
    state["amount"] += -5
    return True

def bug_30(state):
    if any(status == "failed" for _, status in state["log"]):
        state["value"] = state["snapshot"]
        return False
    state["snapshot"] = state["value"]
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
