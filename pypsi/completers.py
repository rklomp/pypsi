#
# Copyright (c) 2015, Adam Meily <meily.adam@gmail.com>
# Pypsi - https://github.com/ameily/pypsi
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

'''
Builtin tab completion functions.
'''

from pypsi.os import path_completer  # noqa


def shell_path_completer(shell, args, prefix):
    return path_completer(args[-1] if args else '', prefix)


def choice_completer(choices, case_sensitive=False):
    '''
    Tab complete from a list of choices.

    :param list choices: the list of choices
    :param bool case_sensitive: whether the choices are case sensitive
    '''
    def complete(shell, args, prefix):
        r = []
        for choice in choices:
            if choice.startswith(prefix if case_sensitive else prefix.lower()):
                r.append(choice)
        return r
    return complete
