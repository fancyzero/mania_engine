# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_basis', [dirname(__file__)])
        except ImportError:
            import _basis
            return _basis
        if fp is not None:
            try:
                _mod = imp.load_module('_basis', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _basis = swig_import_helper()
    del swig_import_helper
else:
    import _basis
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


axis_x = _basis.axis_x
axis_y = _basis.axis_y
axis_z = _basis.axis_z
class point(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, point, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, point, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _basis.point_x_set
    __swig_getmethods__["x"] = _basis.point_x_get
    if _newclass:x = _swig_property(_basis.point_x_get, _basis.point_x_set)
    __swig_setmethods__["y"] = _basis.point_y_set
    __swig_getmethods__["y"] = _basis.point_y_get
    if _newclass:y = _swig_property(_basis.point_y_get, _basis.point_y_set)
    def __init__(self): 
        this = _basis.new_point()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _basis.delete_point
    __del__ = lambda self : None;
point_swigregister = _basis.point_swigregister
point_swigregister(point)

class vector2(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector2, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _basis.new_vector2(*args)
        try: self.this.append(this)
        except: self.this = this
    def __eq__(self, *args): return _basis.vector2___eq__(self, *args)
    def _assign(self, *args): return _basis.vector2__assign(self, *args)
    def _float(self): return _basis.vector2__float(self)
    __swig_setmethods__["x"] = _basis.vector2_x_set
    __swig_getmethods__["x"] = _basis.vector2_x_get
    if _newclass:x = _swig_property(_basis.vector2_x_get, _basis.vector2_x_set)
    __swig_setmethods__["y"] = _basis.vector2_y_set
    __swig_getmethods__["y"] = _basis.vector2_y_get
    if _newclass:y = _swig_property(_basis.vector2_y_get, _basis.vector2_y_set)
    __swig_destroy__ = _basis.delete_vector2
    __del__ = lambda self : None;
vector2_swigregister = _basis.vector2_swigregister
vector2_swigregister(vector2)

class vector3(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector3, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector3, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _basis.new_vector3(*args)
        try: self.this.append(this)
        except: self.this = this
    def __add__(self, *args): return _basis.vector3___add__(self, *args)
    def __sub__(self, *args): return _basis.vector3___sub__(self, *args)
    def normalize(self): return _basis.vector3_normalize(self)
    def __eq__(self, *args): return _basis.vector3___eq__(self, *args)
    def _assign(self, *args): return _basis.vector3__assign(self, *args)
    def length(self): return _basis.vector3_length(self)
    def _float(self): return _basis.vector3__float(self)
    __swig_setmethods__["x"] = _basis.vector3_x_set
    __swig_getmethods__["x"] = _basis.vector3_x_get
    if _newclass:x = _swig_property(_basis.vector3_x_get, _basis.vector3_x_set)
    __swig_setmethods__["y"] = _basis.vector3_y_set
    __swig_getmethods__["y"] = _basis.vector3_y_get
    if _newclass:y = _swig_property(_basis.vector3_y_get, _basis.vector3_y_set)
    __swig_setmethods__["z"] = _basis.vector3_z_set
    __swig_getmethods__["z"] = _basis.vector3_z_get
    if _newclass:z = _swig_property(_basis.vector3_z_get, _basis.vector3_z_set)
    def __str__(self): return _basis.vector3___str__(self)
    __swig_destroy__ = _basis.delete_vector3
    __del__ = lambda self : None;
vector3_swigregister = _basis.vector3_swigregister
vector3_swigregister(vector3)

class vector4(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vector4, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vector4, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _basis.new_vector4(*args)
        try: self.this.append(this)
        except: self.this = this
    def _assign(self, *args): return _basis.vector4__assign(self, *args)
    def _vector3(self): return _basis.vector4__vector3(self)
    def _float(self): return _basis.vector4__float(self)
    def length(self): return _basis.vector4_length(self)
    __swig_setmethods__["x"] = _basis.vector4_x_set
    __swig_getmethods__["x"] = _basis.vector4_x_get
    if _newclass:x = _swig_property(_basis.vector4_x_get, _basis.vector4_x_set)
    __swig_setmethods__["y"] = _basis.vector4_y_set
    __swig_getmethods__["y"] = _basis.vector4_y_get
    if _newclass:y = _swig_property(_basis.vector4_y_get, _basis.vector4_y_set)
    __swig_setmethods__["z"] = _basis.vector4_z_set
    __swig_getmethods__["z"] = _basis.vector4_z_get
    if _newclass:z = _swig_property(_basis.vector4_z_get, _basis.vector4_z_set)
    __swig_setmethods__["w"] = _basis.vector4_w_set
    __swig_getmethods__["w"] = _basis.vector4_w_get
    if _newclass:w = _swig_property(_basis.vector4_w_get, _basis.vector4_w_set)
    __swig_destroy__ = _basis.delete_vector4
    __del__ = lambda self : None;
vector4_swigregister = _basis.vector4_swigregister
vector4_swigregister(vector4)

class Edge2(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Edge2, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Edge2, name)
    __repr__ = _swig_repr
    __swig_setmethods__["p"] = _basis.Edge2_p_set
    __swig_getmethods__["p"] = _basis.Edge2_p_get
    if _newclass:p = _swig_property(_basis.Edge2_p_get, _basis.Edge2_p_set)
    def __init__(self): 
        this = _basis.new_Edge2()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _basis.delete_Edge2
    __del__ = lambda self : None;
Edge2_swigregister = _basis.Edge2_swigregister
Edge2_swigregister(Edge2)

class Edge3(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Edge3, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Edge3, name)
    __repr__ = _swig_repr
    __swig_setmethods__["p"] = _basis.Edge3_p_set
    __swig_getmethods__["p"] = _basis.Edge3_p_get
    if _newclass:p = _swig_property(_basis.Edge3_p_get, _basis.Edge3_p_set)
    def __init__(self): 
        this = _basis.new_Edge3()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _basis.delete_Edge3
    __del__ = lambda self : None;
Edge3_swigregister = _basis.Edge3_swigregister
Edge3_swigregister(Edge3)


def multiply_matrix(*args):
  return _basis.multiply_matrix(*args)
multiply_matrix = _basis.multiply_matrix
class matrix44(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, matrix44, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, matrix44, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _basis.new_matrix44(*args)
        try: self.this.append(this)
        except: self.this = this
    def __mul__(self, *args): return _basis.matrix44___mul__(self, *args)
    def set_identity(self): return _basis.matrix44_set_identity(self)
    def get_axis(self, *args): return _basis.matrix44_get_axis(self, *args)
    def _float(self): return _basis.matrix44__float(self)
    def _kfloat(self): return _basis.matrix44__kfloat(self)
    __swig_destroy__ = _basis.delete_matrix44
    __del__ = lambda self : None;
matrix44_swigregister = _basis.matrix44_swigregister
matrix44_swigregister(matrix44)

class Color(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Color, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Color, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _basis.new_Color(*args)
        try: self.this.append(this)
        except: self.this = this
    def _assign(self, *args): return _basis.Color__assign(self, *args)
    def _DWORD(self): return _basis.Color__DWORD(self)
    def ToRGB(self): return _basis.Color_ToRGB(self)
    __swig_destroy__ = _basis.delete_Color
    __del__ = lambda self : None;
Color_swigregister = _basis.Color_swigregister
Color_swigregister(Color)


def vec_normalize(*args):
  return _basis.vec_normalize(*args)
vec_normalize = _basis.vec_normalize

def vec_cross(*args):
  return _basis.vec_cross(*args)
vec_cross = _basis.vec_cross

def vec_dot(*args):
  return _basis.vec_dot(*args)
vec_dot = _basis.vec_dot

def build_matrix_perspective_fov_lh(*args):
  return _basis.build_matrix_perspective_fov_lh(*args)
build_matrix_perspective_fov_lh = _basis.build_matrix_perspective_fov_lh

def build_matrix_lookat_lh(*args):
  return _basis.build_matrix_lookat_lh(*args)
build_matrix_lookat_lh = _basis.build_matrix_lookat_lh

def build_matrix_rotation_axis(*args):
  return _basis.build_matrix_rotation_axis(*args)
build_matrix_rotation_axis = _basis.build_matrix_rotation_axis

def build_matrix_trans_rot_scale(*args):
  return _basis.build_matrix_trans_rot_scale(*args)
build_matrix_trans_rot_scale = _basis.build_matrix_trans_rot_scale

def arctan2radian(*args):
  return _basis.arctan2radian(*args)
arctan2radian = _basis.arctan2radian
class classinfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, classinfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, classinfo, name)
    __repr__ = _swig_repr
    def _is(self, *args): return _basis.classinfo__is(self, *args)
    __swig_setmethods__["name"] = _basis.classinfo_name_set
    __swig_getmethods__["name"] = _basis.classinfo_name_get
    if _newclass:name = _swig_property(_basis.classinfo_name_get, _basis.classinfo_name_set)
    __swig_setmethods__["parent_class"] = _basis.classinfo_parent_class_set
    __swig_getmethods__["parent_class"] = _basis.classinfo_parent_class_get
    if _newclass:parent_class = _swig_property(_basis.classinfo_parent_class_get, _basis.classinfo_parent_class_set)
    def __init__(self): 
        this = _basis.new_classinfo()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _basis.delete_classinfo
    __del__ = lambda self : None;
classinfo_swigregister = _basis.classinfo_swigregister
classinfo_swigregister(classinfo)

def vec_transform(*args):
  return _basis.vec_transform(*args)
vec_transform = _basis.vec_transform

class ref_counted(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ref_counted, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ref_counted, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _basis.new_ref_counted()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _basis.delete_ref_counted
    __del__ = lambda self : None;
    def addref(self): return _basis.ref_counted_addref(self)
    def release(self): return _basis.ref_counted_release(self)
    def get_refcount(self): return _basis.ref_counted_get_refcount(self)
ref_counted_swigregister = _basis.ref_counted_swigregister
ref_counted_swigregister(ref_counted)

class identifier(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, identifier, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, identifier, name)
    __repr__ = _swig_repr
    __swig_setmethods__["cs"] = _basis.identifier_cs_set
    __swig_getmethods__["cs"] = _basis.identifier_cs_get
    if _newclass:cs = _swig_property(_basis.identifier_cs_get, _basis.identifier_cs_set)
    __swig_setmethods__["counter"] = _basis.identifier_counter_set
    __swig_getmethods__["counter"] = _basis.identifier_counter_get
    if _newclass:counter = _swig_property(_basis.identifier_counter_get, _basis.identifier_counter_set)
    __swig_setmethods__["it"] = _basis.identifier_it_set
    __swig_getmethods__["it"] = _basis.identifier_it_get
    if _newclass:it = _swig_property(_basis.identifier_it_get, _basis.identifier_it_set)
    __swig_setmethods__["serial_number"] = _basis.identifier_serial_number_set
    __swig_getmethods__["serial_number"] = _basis.identifier_serial_number_get
    if _newclass:serial_number = _swig_property(_basis.identifier_serial_number_get, _basis.identifier_serial_number_set)
    def __init__(self): 
        this = _basis.new_identifier()
        try: self.this.append(this)
        except: self.this = this
    def _assign(self, *args): return _basis.identifier__assign(self, *args)
    def empty(self): return _basis.identifier_empty(self)
    def get_string_part(self): return _basis.identifier_get_string_part(self)
    def get_serial(self): return _basis.identifier_get_serial(self)
    __swig_destroy__ = _basis.delete_identifier
    __del__ = lambda self : None;
identifier_swigregister = _basis.identifier_swigregister
identifier_swigregister(identifier)
cvar = _basis.cvar

class object(ref_counted):
    __swig_setmethods__ = {}
    for _s in [ref_counted]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, object, name, value)
    __swig_getmethods__ = {}
    for _s in [ref_counted]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, object, name)
    __repr__ = _swig_repr
    __swig_getmethods__["get_classinfo"] = lambda x: _basis.object_get_classinfo
    if _newclass:get_classinfo = staticmethod(_basis.object_get_classinfo)
    __swig_getmethods__["constructor"] = lambda x: _basis.object_constructor
    if _newclass:constructor = staticmethod(_basis.object_constructor)
    def bind_classinfo(self): return _basis.object_bind_classinfo(self)
    def __init__(self): 
        this = _basis.new_object()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _basis.delete_object
    __del__ = lambda self : None;
    def get_name(self): return _basis.object_get_name(self)
    def set_name(self, *args): return _basis.object_set_name(self, *args)
    def _is(self, *args): return _basis.object__is(self, *args)
    def set_outer(self, *args): return _basis.object_set_outer(self, *args)
    def get_outer(self): return _basis.object_get_outer(self)
object_swigregister = _basis.object_swigregister
object_swigregister(object)

def object_get_classinfo():
  return _basis.object_get_classinfo()
object_get_classinfo = _basis.object_get_classinfo

def object_constructor():
  return _basis.object_constructor()
object_constructor = _basis.object_constructor


