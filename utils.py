#! /usr/bin/python3


def extract_loops(loops):
    """ Recursively extract the outer most loops into lists

    >>> extract_loops(["++>-[++<-]+-[[+]-][++->[--<+]]"])
    ['++>-', ['++<-'], '+-', [['+'], '-'], ['++->', ['--<+']]]
    """
    new_loops = []

    for loop in loops:
        brackets = 0
        op_block = ""
        for op in loop:
            if op not in "[]":
                op_block += op

            else:
                if op == "[":
                    if not brackets:
                        # Non loop structure
                        if op_block != "":
                            new_loops.append(op_block)
                            op_block = ""
                    else:
                        op_block += "["
                    brackets += 1

                elif op == "]":
                    brackets -= 1
                    if not brackets:
                        # Loop structure
                        if "[" in op_block or "]" in op_block:
                            op_block = extract_loops([op_block])
                        else:
                            op_block = [op_block]
                        new_loops.append(op_block)
                        op_block = ""
                    else:
                        op_block += "]"

        if op_block != "":
            new_loops.append(op_block)

    return new_loops


def in_nD_list(search_list, key):
    """ Find element in non-uniform nD list recursively

    >>> in_nD_list(["++--,.", ["++>-", [">++"]], [["+"], [["-"]]]], "]")
    False
    """
    for element in search_list:
        if isinstance(element, str):
            if key in element:
                return True
        elif in_nD_list(element, key):
            return True

    return False
