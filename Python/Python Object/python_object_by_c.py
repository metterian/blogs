#%%
import ctypes
import sys


class IntStruct(ctypes.Structure):
    _fields_ = [
        ("ob_refcnt", ctypes.c_long),
        ("ob_type", ctypes.c_void_p),
        ("ob_size", ctypes.c_ulong),
        ("ob_digit", ctypes.c_long),
    ]

    def __repr__(self) -> str:
        return "IntStruct(ob_digit={self.ob_digit}, " "refcount={self.ob_refcnt})".format(self=self)


# %%
num = 42
IntStruct.from_address(id(42))
# %%
