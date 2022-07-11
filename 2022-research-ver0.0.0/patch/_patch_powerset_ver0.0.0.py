
from itertools import chain,combinations
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def main():
    check_word = [
        'SC-APT-GET-INSTALL',
        'SC-APT-GET-F-NO-INSTALL-RECOMMENDS',
        'SC-RM',
        'SC-APT-GET-UPDATE',
        'SC-APT-GET-F-YES',
        'SC-RM-F-RECURSIVE',
        'SC-RM-F-FORCE',
        'SC-APT-GET-PACKAGES'
    ]
    check_list = powerset(check_word)
    for check in check_list:
        print(check)



if __name__ == "__main__":
    main()