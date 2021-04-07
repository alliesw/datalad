# emacs: -*- mode: python; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 noet:
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the datalad package for the
#   copyright and license terms.
#
# ## ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
"""A helper command to enable shell (bash, zsh) completion for DataLad

"""
__docformat__ = 'restructuredtext'


from .base import Interface
from datalad.interface.base import build_doc


@build_doc
class ShellCompletion(Interface):
    """Display shell script for enabling shell completion for DataLad.

    Output of this command should be "sourced" by the bash or zsh to enable
    shell completions provided by argcomplete.

    Example:

        $ source <(datalad shell-completion)
        $ datalad --<PRESS TAB to display available option>

    """
    # XXX prevent common args from being added to the docstring
    _no_eval_results = True
    _params_ = {}

    @staticmethod
    def __call__():
        """
        """
        print("""\
# Universal completion script for DataLad with the core autogenerated by
# python-argcomplete and only slightly improved to work for ZSH if sourced under ZSH.
#
# Instead of just running this command and seeing this output, do
#
#    source <(datalad shell-completion)
#
# in your bash or zsh session.

if [ "${ZSH_VERSION:-}" != "" ]; then
  autoload -U compinit && compinit
  autoload -U bashcompinit && bashcompinit
fi

_python_argcomplete() {
    local IFS=''
    COMPREPLY=( $(IFS="$IFS" COMP_LINE="$COMP_LINE" COMP_POINT="$COMP_POINT" _ARGCOMPLETE_COMP_WORDBREAKS="$COMP_WORDBREAKS" _ARGCOMPLETE=1                   "$1" 8>&1 9>&2 1>/dev/null 2>/dev/null) )
    if [[ $? != 0 ]]; then
        unset COMPREPLY
    fi
}

complete -o nospace -o default -F _python_argcomplete "datalad"
""")
