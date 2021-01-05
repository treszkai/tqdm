"""
Calculate UTA: uncertain time of arrival

Usage:
>>> from tqdm.contrib.uncertain import tqdm, trange
>>> for i in tqdm(iterable):
...     ...

![screenshot](
https://raw.githubusercontent.com/tqdm/img/src/screenshot-uncertain.gif) # TODO
"""
# from __future__ import absolute_import # TODO needed?

import numpy as np

# TODO for development only
from ..std import tqdm as tqdm_auto
#from ..auto import tqdm as tqdm_auto
from ..utils import _range
__author__ = {'github.com/': ['treszkai']}
__all__ = ['tqdm', 'trange']


class tqdm(tqdm_auto):
    def __init__(self, *args, **kwargs):
        self._calculate_prior()
        # TODO either redefine these or __repr__
        self._ema_dn = ...
        self._ema_dt = ...
        super().__init__(*args, **kwargs)

    def _calculate_prior(self):
        self._log_prior_mu = ...
        self._log_prior_sigma = ...

    def __repr__(self):
        format_dict = self.format_dict
        return self.format_meter(**format_dict)


def trange(*args, **kwargs):
    """
    A shortcut for `tqdm.contrib.uncertain.tqdm(range(*args), **kwargs)`.
    On Python2, `xrange` is used instead of `range`.
    """
    return tqdm(_range(*args), **kwargs)
